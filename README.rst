+------------+------------------------------------------------------------------------------------+
| **Info**   | A python based package providing a set of generation, measurement and              | 
|            | communication building blocks, that can be used to perform PCB Assembly tests.     |
+------------+------------------------------------------------------------------------------------+
| **Author** | National Instruments                                                               |
+------------+------------------------------------------------------------------------------------+

.. contents:: Table of Contents
   :depth: 1
   :backlinks: none

About
=====

The **nipcbatt** package contains an API (Application Programming Interface) for interacting with 
the NI-DAQmx driver and with LabVIEW runtime to perform measurement, generation and communication 
operations. The package is implemented in Python, as a highly object-oriented package.

Python PCB Assembly Test Toolkit or **nipcbatt** is a collection of Measurement Library, Automation Examples,
Test Demo Example developed in Python along with Documentation for PCB Assembly electrical functional test.

**nipcbatt** package is focused on NI DAQ devices hardware, and compatible with NI PC Based DAQ, CompactDAQ,
TestScale and high level enough to be applicable or scalable for other instruments with similar functionality and 
resources on any platform.

Documentation
-------------

Refer to the `Python PCB Assembly Test Toolkit - Getting Started <https://github.com/ni/nipcbatt/blob/main/docs/Python%20PCB%20Assembly%20Test%20Toolkit%20-%20Getting%20Started.pdf>`_ guide for
getting started steps including installation and setup procedures, and steps to run example test sequences. 
Refer to the `User Manual <https://github.com/ni/nipcbatt/blob/main/docs/Python%20PCB%20Assembly%20Test%20Toolkit%20-%20User%20Manual.pdf>`_ for an overview of Toolkit concepts, and measurement fundamentals.

Supported Features
------------------

.. list-table::
   :widths: 25 55 20
   :header-rows: 0

   * - Feature name
     - Description
     - Acronym
   * - Power Supply Source and Measure Library
     - This feature allows initializing, configuring, sourcing, measuring, and closing user configurable power supply for power supply measurements (TestScale only).
     - PSSM
   * - DC-RMS Voltage Measurement Library
     - This feature allows initializing, configuring, measuring, and closing user configurable analog input pins for voltage measurements.
     - DRVM
   * - DC Voltage Generation Library
     - This feature allows initializing, configuring, generating, and closing user configurable analog output pins for DC voltage generations.
     - DRVG
   * - DC-RMS Current Measurement Library
     - This feature allows initializing, configuring, measuring, and closing user configurable analog input pins for current measurements.
     - DRCM
   * - Time Domain Voltage Measurement Library
     - This feature allows initializing, configuring, measuring, and closing user configurable analog input pins for voltage measurement and derive time domain measurement for the measured waveforms.
     - TDVM
   * - Frequency Domain Voltage Measurement Library
     - This feature allows initializing, configuring, measuring, and closing user configurable analog input pins for voltage measurement and derive frequency domain measurement for the measured waveforms.
     - FDVM
   * - Signal Voltage Generation Library
     - This feature allows initializing, configuring, generate, and closing different waveform voltage signals like tones (single/multi) or square windows, over a given generation time(s) on user configurable analog output pins.
     - SVG
   * - Static Digital State Measurement Library
     - This feature allows initializing, configuring, sourcing, measuring, and closing user configurable digital input pins.
     - SDSM
   * - Static Digital State Generation Library
     - This feature allows initializing, configuring, sourcing, generate, and close on user configurable digital output pins.
     - SDSG
   * - Temperature Thermistor Measurement Library
     - This feature allows initializing, configuring, measuring, and closing user configurable analog input pins to derive temperature measurements from voltage excited NTC typed Thermistor devices.
     - TTRM
   * - Temperature RTD Measurement Library
     - This feature allows initializing, configuring, sourcing, measuring, and closing user configurable analog input pins for temperature measurements from Resistance Temperature Detector (RTD).
     - TRTDM
   * - Temperature Thermocouple Measurement Library
     - This feature allows initializing, configuring, sourcing, measuring, and closing user configurable analog input pins to derive temperature measurements from Thermocouples.
     - TTCM
   * - Dynamic Digital Pattern Measurement Library
     - This feature provides options to measure digital patterns through the specified lines.
     - DDPM
   * - Dynamic Digital Pattern Generation Library
     - This feature provides options to generate digital patterns, an array of digital samples in the specified IO lines.
     - DDPG
   * - Digital Clock Generation Library
     - This feature allows initializing, configuring, generate and closing on user configurable terminals using counters.
     - DCG
   * - Digital Pulse Generation Library
     - This feature allows initializing, configuring, generate and closing on user configurable terminals using counters.
     - DPG
   * - Digital Frequency Measurement Library
     - This feature allows initializing, configuring, measuring and closing on user configurable PFI line using the selected counter for digital frequency measurement.
     - DFM
   * - Digital PWM Measurement Library
     - This feature allows initializing, configuring, generating and closing on user configurable PFI line using the selected counter for digital PWM measurement.
     - DPWMM
   * - Digital Edge Count Measurement Library
     - This feature allows initializing, configuring, generating and closing on user configurable PFI line using the selected counter for Edge Counting using Software and Hardware Timers.
     - DECM
   * - Communication Library
     - This feature allows initializing, configuring, read and writing data, and closing on I2C, SPI and Serial Communication devices.
     - COM
   * - Synchronization Library
     - This feature allows synchronizing between specified source and output terminals for the given DAQmx Task.
     - RSS


