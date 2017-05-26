#!/bin/bash
echo "/usr/local/lib" >> /etc/ld.so.conf

cd /tmp
git clone https://github.com/Pulse-Eight/platform.git
mkdir platform/build
cd platform/build
cmake ..
make
make install
cd /tmp
git clone https://github.com/Pulse-Eight/libcec.git
mkdir libcec/build
cd libcec/build
cmake ..
make
make install
ldconfig

cd /

pip3 install pychromecast