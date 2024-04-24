#!/bin/sh

grep -P "\t\w*:" $1 | grep -v -i "equ" | sed -e 's/:/h/' -e 's/:.*$//g' -e 's/h [0-9]\+/h/g' -e 's/\t/ /g' | tr -s " "
