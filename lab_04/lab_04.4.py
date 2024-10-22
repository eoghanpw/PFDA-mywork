# This code will find some text in an access log file.
# Author: Eoghan Walsh

import re

regex = "^\d+\.\d+\.\d+\.\d+"
filename = "smaller_access.log"

with open(filename) as input_file:
    for line in input_file:
        found_text_list = re.findall(regex, line)
        if len(found_text_list) != 0:
            found_text = found_text_list[0]
            print(found_text)
