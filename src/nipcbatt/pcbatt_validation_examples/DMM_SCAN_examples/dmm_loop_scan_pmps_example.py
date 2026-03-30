# pylint: disable=C0200, C0103, C0301

"""This example executes a DMM Scan in a loop 5 times with a 2 second
   delay between iterations. Each iteration scans 3 voltage and 3 current
   measurements and prints the results."""

import time

from nipcbatt import dmm
from nipcbatt import dmm_scan

############### DECLARE INPUT VALUES ########################################################

# edit this list to define the configurations to use during the scan
# each entry should be a list in the format below:
# [channel (int), range & function (MixedRangeAndFunctions), resolution (ResolutionInDigits)]
scan_configuration = [
    [1,  dmm.MixedRangeAndFunctions.DC_10V,               dmm.ResolutionInDigits.DIGITS_5_5],
    [2,  dmm.MixedRangeAndFunctions.DC_1V,                dmm.ResolutionInDigits.DIGITS_5_5],
    [3,  dmm.MixedRangeAndFunctions.DC_10V,               dmm.ResolutionInDigits.DIGITS_5_5],
    [16, dmm.MixedRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_5_5],
    [17, dmm.MixedRangeAndFunctions.DC_10mA,              dmm.ResolutionInDigits.DIGITS_5_5],
    [18, dmm.MixedRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_5_5]
]

#Declare constants for initialization
mux_resource_name = "Sim_MUX"
shunt_resource_name = "Sim_SHUNT"
dmm_resource_name = "Sim_DMM"

mux_topology_name = "2527/2-Wire Dual 16x1 Mux"
shunt_topology_name = "2568/31-SPST"

max_wait = 5000
powerline_freq = 50
close_all_shunts = True
verbose = True # Set to False to not print measurements to console
num_iterations = 5
delay_between_iterations = 2  # seconds

############ EXECUTE SCAN ####################################################################

# Create scan object
scan = dmm_scan.DmmScanPMPS()

# Initialize scan object
resources = scan.initialize(
    mux_resource_name,
    mux_topology_name,
    shunt_resource_name,
    shunt_topology_name,
    dmm_resource_name,
    powerline_freq,
    close_all_shunts
)

# Execute scan loop
for i in range(num_iterations):

    print(f"\n########################### ITERATION {i + 1} of {num_iterations} #######################################")

    # Execute full scan
    results = scan.configure_and_measure(resources, scan_configuration, close_all_shunts, verbose)

    # Wait before next iteration (skip delay after last iteration)
    if i < num_iterations - 1:
        print(f"Waiting {delay_between_iterations} seconds before next iteration...")
        time.sleep(delay_between_iterations)

# Disconnect and close resources
scan.close(resources)
