'''
Write a Python program to get the domain name using PTR
DNS records from a given IP address. 
Domain name using PTR DNS:
dns.google
ec2-13-251-106-90.ap-southeast-1.compute.amazonaws.com
dns.google
ec2-23-23-212-126.compute-1.amazonaws.com

'''

def get_domain_name(ip_address):
      import socket
      result=socket.gethostbyaddr(ip_address)
      return list(result)[0]

print("Domain name using PTR DNS:")
print(get_domain_name("8.8.8.8"))
print(get_domain_name("13.251.106.90"))
print(get_domain_name("8.8.4.4"))
print(get_domain_name("23.23.212.126"))
