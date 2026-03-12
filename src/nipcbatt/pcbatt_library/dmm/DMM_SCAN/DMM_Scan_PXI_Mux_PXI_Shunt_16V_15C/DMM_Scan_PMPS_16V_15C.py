# pylint: disable=C0200, C0103, C0301

"""" Defines class used for DMM Scan using PXI Mux and PXI Shunt """

import time
from typing import NamedTuple

from nipcbatt import switch
from nipcbatt import dmm
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingNISWITCH
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingNIDMM


class ScanResources(NamedTuple):
    """This class exists to be the return type of the initialize method of DmmScanPMPS.
       It contains 2 intialized switch sessions and an intitalized dmm session

    Args:
        NamedTuple: Built-in datatype to hold abstract tuples
    """
    mux_generation: switch.StaticDigitalPathGeneration
    shunt_generation: switch.StaticDigitalPathGeneration
    dmm_generation: dmm.MixedMeasurement

class MeasurementResult(NamedTuple):
    """This class is the return type of the configure_and_measure method of DmmScanPMPS.
       It contains:
        sessions: The references to the switch and dmm sessions used in the measurement
        scan_time: The total elapsed time of the scan 
        formatted_measurements: The list of all completed DMM measurments
        execution_settings: The list of execution settings used in each measurement
        raw_measurements: The list of raw measurements captured during the scan

    Args:
        
    """
    sessions: ScanResources
    scan_time: float
    formatted_measurements: list
    execution_settings: list
    raw_measurements: list
  


