import requests
import threading
from lib.helper.helper import *
from lib.helper.Log import *
from colorama import Fore, Back, Style


print(
        Fore.RED +
         """
                                                                                 
_______                _______                                             .---. 
\  ___ `'.             \  ___ `'.         __.....__   .----.     .----..--.|   | 
 ' |--.\  \             ' |--.\  \    .-''         '.  \    \   /    / |__||   | 
 | |    \  '            | |    \  '  /     .-''"'-.  `. '   '. /'   /  .--.|   | 
 | |     |  '           | |     |  '/     /________\   \|    |'    /   |  ||   | 
 | |     |  |.--------. | |     |  ||                  ||    ||    |   |  ||   | 
 | |     ' .'|____    | | |     ' .'\    .-------------''.   `'   .'   |  ||   | 
 | |___.' /'     /   /  | |___.' /'  \    '-.____...---. \        /    |  ||   | 
/_______.'/    .'   /  /_______.'/    `.             .'   \      /     |__||   | 
\_______|/    /    /___\_______|/       `''-...... -'      '----'          '---' 
             |         |                                                         
             |_________|                                                         
                                          [ twitter.com/devilcombo ]
                                          [ facebook: Belhadj Hussein ]
        """ + Fore.RESET)
Log.info("Starting PwnXSS...")
Log.info("Please Enter Target Url")
url = input
payload = "<script>alert(123);</script>"
req=requests.get(url+payload,"html.parser").text;
print(url+payload)
if payload in req:
Log.high("Detected XSS (POST) at "+url)
else:
    print(Fore.RED + 'XSS Not Found' + Fore.RESET)
