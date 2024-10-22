# This code anonymizes the sub domains of ip addresses
# Author: Eoghan Walsh

import re

regex = "(^\d+\.\d+\.)\d+\.\d+"
replacement_text = "\\1XXX.XXX"
filename = "smaller_access.log"
output_filename = "anonymized_ip.txt"

with open(filename) as input_file:
    with open(output_filename, 'w') as output_file:
        for line in input_file:
            new_line = re.sub(regex, replacement_text, line)
            output_file.write(new_line)
