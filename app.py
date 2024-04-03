from flask import Flask

# Flask uygulamasını oluştur
app = Flask(__name__)

# Kök dizin için bir route tanımla
@app.route('/')
def hello():
    return 'Merhaba, Flask ile ilk uygulamama hoş geldiniz!'

# Uygulamayı çalıştır
if __name__ == '__main__':
    app.run(debug=True)
