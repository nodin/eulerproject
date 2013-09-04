import subprocess
from subprocess import Popen
from subprocess import *
import os
import time

cmd = "/home/nodin/opt/OracleSQLHandler/start-OracleSQLHandler.sh"

print time.time()

sub2 = subprocess.Popen(cmd,shell=True)
print sub2
while 1:
    ret1 = subprocess.Popen.poll(sub2)
    if ret1 == 0:
        print sub2.pid,'end'
        sub2 = subprocess.Popen(cmd,shell=True)
    elif ret1 is None:
        print 'running'
        time.sleep(1)

    else:
        print sub2.pid,'term'
print time.time()
