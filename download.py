import os

dir = '/privapp/apk/it' 
apks = os.listdir(dir)
for apk in apks:
	os.system('python send.py 192.168.1.201 int_transfer testing {}/{}'.format(dir, apk))
