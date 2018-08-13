import os

tmp = os.popen('netsh wlan show profiles').read().split()
ssids = []
for i in range(len(tmp)):
  if tmp[i] == ':':
    ssids.append(tmp[i+1])
	
pw = []
for ssid in ssids:
  tmp = os.popen('netsh wlan show profile %s key=clear'%ssid).read().split()
  if len(tmp) == 93:
    pw.append(tmp[72])
  else:
    pw.append(None)  
	
	
print('\n')	
print(ssids)
print(pw)

for i in range(len(ssids)):
  print('%s:%s'%(ssids[i], pw[i]))

  


