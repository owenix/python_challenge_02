#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

in_file = open('junk.txt')

in_string = (in_file.read())

print(in_string)

for in_s in in_string:
	print(re.findall('[a-z]', in_string))
