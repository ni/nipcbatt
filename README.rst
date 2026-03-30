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

The **nipcbatt** package provides APIs (Application Programming Interface) for interacting with 
the NI_DMM, NI-SWITCH, NI-DAQmx driver and with LabVIEW runtime to perform measurement, generation and communication 
operations. The package is implemented in Python, as a highly object-oriented package.

Python PCB Assembly Test Toolkit or **nipcbatt** is a collection of Measurement Library, Automation Examples,
Test Demo Example developed in Python along with Documentation for PCB Assembly electrical functional test.

**nipcbatt** package is focused on NI DAQ, DMM, and SWITCH devices hardware, and compatible with NI PC Based DAQ, CompactDAQ, NI-DMM,
TestScale and high level enough to be applicable or scalable for other instruments with similar functionality and 
resources on any platform.

Documentation
-------------

Refer to the `Python PCB Assembly Test Toolkit - Getting Started <https://github.com/ni/nipcbatt/blob/main/src/nipcbatt/docs/Python%20PCB%20Assembly%20Test%20Toolkit%20-%20Getting%20Started.pdf>`_ guide for
getting started steps including installation and setup procedures, and steps to run example test sequences. 
Refer to the `User Manual <https://github.com/ni/nipcbatt/blob/main/src/nipcbatt/docs/Python%20PCB%20Assembly%20Test%20Toolkit%20-%20User%20Manual.pdf>`_ for an overview of Toolkit concepts and measurement 
fundamentals, including a brief overview of each library and automation sequences.

Supported Features
------------------

.. list-table::
   :widths: 25 55 20
   :header-rows: 0

   * - Feature name
     - Description
     - Acronym
   * - DMM Measurement Libraries
     - A collection of methods to perform DMM measurements using NI-DMM driver.
     - dmm
   * - DAQ Measurement Libraries
     - A collection of methods to perform measurements using NI-DAQmx driver.
     - daq
   * - SWITCH Measurement Libraries
     - A collection of methods to control Switch hardware, and switch paths using the NI-SWITCH driver.
     - switch
   * - DMM Scan Measurement Libraries
     - A collection of methods to perform measurements using NI-DMM and NI-SWITCH driver.
     - dmm_scan
   * - Communication Libraries
     - A collection of methods to perform communication operations (for example I2C, SPI, and serial) using NI-845x and NI-VISA drivers.
     - comm


Library imports and migrations
-------------------------------

    In this release the instrument-specific measurement libraries are exposed as subpackages under the top-level
    `nipcbatt` package. Example usage:

    .. code-block:: python

      from nipcbatt import daq
      drvg = daq.DcVoltageGeneration()
      drvg.initialize(analog_output_channel_expression="Sim_PC_basedDAQ/ao0")

    Few classes remain accessible directly from `nipcbatt` (for
    example `nipcbatt.MeasurementExecutionType`). However, explicit subpackage imports are the recommended approach 
    for all new code. To migrate existing code, update imports and references from:

    .. code-block:: python

      # Not recommended ❌
      import nipcbatt
      drvg = nipcbatt.DcVoltageGeneration()

    to the explicit subpackage form:

    .. code-block:: python

      # Recommended ✅
      from nipcbatt import daq
      drvg = daq.DcVoltageGeneration()

    See `Migration Guide for nipcbatt 2.0.0 <https://github.com/ni/nipcbatt/blob/main/src/nipcbatt/docs/migration_guide_api.md>`_ 
    for a complete list of class mappings, and all available subpackage classes.


Required Drivers
-----------------


- NI-DMM: 2023 Q4 and above
- NI-SWITCH: 2023 Q4 and above 
- NI-DAQmx: 2023 Q3 and above 
- LabVIEW Runtime: 2022 Q3 and above (64 bit) 
- NI-845x: 2022 Q3 and above 
- NI-VISA: 2023 Q2 and above 
- NI-Serial: 2023 Q2 and above 
  
Visit `ni.com/downloads <http://www.ni.com/downloads/>`_  or visit `NI Package Manager <https://www.ni.com/en/support/downloads/software-products/download.package-manager.html>`_ to download the Required Drivers.


Supported Hardware
------------------

- DMM devices compatible with the NI-DMM driver
- Switch devices compatible with the NI-SWITCH driver
- Any DAQmx devices with similar functionality and resources
- NI PC-Based DAQ
- CompactDAQ
- TestScale


Operating System Support
------------------------

