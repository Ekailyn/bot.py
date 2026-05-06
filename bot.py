from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app) # Flutter'ın bağlanabilmesi için şart

class MarketBotu:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def migros_ara(self, urun):
        # Gerçek Migros çekme kodların buraya gelecek
        return [{"ad": f"{urun} - Migros", "fiyat": "45.00 TL", "market": "Migros", "resim": "https://picsum.photos/200"}]

    def a101_ara(self, urun):
        # Gerçek A101 çekme kodların buraya gelecek
        return [{"ad": f"{urun} - A101", "fiyat": "42.50 TL", "market": "A101", "resim": "https://picsum.photos/201"}]

@app.route('/ara')
def ara():
    sorgu = request.args.get('q')
    bot = MarketBotu()
    # Oda oda gezme başlıyor:
    sonuclar = bot.migros_ara(sorgu) + bot.a101_ara(sorgu)
    return jsonify(sonuclar)

if __name__ == '__main__':
    # host='0.0.0.0' demek "tüm ağdan gelen isteklere cevap ver" demektir
    app.run(host='0.0.0.0', port=5000, debug=True)