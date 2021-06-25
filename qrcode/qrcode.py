import pyqrcode as pqr
import io
import png

url=pqr.create('http://localhost:8000/dados_planta/')
with open('qrcode.png', 'w') as fstream:
    url.png('qrcode.png',scale=5)
url.png('qrcode.png',scale=5)
buffer=io.BytesIO()
url.png(buffer)