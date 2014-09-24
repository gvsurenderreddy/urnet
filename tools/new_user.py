#!/usr/bin/env python3

import os
import sys

# Python2 compatibility
try:
    input = raw_input
except NameError:
    pass


if len(sys.argv) > 1:
    name = sys.argv[1]
    print('name =', name)
else:
    name = input('name: ').strip()

ip_number = int(input('IP number (0-255): '))

open('/etc/tinc/urnet/tinc.conf', 'w').write(
'''Name = {}
AddressFamily = ipv4
Interface = tun0
ConnectTo = oksoserver
'''.format(name))

open('/etc/tinc/urnet/hosts/{}'.format(name), 'w').write(
'''Subnet = 10.131.0.{}/32
'''.format(ip_number))

os.system('tincd -n urnet -K4096')

open('/etc/tinc/urnet/tinc-up', 'w').write(
'''ifconfig $INTERFACE 10.131.0.{} netmask 255.255.255.0
'''.format(ip_number))

