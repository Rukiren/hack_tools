import requests

base_url = "https://xxx.com"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": "ASP.NET_SessionId= "
}

for i in range(10000):
    page = f"WEB{i:04d}.aspx"
    url = f"{base_url}/{page}"

    try:
        r = requests.get(url, headers=headers, timeout=5, allow_redirects=True)

        # 確認最後的實際 URL 沒有被 redirect 到 /ErrorPage.htm
        if r.status_code == 200 and "網頁開啟錯誤" not in r.text and "ErrorPage.htm" not in r.url:
            print(f"[200] {url}")

    except requests.RequestException:
        continue
