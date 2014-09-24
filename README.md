UrNet
=====

UrLab's Virtual Private Network

## Install

Clone this repository as /etc/tinc/urnet

`sudo git clone https://github.com/UrLab/urnet.git /etc/tinc/urnet`

## Your setup

Choose a free IP number (the X in 10.131.0.X). The script below will show you currently used IP addresses:
`/etc/tinc/urnet/tools/hosts.py`

Two solutions next: run the setup script or create your files by hand.

### Setup script

Run:
`sudo /etc/tinc/urnet/tools/new_user.py`

Then follow the instructions to enter your `name` and your `IP number` (X in 10.131.0.X).

### Setup by hand

```
cp /etc/tinc/urnet/tinc.conf.example /etc/tinc/urnet/tinc.conf
nano /etc/tinc/urnet/tinc.conf  # CHANGE THE NAME
cp /etc/tinc/urnet/tinc-up.example /etc/tinc/urnet/tinc-up
nano /etc/tinc/urnet/tinc-up  # CHANGE THE IP

cp /etc/tinc/urnet/hosts/okso /etc/tinc/urnet/$YOURNAME
nano /etc/tinc/urnet/hosts/$YOURNAME  # CHANGE THE IP
```
