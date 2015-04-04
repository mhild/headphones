import struct, socket, sys, time, os
from urlparse import urlparse

#Test Connection function
def testCon(host):
        o = urlparse(host)
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((o.hostname, o.port))
            return "Up"
            s.close()
        except socket.error, e:
            return "Down"

#Wake function
def wakeOnLan(ethernet_address):

        addr_byte = ethernet_address.split(':')
        hw_addr = struct.pack('BBBBBB', int(addr_byte[0], 16),
        int(addr_byte[1], 16),
        int(addr_byte[2], 16),
        int(addr_byte[3], 16),
        int(addr_byte[4], 16),
        int(addr_byte[5], 16))
                     
        # Build the Wake-On-LAN "Magic Packet"...
                        
        msg = '\xff' * 6 + hw_addr * 16
                           
        # ...and send it to the broadcast address using UDP
                              
        ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ss.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        ss.sendto(msg, ('<broadcast>', 9))
        ss.close()
        
def wakeHost(mac, host, retries, timeout):
    
        i = 0
        while testCon(host) == "Down" and i < retries:
            wakeOnLan(mac)    
            time.sleep(timeout)
            i = i + 1
            
        
