import requests

r = requests.get('https://httpbin.org/basic-auth/root/patriot', auth=('root', 'patriot'),
                 timeout=50)

print(r)