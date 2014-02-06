#
# scanlist - this utility cleans up a text file of random IP addresses, subnets, or network ranges
# feb 6, 2014 - Eric Humphries (eric.humphries@netspi.com)
#

import ipaddress
from array import *
import re

def expandrange( range ):  #-------------------------------------
 netstart = unicode(range.split('-')[0].rstrip())
 netstop = unicode(range.split('-')[1].rstrip())

 number = int(ipaddress.IPv4Address(netstop.rstrip())) - int(ipaddress.IPv4Address(netstart.rstrip()))

 counter = 0 

 while counter <= number:
  rangeaddress = ipaddress.ip_address(netstop) - counter 
  validateip(rangeaddress)
  counter=counter+1

def expandnetwork( network ): #-------------------------------------------
 try:
  ipaddress.IPv4Network(network.rstrip())
 except Exception,e:
  invalid.append(network.rstrip())
 else:
  for host in ipaddress.IPv4Network(network.rstrip()):
	validateip(host)

def validateip( line ): #--------------------------------------------
 ip = unicode(line)
 try:
  ipaddress.ip_address(ip)
  private = str(ipaddress.ip_address(ip).is_private)
  version = str(ipaddress.ip_address(ip).version)
 except Exception,e:
  #invalid.append(ip)
  expandnetwork(ip);
 else:
  if version == '4':
   validv4.append(ip)
  elif version == '6':
   validv6.append(ip)
  else:
   invalid.append(ip)

# create arrays that are going to store our ipaddresses
validv4 = []
validv6 = []
invalid = [] 

# main()

f = open('test.txt')

for line in f:
	match = re.search('-',line)
	if match:
		expandrange(line)
	else:
		validateip(line.rstrip());

f.close()

print "\nvalid ipv4 addresses"

for a in validv4:
	print a

print "\nvalid ipv6 addresses"

for b in validv6:
	print b

print "\nitems that didn't validate:"

for c in invalid:
	print c

