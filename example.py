import port_based as pb

traffic_file = open("l1.txt","r")
lines = traffic_file.readlines()

port = pb.create_port_db()
i = 1
for line in lines:
	print i,"\t",
	sd_port = line.split(" ")[3:5]
	t_sport = sd_port[0]
	t_dport = sd_port[1]
	pb.classify(t_sport,t_dport,port)
	i += 1