#!/usr/bin/python3

# This script get the rate of unknown unum for
# teammates and opponents.

import re
import time

outfile = f"/home/rcss2d/logs/unum/{time.time()}"
pattern = r"unknown_unum_teammates=(\d+)\s+unknown_unum_opponents=(\d+)"
teammates_total = 0
opponents_total = 0
num_matches = 0
for i in range(1, 12):
    filepath = f"/tmp/HELIOS_base-{i}.log"
    with open(filepath, "r") as file:
        for l in file:
            regex_match = re.search(pattern, l)
            if regex_match:
                num_matches += 1

                teammates = int(regex_match.group(1))
                opponents = int(regex_match.group(2))

                teammates_total += teammates
                opponents_total += opponents

                teammates_rate = teammates / 11
                opponents_rate = opponents / 11
                total_rate = (teammates + opponents) / 22

                with open(outfile, "a") as out:
                    out.write(f"{teammates_rate},{opponents_rate},{total_rate}\n")

    total_teammates_rate = teammates_total / (12 * num_matches)
    total_opponents_rate = opponents_total / (12 * num_matches)
    total_final_rate = (teammates_total + opponents_total) / (22 * num_matches)
    with open(outfile, "a") as out:
        out.write(f"Final Rates: {total_teammates_rate},{total_opponents_rate},{total_final_rate}\n")
 
