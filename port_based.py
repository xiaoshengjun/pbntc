"""
Port-based network traffic classification
contact: chenjj@mail.buct.edu.cn
Let you fly!!!!
"""



def create_port_db():
	"""
	Parameters
    ----------

    Returns
    -------
    port dict 

	"""

	port = {}
	f = open("./PortDB","r")
	line = f.readline()

	while line:
		if line.find("group")==0:
			group = line[6:].replace("\n","").replace(" ","")
			sport = f.readline().split(':')[1].replace(" ","").replace("\n","")
			dport = f.readline().split(':')[1].replace(" ","").replace("\n","")
			for sp in sport.split(','):
				for dp in dport.split(','):
					#deal with abbreviated form e.g. 1-100
					if "-" in sp:
						sp_min = int(sp.split("-")[0])
						sp_max = int(sp.split("-")[1])
						if "-" in dp:
							dp_min = int(dp.split("-")[0])
							dp_max = int(dp.split("-")[1])
							for n_sp in range(sp_min,sp_max+1):
								for n_dp in range(dp_min,dp_max+1):
									key = str(n_sp)+"|"+str(n_dp)
									port[key] = group
						else:
							for n_sp in range(sp_min,sp_max+1):
								key = str(n_sp)+"|"+dp
								port[key] = group
					else:
						if "-" in dp:
							dp_min = int(dp.split("-")[0])
							dp_max = int(dp.split("-")[1])
							for n_dp in range(dp_min,dp_max+1):
								key = sp+"|"+str(n_dp)
								port[key] = group
						else:
							key = sp+"|"+dp
							port[key] = group
		line = f.readline()
	f.close()

	return port

def classify(t_sport,t_dport,port):
	"""
	Port-based classification

	Parameters
    ----------
    sport
    dport

    Returns
    -------
    application's group

	"""
	if port.has_key(t_sport+"|"+t_dport):
		print port.get(t_sport+"|"+t_dport)
	elif port.has_key(t_dport+"|"+t_sport):
		print port.get(t_dport+"|"+t_sport)
	elif port.has_key(t_sport+"|*"):
		print port.get(t_sport+"|*")
	elif port.has_key("*|"+t_sport):
		print port.get("*|"+t_sport)
	elif port.has_key("*|"+t_dport):
		print port.get("*|"+t_dport)
	elif port.has_key(t_dport+"|*"):
		print port.get(t_dport+"|*")
	else:
		print "Unknown"

if __name__ == '__main__':
	print "Let you fly!!!!"

	
	"""
	Example:

	traffic_file = open("l1.txt","r")
	lines = traffic_file.readlines()

	i = 1
	for line in lines:
		print i,"\t",
		sd_port = line.split(" ")[3:5]
		t_sport = sd_port[0]
		t_dport = sd_port[1]
		port = create_port_db()
		classify(t_sport,t_dport,port)
		i += 1
	"""