class DmmScanPMPS(BuildingBlockUsingNIDMM, BuildingBlockUsingNISWITCH):
    """This class represents the set of properties and methods needed
       to complete a scan of different measurements using a DMM 
       and various switch configurations

    Args:
        BuildingBlockUsingNISWITCH: The NI-SWITCH building block
        BuildingBlockUsingNIDMM: The NI-DMM building block
    """

    def initialize(
            self,
            mux_resource_name = "Sim_MUX",
            mux_topology_name = "2527/2-Wire Dual 16x1 Mux",
            shunt_resource_name = "Sim_SHUNT",
            shunt_topology_name = "2568/31-SPST",
            dmm_resource_name = "Sim_DMM",
            powerline_freq = 50,
            close_all_shunts = True
    ) -> ScanResources:
        
        """Initializes the switch and dmm objects to be used in the dmm scan

        Args:
            mux_resource_name (str): The name of the mux resource. Defaults to "Sim_MUX".
            mux_topology_name (str): The name of the mux topology. Defaults to "2527/2-Wire Dual 16x1 Mux".
            shunt_resource_name (str): The name of the shunt resource. Defaults to "Sim_SHUNT".
            shunt_topology_name (str): The name of the shunt topology. Defaults to "2568/31-SPST".
            dmm_resource_name (str=): The name of the dmm resource. Defaults to "Sim_DMM".
            powerline_freq (int): The power grid frequency. Defaults to 50.
            close_all_shunts (bool): If true, all shunt paths will be closed. Defaults to True.

        Returns:
            ScanResources: A tuple of two initialized switch sessions and one initalized dmm session
        """
        
        #Generate switch sessions for scan
        mux_generation = switch.StaticDigitalPathGeneration()
        shunt_generation = switch.StaticDigitalPathGeneration()

        # Generate dmm session for mixed measurements
        dmm_generation = dmm.MixedMeasurement()
        
        #Initialize sessions
        mux_generation.close()
        shunt_generation.close()
        dmm_generation.close()

        mux_generation.initialize(mux_resource_name, mux_topology_name, reset_device=True, simulate=False)
        shunt_generation.initialize(shunt_resource_name, shunt_topology_name, reset_device=True, simulate=False)
        dmm_generation.initialize(dmm_resource_name, powerline_freq)

        # Close all shunt relays from 16 to 30 (NI 2568) in a fixed
        # channel topology mapping - option to open shunts only for 2-wire resistance measuerments
        if close_all_shunts:

            #cycle across all 16 channel pairs
            for i in range(15):

                #adjust channel index
                idx = i + 16

                #declare channels
                ch1 = f'ch{idx}'
                ch2 = f'com{idx}'

                #create channel parameters and state objects
                channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch1, ch2)
                state = switch.StaticDigitalPathGenerationStateParameters(True)

                #configure terminal and timing settings
                ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
                timing_settings = switch.StaticDigitalPathGenerationTimingParameters()
                config = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

                #configure and generate
                shunt_generation.configure_and_generate(config)

        #return initialized objects
        return ScanResources(mux_generation, shunt_generation, dmm_generation)


    def configure_and_measure(
            self,
            resource_handles: ScanResources,
            scan_configuration: list,
            close_all_shunts: bool = True,
            verbose=True
        ) -> MeasurementResult:

        """This method executes a complete scan across every measurement which is
           provided in the scan_configuration input parameter

        Args:
            resource_handles (ScanResources): The two switch sessions and dmm session to use
            scan_configuration (list): Populate this list with every measurement you 
              wish to make during the scan
            close_all_shunts: Set to True if all shunts were closed during initialize()
            verbose(bool): If True, this will print out all of the measurement results
              from the scan. Pass False if you do not wish to print results to console

        Returns:
            MeasurementResult: The results of all measurements
            ScanResources: Handles to each session used
        """
        # extract individual resource handles from resource_handles input
        mux_generation = resource_handles.mux_generation
        shunt_generation = resource_handles.shunt_generation
        dmm_generation = resource_handles.dmm_generation

        # extract range & function, resolution in digits and channel from scan configuration
        function_range_resolution = []
        channel_list = []
        for cfg in scan_configuration:
            channel_list.append(cfg[0])
            function_range_resolution.append((cfg[1], cfg[2]))

        # pair channels with respective com -- ch 0-15 -> com0, ch 16-30 -> com1
        channel_pairs = []
        for ch in channel_list:
            if ch < 16:
                pair = (ch, 'com0')
            else:
                pair = (ch, 'com1')
            channel_pairs.append(pair)

        # Data structures for output
        raw_measurements = []
        formatted_measurements = []
        execution_settings = []

        # previous function, range, resolution for comparison
        prev = None

        # start wall time counter
        start_time = time.perf_counter()

        # Main Scan Loop
        for i in range(len(scan_configuration)):

            #extract ch (int) and com (string)
            ch, com = channel_pairs[i][0], channel_pairs[i][1]
            channel_name = 'ch' + str(ch)

            # MUX handling -- close MUX channel for respective ch#, com#
            channel_params = switch.StaticDigitalPathGenerationChannelParameters(channel_name, com)
            state = switch.StaticDigitalPathGenerationStateParameters(True) # Use TRUE value to CLOSE mux channel
            ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
            timing_settings = switch.StaticDigitalPathGenerationTimingParameters()
            mux_config = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

            # execute configure and generate for max channel pair
            mux_generation.configure_and_generate(mux_config)


            # SHUNT handling -- if channel is a current channel, open SHUNT
            if ch >= 16 and close_all_shunts:   # current channels are ch16 - ch30
                com = 'com' + str(ch)
                channel_params = switch.StaticDigitalPathGenerationChannelParameters(channel_name, com)
                state = switch.StaticDigitalPathGenerationStateParameters(False)  # False state to OPEN shunt
                ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
                timing_settings = switch.StaticDigitalPathGenerationTimingParameters()
                shunt_config = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

                # execute configure and generate for shunt channel pair
                shunt_generation.configure_and_generate(shunt_config)


            # DMM handling -- configure and acquire measurement
            function_and_range = function_range_resolution[i][0]
            resolution = function_range_resolution[i][1]

            # if previous function, range, and resolution are the same skip dmm configuration, otherwise configure
            if prev != function_range_resolution[i]:
                
                # instantiate parameters object
                params = dmm.MixedMeasurementFunctionParameters(function_and_range, resolution)
                dmm_generation.configure_measurement_function(params)

            # measure only
            dmm_read = dmm_generation.acquire_measurement(resolution.value)

            # SHUNT handling -- close current shunt if opened
            if ch >= 16 and close_all_shunts:   # current channels are ch16 - ch30
                com = 'com' + str(ch)
                channel_params = switch.StaticDigitalPathGenerationChannelParameters(channel_name, com)
                state = switch.StaticDigitalPathGenerationStateParameters(True)  # True state to CLOSE shunt
                ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
                timing_settings = switch.StaticDigitalPathGenerationTimingParameters()
                shunt_config = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

                # execute configure and generate for shunt channel pair 
                shunt_generation.configure_and_generate(shunt_config)

            # MUX handling -- open MUX channel to release it
            ch, com = channel_pairs[i][0], channel_pairs[i][1]
            channel_name = 'ch' + str(ch)
            channel_params = switch.StaticDigitalPathGenerationChannelParameters(channel_name, com)
            state = switch.StaticDigitalPathGenerationStateParameters(False) # Use FALSE value to OPEN mux channel
            ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
            timing_settings = switch.StaticDigitalPathGenerationTimingParameters()
            mux_config = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

            # execute configure and generate for max channel pair
            mux_generation.configure_and_generate(mux_config)

            #measure elapsed time
            switch_time = time.perf_counter() - start_time

            #store raw output
            meas_type = params.measurement_function.value[0].name
            value = dmm_read.measurement
            raw_data = (channel_name, value, meas_type)
            raw_measurements.append(raw_data)

            #store formatted measurement output
            data = dmm_generation.acquire_measurement(resolution.value)
            meas = data.measurement
            formatted_meaurement = (channel_name, meas['Formatted_Measurement'], switch_time)
            formatted_measurements.append(formatted_meaurement)

            #store execution ettings
            exec_settings = data.dmm_execution_settings
            execution_settings.append(exec_settings)

            #store current function/range/resolution settings for comparison in next loop
            prev = function_range_resolution[i]

            ######### END MAIN LOOP #####################

        #capture total scan time
        total_time_elapsed = time.perf_counter() - start_time

        #if verbose = True, print results to console
        if verbose:
            print()
            print('------------- SCAN TIME --------------')
            print('Total Scan Time (s):', f'{total_time_elapsed: .2f}')
            print('\n')

            print('------- FORMATTED MEASUREMENTS -------')
            print(f'{"Channel":<10} {"Measurement":<18} {"Time":>8}')

            for i in range(len(formatted_measurements)):
                measurement = formatted_measurements[i]
                full_unit = raw_measurements[i][2]

                if 'DC' in full_unit:
                    unit = '(dc)'
                elif 'AC' in full_unit:
                    unit = '(ac)'
                else:
                    unit = '(ohm)'

                channel = measurement[0]
                value = f'{measurement[1]} {unit}'
                switch_time = measurement[2]

                print(f'{channel:<10} {value:<18} {switch_time:>8.3f}')
            print('\n')

            print('--------- EXECUTION SETTINGS ---------')
            for setting in execution_settings:
                for key, value in setting.items():
                    print(str(key) + ': ' + str(value))
                print()
            print('\n')


            #prepare raw measurements for output -- get largest width
            values_as_str = [
                f"{m[1]['Measured_Value']:.16g}" for m in raw_measurements
            ]
            value_width = max(len(v) for v in values_as_str)

            print('----------- RAW MEASUREMENTS -------------')
            print(f'{"Channel":<10} {"Value":^23} {"Units":^8}')

            for measurement, value_str in zip(raw_measurements, values_as_str):
                channel = measurement[0]
                unit = measurement[1]['Unit']

                print(f'{channel:<10} {value_str:<{value_width}} {unit:>8}')
            print('\n')

        # prepare output
        output = MeasurementResult(
            ScanResources(mux_generation, shunt_generation, dmm_generation),
            total_time_elapsed, 
            formatted_measurements,
            execution_settings,
            raw_measurements
        )

        #return measurement result
        return output


    def close(self, resource_handles: ScanResources) -> None:
        """This method disconnects, closes, and releases the resources

        Args:
            resource_handles (ScanResources): Contains the sessions handles used in the scan
        """
        mux_generation = resource_handles.mux_generation
        shunt_generation = resource_handles.shunt_generation 
        dmm_generation = resource_handles.dmm_generation

        #close and release all resources
        mux_generation.close()
        shunt_generation.close()
        dmm_generation.close()







