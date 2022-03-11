#!/usr/bin/env python
"""
days_to_surge.py

Simulate the growth of Omicron BA.2 in the general population, going to the surge.

Print the results for key days.

Usage: python days_to_ten_percent.py [-h] [-o OUTPUT_FILENAME]
"""

import copy

# Current percentage of BA.2 to total COVID cases, used to calculate BA.2 cases
# On 3/8 it was 11.6%, 3/1 it was 6.6%, 2/22 it was 4%, 2/15 it was 2%, according to the CDC
BA2_PERCENT_OF_COVID_INITIAL = 11.6
# CDC is using 7 days to double, but some in HHS estimate as low as 1
DAYS_TO_DOUBLE = 7.0
# Stop simulation at this percentage of the general population
SURGE_PERCENT = 10.0
# Early March test positivity for Los Angeles is staying fairly steady at 1%
# Most tests are schools and employers, so it represents the general population fairly well
TEST_POSITIVITY_PERCENT_OVERALL = 1.0


def main():
    """
    Main entry point to run the simulation
    """
    # Using Python 2 prints
    print 'Starting Omicron BA.2 simulation. Doubling interval = ', DAYS_TO_DOUBLE, ' days'

    # Calculate the percentage of the whole population infected with BA.2
    ba2_percent_initial = TEST_POSITIVITY_PERCENT_OVERALL * (BA2_PERCENT_OF_COVID_INITIAL / 100.0)
    ba2_percent_current = copy.copy(ba2_percent_initial)

    day = 1
    print 'Day ', day, '   Percent positive: ', ba2_percent_current

    while ba2_percent_current < SURGE_PERCENT:
        day = day + DAYS_TO_DOUBLE
        ba2_percent_current = ba2_percent_current * 2
        print 'Day ', day, '   Percent positive: ', ba2_percent_current

    print 'Completed simulation'


if __name__ == '__main__':
    main()
