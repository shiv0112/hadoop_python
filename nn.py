import os
import subprocess
os.system("clear")

os.system("ls /root/jdk-8u171-linux-x64.rpm")
if os.system("echo $?")==0:
    pass
else:
    print("\n\n\n\t\tInstalling jdk")
    os.system("curl -O http://35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm")

os.system("ls /root/hadoop-1.2.1-1.x86_64.rpm")
if os.system("echo $?")==0:
    pass
else:
    print("\n\n\n\t\tInstalling hadoop")
    os.system("curl -O https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")

os.system("rpm -q jdk1.8")
if os.system("echo $?")==0:
    pass
else:
    print("\n\n\n\t\tInstalling JDK\n\n\n")
    os.system("rpm -ivh jdk-8u171-linux-x64.rpm")

os.system("rpm -q hadoop")
if os.system("echo $?")==0:
    pass
else:
    print("\n\n\t\t Installing Hadoop\n\n")
    os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")

os.system("rm -rf /name")
os.system("mkdir /name")

m=open("/etc/hadoop/hdfs-site.xml","w")
m.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/name</value>
</property>
</configuration>""")
m.close()

ip=subprocess.getoutput("hostname -I | awk '{print $1}'")

m=open("/etc/hadoop/core-site.xml","w")
m.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://"""+(str)(ip)+""":9001</value>
</property>
</configuration>""")
m.close()

os.system("systemctl stop firewalld")
os.system("echo 'Y' | hadoop namenode -format")
os.system("hadoop-daemon.sh start namenode")
os.system("jps")
os.system("hadoop dfsadmin -report")

