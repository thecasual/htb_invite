import requests
import base64

url = 'https://www.hackthebox.eu/api/invite/generate'

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "not python",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
r = requests.post(url, headers=headers)

code = r.json()['data']['code']
decoded = base64.b64decode(code)

print(f'Invite code: {decoded.decode("utf-8")}')