#!/bin/bash

apkName=$1
OutPut=$apkName'_output'

echo -e "\e[31m\n\n  
                * لا تقول لي وش استفيد منها عشان مانتحر هههه
		* 0xSaudiAPK v2 
		* Telegram: https://t.me/x0Saudi
		* Twitter:  https://twitter.com/Dmaral3noz
		* Saud Alenazi    
	\033[0;37m"
sleep 5
apk_decode(){
echo -e "\n\e[34m###########[APK Decompile $apkName]###########\e[0m\n"
apktool d $apkName -o $OutPut
}
apk_decode
url_filter(){
echo -e "\n\e[34m###########[Extract URL from =>  $apkName]###########\e[0m\n"
grep -Pharo "(http|https)://[a-zA-Z0-9./?=_-]*" $OutPut/  | sed 's#"##g'  | uniq |grep -v "w3\|android\|github\|http://schemas.android\|google\|http://goo.gl"
}
url_filter
phone_number(){
echo -e "\n\e[34m###########[Extract PhoneNumber from =>  $apkName]###########\e[0m\n"
grep -Pharo "^(009665|9665|\+9665|05|5)(5|0|3|6|4|9|1|8|7)([0-9]{7})$" $OutPut/
}
phone_number
email_filter(){
echo -e "\n\e[34m###########[Extract EMAIL from =>  $apkName]###########\e[0m\n\n"
grep -Pharo "[A-Za-z0-9][A-Za-z0-9._%+-]+@[A-Za-z0-9][A-Za-z0-9.-]+\.[A-Za-z]{2,6}"  $OutPut/
}
email_filter
Key_filter(){
echo -e "\n\e[34m###########[Extract Google API Key and Oauth from =>  $apkName]###########\e[0m\n\n"
grep -Pharo "AIza[0-9A-Za-z\\-_]{35}"  $OutPut/
grep -Pharo "[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com"  $OutPut/
}
Key_filter
AWS_filter(){
echo -e "\n\e[34m###########[Extract AWS =>  $apkName]###########\e[0m\n\n"
grep -Pharo "amzn\.mws\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"  $OutPut/
grep -Pharo "([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}"  $OutPut/
grep -Pharo "AKIA[0-9A-Z]{16}"  $OutPut/
grep -Pharo "[a-z0-9.-]+\\.s3\\.amazonaws\\.com"  $OutPut/
grep -Pharo "[a-z0-9.-]+\\.s3-[a-z0-9-]\\.amazonaws\\.com"  $OutPut/
grep -Pharo "[a-z0-9.-]+\\.s3-website[.-](eu|ap|us|ca|sa|cn)"  $OutPut/
grep -Pharo "//s3\\.amazonaws\\.com/[a-z0-9._-]+"  $OutPut/
grep -Pharo "//s3-[a-z0-9-]+\\.amazonaws\\.com/[a-z0-9._-]+"  $OutPut/
grep -Pharo "amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"  $OutPut/
}
AWS_filter
Firebase_filter(){
echo -e "\n\e[34m###########[Extract Firebase =>  $apkName]###########\e[0m\n\n"
grep -Pharo "[a-z0-9.-]+\.firebaseio\.com"  $OutPut/
}
Firebase_filter
