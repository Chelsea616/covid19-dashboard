import urllib.request
ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
print(f"你的IP：{ip}")