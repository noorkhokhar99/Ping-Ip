import ipaddress
import sh as pbs


user_input = raw_input("")

network = ipaddress.ip_network(unicode(user_input))

for i in network.hosts():
	try:
		sh.ping(1,"-c 1")
		print(i, "is active")
	except sh.ErrorReturnCode_1:
		print("no response from",i)