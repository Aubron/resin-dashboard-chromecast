import time
import subprocess
import pychromecast
import sys

# if no argument supplied, exit
try:
    if sys.argv[1]:
        print('[inputSwitch] Searching for Chromecast:')
        print(sys.argv[1])
        
except IndexError:
    print('[inputSwitch] No Chromecast name found. Remember to set your environment variables.')
    exit()
    


# get a list of chromecasts, find the one we're looking for
chromecasts = pychromecast.get_chromecasts()
chromecast = False

chromecast = next(cc for cc in chromecasts if cc.device.friendly_name == sys.argv[1])
if chromecast:
    print('[inputSwitch] Found Chromecast:')
    print(chromecast)
else:
    print("[inputSwitch] Couldn't find a Chromecast. Did you set your chromecast name env variable correctly?")
    exit()

#Checks to see if the Chromecast has been used, and when it finds it has, and no longer is, switches back to Dashboard.
has_watched = False
while True:
    time.sleep(5)
    if chromecast.status:
        if has_watched == False and chromecast.status.display_name != 'Backdrop':
            print('[inputSwitch] Chromecast in use, switcher primed.')
            has_watched = True
            
        if has_watched == True and chromecast.status.display_name == 'Backdrop':
            print('[inputSwitch] Chromecast no longer in use, attempting to switch back to the dashboard.')
            subprocess.run(['cec-client','-s','-d','1'],input=b'as')
            has_watched = False
    