import requests
import re

def obtener_url():
    url_web = "https://colorvision.com.do"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        r = requests.get(url_web, headers=headers)
        # Busca la URL que termina en .m3u8 y tiene parámetros (el token)
        match = re.search(r'https?://[^\s"\'<>]+index\.m3u8\?[^\s"\'<>]+', r.text)
        if match:
            return match.group(0)
    except:
        pass
    return None

nueva_url = obtener_url()
if nueva_url:
    with open("lista.m3u", "w") as f:
        f.write("#EXTM3U\n")
        f.write("#EXTINF:-1 tvg-logo=\"https://colorvision.com.do\", Color Vision Canal 9\n")
        f.write(nueva_url)
