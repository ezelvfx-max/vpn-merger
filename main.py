import base64
import urllib.request

# Укажите здесь ваши ссылки на VPN-подписки или отдельные ключи (vless://, vmess:// и т.д.)
SOURCES = [
    "vless://d9d0f208-d582-41d5-bb7b-742671402810@185.255.179.11:9443?encryption=none&security=tls&sni=hub-de-05.hanvpn.cc&fp=firefox&type=ws&host=hub-de-05.hanvpn.cc&path=%2Fde05-ws-8e47a#%F0%9F%87%A9%F0%9F%87%AA%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F%20%5BBL%5D",
    "vless://d9d0f208-d582-41d5-bb7b-742671402810@185.255.179.11:9443?encryption=none&security=tls&sni=hub-de-05.hanvpn.cc&fp=firefox&type=grpc&mode=gun&authority=&serviceName=de05-grpc-8e47a#%F0%9F%87%A9%F0%9F%87%AA%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F%20%5BBL%5D",
    "vless://4054fdc2-ee80-4419-8a8e-d937df4719e2@qq.utiltools.site:443?flow=xtls-rprx-vision&encryption=none&security=reality&sni=qq.utiltools.site&fp=qq&pbk=drY21DHNOr6ezJLA2B10mzTExeJ9-gVBfTBNLwVBtWI&type=tcp&headerType=none#%F0%9F%91%89%D0%A2%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC%20%F0%9F%87%B7%F0%9F%87%BA",
    "vless://f4ba862a-4d64-431a-9213-dd7aaafd476a@94.183.209.33:8443?encryption=none&security=reality&sni=timeline.www.cloudflare.com&fp=firefox&pbk=S_13TsXuoNyvkx6uf7JHJeuPX3G-nmSRMzn_hgcF3mk&sid=bafa6f22a3&spx=%2Fzsncv2tq91fyune&type=tcp&headerType=none#%F0%9F%87%B5%F0%9F%87%B1%20%D0%9F%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%20%E2%80%94%20Wyszk%C3%B3w",
    "vless://cd3bb7d9-7df3-4644-ac05-c260990ac277@66.90.105.210:2083?encryption=none&security=none&type=grpc&mode=gun&authority=&serviceName=vless#tg%3AVLESSFORU%20%F0%9F%87%AC%F0%9F%87%A7%20%E2%9A%A1",
    "vless://f4ba862a-4d64-431a-9213-dd7aaafd476a@94.183.209.33:8443?encryption=none&security=reality&sni=timeline.www.cloudflare.com&fp=firefox&pbk=S_13TsXuoNyvkx6uf7JHJeuPX3G-nmSRMzn_hgcF3mk&sid=bafa6f22a3&type=tcp&headerType=none#%F0%9F%87%B5%F0%9F%87%B1%20%D0%9F%D0%BE%D0%BB%D1%8C%D1%88%D0%B0",
    "vless://cd3bb7d9-7df3-4644-ac05-c260990ac277@66.90.105.210:2083?encryption=none&security=none&type=grpc&mode=gun&authority=&serviceName=vless#%F0%9F%87%AC%F0%9F%87%A7%20%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%BE%D0%B1%D1%80%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D1%8F",
    "vless://5dec24d0-89b5-457a-81fd-7992e4c09e30@198.105.123.26:8443?security=reality&encryption=none&pbk=fiE-KoxoQgOIuvm1EuBTeZp9TFZLq9FYbZPrcWes-GM&headerType=none&fp=firefox&type=tcp&flow=xtls-rprx-vision&sni=slfs3.ardor-cloud.ru&sid=ba86aaa222fa2ee1#%F0%9F%87%B9%F0%9F%87%B7%E2%9A%A1%EF%B8%8F%20%D0%A2%D1%83%D1%80%D1%86%D0%B8%D1%8F", 
]

def fetch_and_decode(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8').strip()
            # Пробуем декодировать Base64, если подписка закодирована
            try:
                decoded = base64.b64decode(content).decode('utf-8')
                return decoded.splitlines()
            except Exception:
                return content.splitlines()
    except Exception as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return []

def main():
    all_configs = []
    for source in SOURCES:
        lines = fetch_and_decode(source)
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                all_configs.append(line)

    # Удаляем дубликаты
    unique_configs = list(dict.fromkeys(all_configs))
    
    # Объединяем и кодируем в Base64
    combined_text = "\n".join(unique_configs)
    encoded_result = base64.b64encode(combined_text.encode('utf-8')).decode('utf-8')

    # Сохраняем в index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(encoded_result)

if __name__ == "__main__":
    main()
