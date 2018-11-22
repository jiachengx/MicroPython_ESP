#Author: Stephen Hsu

import pexpect
import time
import sys


print("Configure the MicroPython\n")
esp = pexpect.spawn('picocom /dev/ttyUSB{0} -b 115200'.format(sys.argv[1]))
time.sleep(1)
esp.sendline('\r\r')
time.sleep(1)
esp.sendline('import webrepl_setup\r')
time.sleep(1)
esp.sendline('E\r')
time.sleep(1)
esp.sendline('{your password}\r')
time.sleep(1)
esp.sendline('{your password}\r')
time.sleep(1)
esp.sendline('y\r')
time.sleep(1)
print("Finish to configure the MicroPython\n")
