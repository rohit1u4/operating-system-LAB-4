#!/bin/bash
echo "----- System Information -----"

echo "Kernel Version:"
uname -r

echo "User:"
whoami

echo "Hardware Info:"
lscpu | grep "Virtualization"
