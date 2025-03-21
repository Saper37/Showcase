#! /bin/bash
echo ${1}
import_string="import ${1}"
echo ${import_string}
sudo python -c ${import_string}
echo $?

