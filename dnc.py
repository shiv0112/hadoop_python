import os
ip=input("Enter the IP of the master node : ")

m=open("/root/core-site.xml","w")
m.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>""".format(ip))
m.close()

ip=input("Enter the IP of the slave node : ")
os.system("scp /root/core-site.xml root@{}:/etc/hadoop/core-site.xml".format(ip))
os.system("scp /root/hadoop_menu/dn.py root@{}:/root/dn.py".format(ip))
os.system("ssh root@{} python3 /root/dn.py".format(ip))