**nipcbatt** supports Windows 10 and 11 systems where the supported drivers are 
installed. Refer to `NI Hardware and Operating System Compatibility <https://www.ni.com/r/hw-support>`_ for 
which versions of the driver support your hardware on a given operating system.

Python Version Support
----------------------

**nipcbatt** supports Python 3.9+ (64 bit)

Installation
============

You can use `pip <http://pypi.python.org/pypi/pip>`_ to download **nipcbatt** from
`PyPI <https://pypi.org/project/nipcbatt/>`_ and install it::

  $ python -m pip install nipcbatt==2.0.0


Getting Started
===============

In order to use the **nipcbatt package**, you must have at least one DAQ (`Data Acquisition <https://www.ni.com/en/shop/data-acquisition.html>`_)
device installed on your system. Both physical and simulated devices are supported. The examples below use PC 
based DAQ device (PCIe-6353). You can use NI MAX or NI Hardware 
Configuration Utility to verify and configure your devices.


Finding and configuring device name in **NI MAX**:

.. image:: https://raw.githubusercontent.com/ni/nipcbatt/main/src/nipcbatt/docs/images/NI-MAX%20Configuration.png
  :alt: NI-MAX
  :align: center
  :width: 800px

Finding and configuring device name in **NI Hardware Configuration Utility**:

.. image:: https://raw.githubusercontent.com/ni/nipcbatt/main/src/nipcbatt/docs/images/Hardware%20Configuration%20Utility.png
  :alt: Hardware Config 
  :align: center
  :width: 800px

Then refer to the Validation examples and Automation sequences to start testing. Refer to the Getting Started Guide for information.


Key Concepts in Python PCBATT
=============================

1. Libraries
-------------

All the measurement libraries consist of three main methods which have to be used in the following order:

- Initialize:
 
   Used to initialize a measurement instance (for DAQmx use either physical or global virtual channels to perform the respective task).

   This is done by calling the initialize() method on the class instance.

Example code to initialize an instance of DC RMS voltage measurement:

.. code-block:: python

  >>> from nipcbatt import dmm
  >>> dmm_voltage_measurement = dmm.DcRmsVoltageMeasurement()
  >>> dmm_voltage_measurement.initialize("Sim_DMM", 50)


- Configure and Generate/Configure and Measure:
 
   Configures and executes measurement or generation tasks. For measurements, 
   this method can return both raw data for custom analysis and processed results 
   from built-in analysis functions (configurable via measurement options).
 
   This is done by calling the
   configure_and_measure()/configure_and_generate() method on the class instance.

Example code to configure and measure DC voltage using the class instance:

.. code-block:: python

  >>> measurement = dmm_voltage_measurement.configure_and_measure(
  >>>   configuration=dmm.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION
  >>> )
  ... # Default voltage measurement configuration 


- Close:
 
   Closes the measurement or generation session and releases hardware resources.

   This is done by calling the close() method on the class instance.
  
Example code to close the session and clear resources:

.. code-block:: python

  >>> dmm_voltage_measurement.close()


1. Features and Utilities
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
The validation examples can be found in this location `pcbatt_validation_examples <https://github.com/ni/nipcbatt/tree/main/src/nipcbatt/pcbatt_validation_examples>`_.

The following images shows sample results for Signal Voltage Generation to Frequency Domain Voltage Measurement Validation example which
is located at *"/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_FDVM.py"*:

.. image:: https://raw.githubusercontent.com/ni/nipcbatt/main/src/nipcbatt/docs/images/SVG_to_FDVM_Results.png
  :alt: SVG_to_FDVM_Results
  :align: center
  :width: 600px

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

The Automation Sequences can be found in this location `pcbatt_automation <https://github.com/ni/nipcbatt/tree/main/src/nipcbatt/pcbatt_automation>`_.

 
3. Functional Test Demo Sequence
---------------------------------
 
FT demo sequence is an example for creating a test sequence using
libraries with applying test limits on the results to determine whether the test is a pass or a fail.

Please refer to the FT Demo Sequence in the location `pcbatt_ft_demo_test_sequence <https://github.com/ni/nipcbatt/tree/main/src/nipcbatt/pcbatt_ft_demo_test_sequence>`_.



Bugs / Feature Requests
=======================

To report a bug or submit a feature request, please use GitHub `Issues  <https://github.com/ni/nipcbatt/issues>`_.


License
========
**nipcbatt** is licensed under an MIT-style license. Other incorporated projects may be licensed under different licenses. All 
licenses allow for non-commercial and commercial use.

