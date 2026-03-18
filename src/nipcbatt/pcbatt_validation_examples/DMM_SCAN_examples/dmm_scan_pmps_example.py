# pylint: disable=C0200, C0103, C0301

"""This example executes a DMM Scan to obtain 3 voltage, 3 current,
   and one resistance measurement. It returns both the formatted and
   the raw measurements."""

from nipcbatt import dmm
from nipcbatt import dmm_scan

############### DECLARE INPUT VALUES ########################################################

# edit this list to define the configurations to use during the scan
# each entry should be a list in the format below:
# [channel (int), range & function (<type>RangeAndFunctions), resolution (ResolutionInDigits)]
scan_configuration = [
    [0,  dmm.VoltageRangeAndFunctions.DC_100mV,             dmm.ResolutionInDigits.DIGITS_6_5],
    [1,  dmm.VoltageRangeAndFunctions.DC_1V,                dmm.ResolutionInDigits.DIGITS_5_5],
    [2,  dmm.VoltageRangeAndFunctions.AC_2V,                dmm.ResolutionInDigits.DIGITS_4_5],
    [3,  dmm.ResistanceRangeAndFunctions.TWO_W_RES_10k_Ohm, dmm.ResolutionInDigits.DIGITS_4_5],
    [16, dmm.CurrentRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_6_5],
    [17, dmm.CurrentRangeAndFunctions.DC_10mA,              dmm.ResolutionInDigits.DIGITS_5_5],
    [18, dmm.CurrentRangeAndFunctions.AC_10mA,              dmm.ResolutionInDigits.DIGITS_4_5]
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

# Execute scan
results = scan.configure_and_measure(resources, scan_configuration, close_all_shunts, verbose)

# Disconnect and close resources
scan.close(resources)
