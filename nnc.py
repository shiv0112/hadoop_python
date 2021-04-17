import os
ip=input("Enter the IP of the master node : ")
os.system("scp /root/hadoop_menu/nn.py root@{}:/root/nn.py".format(ip))
os.system("ssh root@{} python3 /root/nn.py".format(ip))
