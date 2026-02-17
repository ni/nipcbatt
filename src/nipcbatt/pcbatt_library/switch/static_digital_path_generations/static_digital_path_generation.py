"""Use this class to connect switch paths is a test fixture"""
# pylint: disable=W0611

from typing import List
from varname import nameof

import nidaqmx.constants
import nidaqmx.errors
import nidaqmx.stream_writers
import nidaqmx.system
import numpy as np

import niswitch

from nipcbatt.pcbatt_library.switch.static_digital_path_generations.static_digital_path_data_types import(
    StaticDigitalPathGenerationModuleCharacteristics,
    StaticDigitalPathGenerationChannelParameters,
    StaticDigitalPathGenerarionPathStatus,
    StaticDigitalPathGenerationStateParameters,
    StaticDigitalPathGenerationTimingParameters,
    StaticDigitalPathGenerationTerminalAndStateSettings
)

from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingNISWITCH



class StaticDigitalPathGeneration(BuildingBlockUsingNISWITCH):
    """This class represents the set of digital path connections the
       user wishes to create on the switch matrix

    Args:
        BuildingBlockUsingNISWITCH: The NI-SWITCH building block
    """

    def initialize(self,
                   switch_resource_name: str,
                   topology_name: str,
                   reset_device: bool = True,                
                   simulate: bool = False
        ) -> None:
        """Initializes the session to prepare for path generation

        Args:
            switch_resource_name (str): The name of the switch
            resource to be used
        """
        if self.is_session_initialized:
            return
        
        #input validation
        Guard.is_not_none(switch_resource_name, nameof(switch_resource_name))
        Guard.is_not_empty(switch_resource_name, nameof(switch_resource_name))

        Guard.is_not_none(topology_name, nameof(topology_name))
        Guard.is_not_empty(topology_name, nameof(topology_name))

        Guard.is_not_none(reset_device, nameof(reset_device))    
        if not isinstance(reset_device, bool):
            raise TypeError(f"{nameof(reset_device)} must be a bool.")

        #clean input 
        switch_resource_name = switch_resource_name.strip()
        topology_name = topology_name.strip()

        #create session with parameters
        session = niswitch.Session(
            resource_name=switch_resource_name,
            topology=topology_name,
            simulate=simulate,
            reset_device=reset_device,
        )
        
        #assign session
        self._instrument = session

    def close(self):
        """Disconnects all channels, closes the session and returns the resource"""
        if not self.is_session_initialized:
            return
        
        #disconnect all connections
        self.session.disconnect_all()

        #close the session
        self.session.close()

    def configure_and_generate(
            self, 
            terminal_and_state_settings: StaticDigitalPathGenerationTerminalAndStateSettings,
            timing_settings: StaticDigitalPathGenerationTimingParameters
    ) -> StaticDigitalPathGenerarionPathStatus:
        
        """Creates the connections defined within the terminal and state settings
           and generates a path status indicating if the operation was succesful

           Args:
                terminal_and_state_settings: Contains both the channel and state to employ
        """
        
        #extract channels and state to employ
        channel_one = terminal_and_state_settings.channel_parameters.channel_one
        channel_two = terminal_and_state_settings.channel_parameters.channel_two
        connect = terminal_and_state_settings.connection_state.connect

        #extract maximum wait for debounce time
        max_wait = timing_settings.max_debounce_wait

        #verify channels can be connected
        path_capability = self.session.can_connect(channel_one, channel_two)

        #connect/disconnect/ignore depending on path capability
        if path_capability.PATH_AVAILABLE or path_capability.PATH_EXISTS:

            #if connecting make connection, else disconnect
            if connect:
                self.session.connect(channel_one, channel_two)
            else:
                self.session.disconnect(channel_one, channel_two)

            #wait for maximum debounce time
            self.session.wait_for_debounce(max_wait)

        #if the path is not available or doesn't exist, do nothing
        else:
            pass

        #return path capbility inside path status object
        return StaticDigitalPathGenerarionPathStatus(path_capability)

        
        





