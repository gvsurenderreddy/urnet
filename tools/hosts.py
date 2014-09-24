#!/bin/env python3

from __future__ import print_function

import re
import glob

for filename in glob.glob('/etc/tinc/urnet/hosts/*'):
    content = open(filename).readlines()
    for line in content:
        match_ip = re.findall(r'Subnet\s*=\s*(\d+\.\d+\.\d+\.\d+)\/?\d*$', line)
        if match_ip:
            match = match_ip[0]
            hostname = filename.split('/')[-1]
            print(match, hostname)
