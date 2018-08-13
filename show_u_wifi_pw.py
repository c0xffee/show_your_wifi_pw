import os

def c0xffee():
  os.system('color b')
  c0xffee = '''

  
  
  

    :'######::::'#####:::'##::::'##:'########:'########:'########:'########:
    '##... ##::'##.. ##::. ##::'##:: ##.....:: ##.....:: ##.....:: ##.....::
     ##:::..::'##:::: ##::. ##'##::: ##::::::: ##::::::: ##::::::: ##:::::::
     ##::::::: ##:::: ##:::. ###:::: ######::: ######::: ######::: ######:::
     ##::::::: ##:::: ##::: ## ##::: ##...:::: ##...:::: ##...:::: ##...::::
     ##::: ##:. ##:: ##::: ##:. ##:: ##::::::: ##::::::: ##::::::: ##:::::::
    . ######:::. #####::: ##:::. ##: ##::::::: ##::::::: ########: ########:
    :......:::::.....::::..:::::..::..::::::::..::::::::........::........::
	
	
'''
  print(c0xffee)
  
def title():
  print('\n'*2)
  print('='*80)  
  print('='*33+'show_u_wifi_pw'+'='*33)
  print('='*80)  
  print('='*31+'powered_by_c0xffee'+'='*31)
  print('='*80)  
  print('\n'*2)
  

c0xffee()
title()
tmp = os.popen('netsh wlan show profiles').read().split()
ssids = []
for i in range(len(tmp)):
  if tmp[i] == ':':
    ssids.append(tmp[i+1])
	
pw = []
leng = 0
for ssid in ssids:
  if len(ssid) > leng:
    leng = len(ssid)
  
  tmp = os.popen('netsh wlan show profile %s key=clear'%ssid).read().split()
  if len(tmp) == 93:
    pw.append(tmp[72])
  else:
    pw.append(None)  
	

print('Results:\n')	


m = leng + 4

for i in range(len(ssids)):
  print('                        %s%s:    %s'%(ssids[i], ' '*(m-len(ssids[i])), pw[i]))

print('\n')
  