Required Drivers
-----------------


| NI-DAQmx: 2023 Q3 and above 
| LabVIEW Runtime: 2022 Q3 and above (64 bit) 
| NI-845x: 2022 Q3 and above 
| NI-VISA: 2023 Q2 and above 
| NI-Serial: 2023 Q2 and above 

Supported Hardware
------------------

| NI PC Based DAQ
| CompactDAQ
| TestScale
| Any DAQmx devices with similar functionality and resources.


Operating System Support
------------------------

nipcbatt supports Windows 10 and 11 systems where the supported drivers are 
installed. Refer to `NI Hardware and Operating System Compatibility <https://www.ni.com/r/hw-support>`_ for 
which versions of the driver support your hardware on a given operating system.

Python Version Support
----------------------

**nipcbatt** supports Python 3.9+ (64 bit)

Installation
============

You can use `pip <http://pypi.python.org/pypi/pip>`_ to download **nipcbatt** from
`PyPI <https://pypi.org/project/nipcbatt/>`_ and install it::

  $ python -m pip install nipcbatt


Manual Driver Installation
--------------------------

Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the latest version of **Python PCB Assembly Test
Toolkit**. It is recommended you continue to install the NI-DAQmx Runtime with Configuration Support and NI Hardware Configuration Utility from the Additional items
checklist as it is required to access and manage hardware. All other recommended Additional items
are not necessary for nipcbatt to function, and they can be removed to minimize installation size. 

Getting Started
===============

In order to use the **nipcbatt package**, you must have at least one DAQ (`Data Acquisition <https://www.ni.com/en/shop/data-acquisition.html>`_)
device installed on your system. Both physical and simulated devices are supported. The examples below use PC 
based DAQ device (PCIe-6363). You can use NI MAX or NI Hardware 
Configuration Utility to verify and configure your devices.


Finding and configuring device name in **NI MAX**:

.. image:: https://raw.githubusercontent.com/ni/nidaqmx-python/ca9b8554e351a45172a3490a4716a52d8af6e95e/max_device_name.png

Finding and configuring device name in **NI Hardware Configuration Utility**:

.. image:: https://raw.githubusercontent.com/ni/nidaqmx-python/ca9b8554e351a45172a3490a4716a52d8af6e95e/hwcu_device_name.png

Then refer to the Getting Started guide to proceed with testing. The Guide can be found at this location: 
*"\\nipcbatt-1.x\\src\\docs\\Python PCB Assembly Test Toolkit - Getting Started.pdf"*


Key Concepts in Python PCBATT
=============================

1. Libraries
-------------

