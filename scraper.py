import requests
from bs4 import BeautifulSoup

# Örnek bir ürün linki (Burayı kendi takip edeceğin ürünle değiştir)
url = "https://www.hepsiburada.com/logitech-g-pro-x-superlight-kablosuz-oyuncu-mouse-siyah-p-HBCV000001JR65"

# Bazı siteler bot olduğumuzu anlar, bu yüzden header ekliyoruz
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# DİKKAT: Buradaki 'span' ve 'id' kısmı sitenin tasarımına göre değişir!
# Hepsiburada veya Trendyol'da bu kodları "İncele" (Inspect) diyerek bulman lazım.
price = soup.find("span", {"data-test-id": "price-current-price"}).get_text()

print(f"Güncel Fiyat: {price}")
