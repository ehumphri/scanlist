Scanlist 
========

   I regularly end up with random text files with lots of different notations of networks, and ip ranges from customers. This script aims to make cleanup and validation of ip addresses quick and easy. 

# Prerequesites / Installation
```
   easy_install ipaddress
   copy the .py file to your system and run 
```
# Usage:

 ## View the usage output 
```
   shell$ python scanlist.py -h addresses.txt 
   scanlist.py -i <inputfile>
   shell$ 
```
 ## Select a file of addresses (included in the github repo for testing):
```
   shell$ python scanlist.py -i addresses.txt 

   valid ipv4 addresses
   192.168.0.1
   216.185.197.0
   216.185.197.1
   216.185.197.2
   216.185.197.3
   216.185.197.4
   216.185.197.5
   216.185.197.6
   216.185.197.7
   10.2.3.27
   172.16.1.23
   192.168.250.23
   8.0.0.0
   8.0.0.1
   8.0.0.2
   8.0.0.3
   10.2.2.5
   10.2.2.4
   10.2.2.3
   192.168.79.5
   192.168.79.4
   192.168.79.3
   192.168.79.2
   192.168.79.1
   192.168.79.0
   192.168.78.255
   192.168.78.254
   192.168.78.253

   valid ipv6 addresses
   2001:0DB8:AC10:FE01::
   2001:db8::1

   items that didn't validate:
   shell$
```
# Limitations

   if you have a network in a list, and the host listed isn't the network address, 
   it will not validate and it should be corrected.
   
   for example: 192.168.2.21/30 - the network address of the subnet is actually 
   192.168.2.20.
```
   shell$ whatmask 192.168.2.21/30

    ------------------------------------------------
               TCP/IP NETWORK INFORMATION
    ------------------------------------------------
    IP Entered = ..................: 192.168.2.21
    CIDR = ........................: /30
    Netmask = .....................: 255.255.255.252
    Netmask (hex) = ...............: 0xfffffffc
    Wildcard Bits = ...............: 0.0.0.3
    ------------------------------------------------
>>> Network Address = .............: 192.168.2.20 <<<---- see?
    Broadcast Address = ...........: 192.168.2.23
    Usable IP Addresses = .........: 2
    First Usable IP Address = .....: 192.168.2.21
    Last Usable IP Address = ......: 192.168.2.22
```

   probably many other limitations

# Tested Operating Systems

   OSX 10.9.1