All the measurement libraries consist of three main methods which have to be used in the following order:

- Initialize:
 
   Used to initialize a DAQmx using either physical or global virtual channels 
   provided to perform the respective task.

   This is done by calling the intialize() method on the class instance.

 
- Configure and Generate/Configure and Measure:
 
   Configures, Initiates and Measure/Generate for an input/output 
   task respectively. Also, can return raw data for external custom post 
   analysis and measurements from embedded analysis(selectable/optional)
 
   This is done by calling the
   configure_and_measure()/configure_and_generate() method on the class instance.

- Close:
 
   Closes the DAQmx tasks and clears resources.

   This is done by calling the close() method on the class instance.

2. Features and Utilities
-------------------------

- Virtual Channels 

   Virtual channels, or sometimes referred to generically as channels, are software entities that encapsulate the physical channel along with 
   other channel specific information (e.g.: range, terminal configuration, and custom scaling) that formats the data. A physical channel is a 
   terminal or pin at which you can measure or generate an analog or digital signal. A single physical channel can include more than one 
   terminal, as in the case of a differential analog input channel or a digital port of eight lines. Every physical channel on a device has a unique 
   name (for instance, cDAQ1Mod4/ai0, Dev2/ao5, and Dev6/ctr3) that follows the NI-DAQmx physical channel naming convention. 
   Refer to `NI-DAQmx Channel <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/chans.html>`_ for more information.

- Logger

   The logger is a feature which comes along with the package as a part of PCBATT Utilities and helps in 
   storing configuration details and results for every run of the sequences. It can be used to store results 
   in the *.txt* or *.csv* file formats. The logger stores results for every run in the same file. Example usage of the logger can be found 
   in the automation sequences.

- Save Traces

   This Utility works in a similar manner as the logger but it saves configuration settings and results for each run in separate files.
   Example usage of the save_traces module can be found in the validation examples.



Usage
=============
 
1. Validation Examples
---------------------------
 
Validation examples are created as examples for testing and validating a pair of
libraries together, where one library is used for generation and another for measurement.
The validation examples can be found in this location in the installed library.

“\\<venv>\\Lib\\site-packages\\nipcbatt\\pcbatt_validation_examples”

Or refer to the location given below if you are using the downloaded
source code:

“\\nipcbatt-1.x\\src\\nipcbatt\\pcbatt_validation_examples”

 
2. Automation Sequences
-----------------------

Automation sequences are examples of using libraries for real time
scenarios like microphone tests, LED tests and so on. Automation sequences are tested in simulation mode.

Following is the list of Automation Sequences provided as a part of the package.

a. action_button_tests

b. audio_tests

c. communication_tests

d. digital_io_tests

e. led_tests

f. microphone_tests

g. power_supply_tests

h. sensor_tests

i. synchronization_tests

The Automation Sequences can be found in this location using the installed package:

“\\<venv>\\Lib\\site-packages\\nipcbatt\\pcbatt_automation”

Or refer to the location given below if you are using source code:

“\\nipcbatt-1.x\\src\\nipcbatt\\pcbatt_automation”
 
3. Functional Test Demo Sequence
---------------------------------
 
FT demo sequence is an example for creating a test sequence using
libraries with applying test limits on the results to determine whether the test is a pass or a fail.

Please refer to the FT Demo Sequence in the location.

“\\<venv>\\Lib\\site-packages\\nipcbatt\\pcbatt_ft_demo_test_sequence”

Or refer to the location given below if you are using source code:

“\\nipcbatt-1.x\\src\\nipcbatt\\pcbatt_ft_demo_test_sequence”



Bugs / Feature Requests
=======================

To report a bug or submit a feature request, please use this `link <https://www.ni.com/my-support/s/service-requests>`_.
Or write an email to : `Customer Requests <90006a91.emerson.onmicrosoft.com@amer.teams.ms>`_


License
========
**nipcbatt** is licensed under an MIT-style license. Other incorporated projects may be licensed under different licenses. All 
licenses allow for non-commercial and commercial use.

