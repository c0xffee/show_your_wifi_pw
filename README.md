# show_your_wifi_pw
  this program can show your wifi passwords on windows OS.   
  
  the key command:                           
  
        >netsh wlan show profiles
           // this command show you the connected SSID
        >netsh wlan show profile [SSID] key=clear
           // then, put the SSID in this command will show you password
                  
# how_it_work
  it use [netsh wlan show profiles] get your device all connected wifi SSIDs.  
  
  than, put the SSIDs from last command in [netsh wlan show profile [SSID] key=clear] to get passwords.        
  
  finally, show you the results from your screen.                

