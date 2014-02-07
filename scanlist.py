#
# scanlist - this utility cleans up a text file of random IP addresses, subnets, or network ranges
# feb 6, 2014 - Eric Humphries (eric.humphries@netspi.com)
#

import ipaddress
from array import *
import re
import sys, getopt

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
 #print "potential network caught " + network
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
  # assume that if it isn't a valid IP, that it's a network
  expandnetwork(ip);
 else:
  if version == '4':
   validv4.append(ip)
  elif version == '6':
   validv6.append(ip)
  else:
   invalid.append(ip)

def main(argv): #-------------------------------------

  inputfile = ''

  try:
   opts, args = getopt.getopt(argv,"hi:",["ifile="])
  except getopt.GetoptError:
   print 'scanlist.py -i <inputfile>'
   sys.exit(2)
  for opt, arg in opts:
   if opt == '-h':
    print 'scanlist.py -i <inputfile>'
    sys.exit()
   elif opt in ("-i", "--ifile"):
    inputfile = arg

  return inputfile

if __name__ == "__main__":
   filename = main(sys.argv[1:])
  

# create arrays that are going to store our ipaddresses
validv4 = []
validv6 = []
invalid = [] 

# main()

f = open(filename)

for line in f:
	match = re.search('-',line)
	if match:
		expandrange(line)
	else:
		validateip(line.rstrip());

f.close()

if len(validv4) > 0:
 print "\nValid ipv4 addresses"

 for a in validv4:
	print a

if len(validv6) > 0:
 print "\nValid ipv6 addresses"

 for b in validv6:
	print b

if len(invalid) > 0:
 print "\nItems that didn't validate:"
 print "note: if the network doesn't start with the network address, it will not validate. "

 for c in invalid:
	print c

