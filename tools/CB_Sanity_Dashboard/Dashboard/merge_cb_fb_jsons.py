"""
Author: Soumil R Kulkarni
"""

import time
import sys
from bs4 import BeautifulSoup
import ConfigParser
import paramiko
import os
import re
import subprocess
import urllib
from optparse import OptionParser
import json
import displaytemplate






def main():
        parser = OptionParser()
        parser.add_option('-c', '--cb_json', help='Json with cb info', type='string', dest='cb_json')
        parser.add_option('-f', '--fb_json', help='Json with fb info', dest='fb_json')
        parser.add_option('-o', '--out_json', help='Final output Json', type='string', dest='out_json')
        (opts, args) = parser.parse_args()
	cb_json=opts.cb_json
	fb_json=opts.fb_json
	out_json=opts.out_json

	cb_json_fh=open(cb_json,'r')
	fb_json_fh=open(fb_json,'r')
	
	out_json_fh=open(out_json,'w')

	a=json.loads(cb_json_fh)
	print a

	close(cb_json_fh)
	close(fb_json_fh)
	close(out_json_fh)


main()
