from typing import List

import niswitch

from varname import nameof 

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard

class StaticDigitalPathGenerationChannelParameters(PCBATestToolkitData):
    """Defines the channel value names assigned for the switch connection"""    

    def __init__(self, channel_one: str, channel_two: str) -> None:
        """Creates an instance of StaticDigitalPathGenerationChannelParameters

        Args:
            channel_one (str): The name of the first channel
            channel_two (str): The name of the second channel
        """

        #input validation
        Guard.is_not_none_nor_empty_nor_whitespace(channel_one, nameof(channel_one))
        Guard.is_not_none_nor_empty_nor_whitespace(channel_two, nameof(channel_two))

        #assign values
        self._channel_one = channel_two
        self._channel_two = channel_two

    @property 
    def channel_one(self) -> str:
        """
        :type:'str': Returns the name of channel one
        """
        return self._channel_one
    
    @property
    def channel_two(self) -> str:
        """
        :type:'str': Returns the name of channel two
        """
        return self._channel_two
    
class StaticDigitalPathGenerationStateParameters(PCBATestToolkitData):
    """Creates an instance of StaticDigitalPathGenerationStateParameters"""

    def __init__(self, connect: bool) -> None:
        """Defines whether to disconnect or connect a particular path 

            Args:
                connect(bool): Indicates whether to make or break a given connection
        """

        #inout validation
        Guard.is_not_none(connect, nameof(connect))
        Guard.is_not_empty(connect, nameof(connect))
        Guard.is_not_float(connect, nameof(connect))

        # assign values 
        self._connect = connect

    @property 
    def connect(self) -> bool:
        """  
        :type:'boolean': Gets the boolean value to write
        """
        return self._connect
    
class StaticDigitalPathGenerationTimingParameters(PCBATestToolkitData):    
    """ Creates an instance of StaticDigitalPathGenerationTimingParameters """

    def __init__(self, max_debounce_wait: int):
        """Defines the maximum wait for debounce time

        Args:
            max_debounce_wait (int): The maximum time to wait for debounce
        """

        #Input Validation
        Guard.is_not_none(max_debounce_wait, nameof(max_debounce_wait))
        Guard.is_greater_than_or_equal_to_zero(max_debounce_wait, nameof(max_debounce_wait))

        #assign values
        self._max_debounce_wait = max_debounce_wait

    @property
    def max_debounce_wait(self) -> int:
        """   
        :type:int
        """
        return self._max_debounce_wait
    
class StaticDigitalPathGenerationTerminalAndStateSettings(PCBATestToolkitData):
    """Creates an instance of StaticDigitalPathGenerationTerminalAndStateSettings"""

    def __init__(self,
                 channel_parameters: StaticDigitalPathGenerationChannelParameters,
                 connection_state: StaticDigitalPathGenerationStateParameters
    ):
        """Aggragates channel and timing parameters into a single class

        Args:
            channel_parameters (StaticDigitalPathGenerationChannelParameters): The channels
                involved in the connection
            timing_parameters (StaticDigitalPathGenerationStateParameters): The connection
                state to be implemented
        """
        #input validation
        Guard.is_not_none(channel_parameters, nameof(channel_parameters))
        Guard.is_not_none(connection_state, nameof(connection_state))

        #assign values 
        self._channel_parameters = channel_parameters 
        self._connection_state = connection_state 

    @property
    def channel_parameters(self) -> StaticDigitalPathGenerationChannelParameters:
        """  
        :type: StaticDigitalPathGenerationChannelParameters
        """
        return self._channel_parameters
    
    @property 
    def connection_state(self) -> StaticDigitalPathGenerationStateParameters:
        """   
        :type: StaticDigitalPathGenerationStateParameters
        """
        return self._connection_state
        

class StaticDigitalPathGenerationModuleCharacteristics(PCBATestToolkitData):
    """  Defines the max voltage and current characteristics of the switch """
    
    def __init__(self, max_dc_voltage: float, max_ac_voltage: float, max_switching_dc_current: float, max_switching_ac_current: float) -> None:
        """Creates an instance of StaticDigitalPathGenerationModuleCharacteristics

        Args:
            max_dc_voltage (float): The rated maximum DC voltage of the topology 
            max_ac_voltage (float): The rated maximum AC voltage of the topology 
            max_switching_dc_current (float): The rated maximum DC switching current of the topology
            max_switching_ac_current (float): The rated maximum AC switching current of the topology
        """

        #input validation 
        Guard.is_not_none(max_dc_voltage, nameof(max_dc_voltage))
        Guard.is_greater_than_or_equal_to_zero(max_dc_voltage, nameof(max_dc_voltage))

        Guard.is_not_none(max_ac_voltage, nameof(max_ac_voltage))
        Guard.is_greater_than_or_equal_to_zero(max_ac_voltage, nameof(max_ac_voltage))

        Guard.is_not_none(max_switching_dc_current, nameof(max_switching_dc_current))
        Guard.is_greater_than_or_equal_to_zero(max_switching_dc_current, nameof(max_switching_dc_current))

        Guard.is_not_none(max_switching_ac_current, nameof(max_switching_ac_current))
        Guard.is_greater_than_or_equal_to_zero(max_switching_ac_current, nameof(max_switching_ac_current))

        # assign values
        self._max_dc_voltage = max_dc_voltage
        self._max_ac_voltage = max_ac_voltage
        self._max_switching_dc_current = max_switching_dc_current
        self._max_switching_ac_current = max_switching_ac_current

    @property
    def max_dc_voltage(self) -> float:
        """  
        :type:'float': Returns the max DC voltage for the topology 
        """
        return self._max_dc_voltage
    
    @property 
    def max_ac_voltage(self) -> float:
        """  
        :type:'float': Returns the max AC voltage for the topology
        """
        return self._max_ac_voltage
    
class StaticDigitalPathGenerarionPathStatus(PCBATestToolkitData):
    """ Defines the status of the path"""

    def __init__(self, path_status: niswitch.PathCapability) -> None:
        """Creates an instance of StaticDigitalPathGenerationPathStatus

        Args:
            path_status (str): Displays whether or not the switch path is available
        """

        #input validation
        Guard.is_not_none(path_status, nameof(path_status))

        #assign values 
        self._path_status = path_status

    @property
    def path_status(self) -> niswitch.PathCapability:
        """  
        :type:'string': Returns the availability of the path for the given connections 
        """
        return self._path_status
    
