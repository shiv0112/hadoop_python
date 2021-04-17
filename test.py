import os
os.system("ls /root/hadoop-1.2.1-1.x86_64.rpm")
if os.system("echo $?")==0:
    pass
else:
    os.system("curl -O https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")

