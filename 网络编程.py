#import requests
#
#
#resp = requests.get('https://www.python.org/index.html')
#staus = resp.status_code
#
#print(resp.headers)
#print(resp.cookies)
#
import requests

response = requests.get('http://httpbin.org/get?name=Dave&n=37',headers={"User-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'})


print(response.json())
