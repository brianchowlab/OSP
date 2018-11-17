#!/bin/sh
pip install pyserial
pip install -U matplotlib
apt-get update
apt-get install python-cairo -y
apt-get install python-qt4 -y
pip install XlsxWriter
apt-get install git-all build-essential libusb-dev -y
pip install pyusb
cd python-seabreeze/misc
./install_libseabreeze.sh
./install_udev_rules.sh
cd ..
pip install . 