from urllib.request import urlopen

url = urlopen('https://api.ipify.org')
ip = str(url.read())
print('public ip: ', ip[1:])
