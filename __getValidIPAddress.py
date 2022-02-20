'''
Python program to check if an IP address is valid or not
'''
import socket
import re

#Sample Solution-1:
def checkValidIPOptionOne ():
    #addr = '127.0.0.2561'
    addr =  '10.0.0.0'
    try:
        socket.inet_aton(addr)
        print("Valid IP")
    except socket.error:
        print("Invalid IP")
    
#Sample Solution-2:
def checkValidIPOptionTwo ():
    
    ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    user_ip = "10.0.0.0"
    print("\n",user_ip,"->",check_ip_address(user_ip, ip_regex))
    user_ip = "10.255.255.255"
    print("\n",user_ip,"->",check_ip_address(user_ip, ip_regex))
    user_ip = "192.168.255.0"
    print("\n",user_ip,"->",check_ip_address(user_ip, ip_regex))
    user_ip = "266.1.0.2"
    print("\n",user_ip,"->",check_ip_address(user_ip, ip_regex))
    user_ip = "01.102.103.104"
    print("\n",user_ip,"->",check_ip_address(user_ip,ip_regex))

def check_ip_address(user_ip, ip_regex):
   if(re.search(ip_regex, user_ip)):
       return "Valid Ip address"        
   else:
       return "Invalid Ip address"

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : checkValidIPOptionOne,
                  2 : checkValidIPOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()


