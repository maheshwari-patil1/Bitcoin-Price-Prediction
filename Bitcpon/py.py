from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    api_url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/24h'
    response = requests.get(api_url)
    data = response.json()
    return render_template('index.html', data=data)

if __name__ == '__main__':
  
