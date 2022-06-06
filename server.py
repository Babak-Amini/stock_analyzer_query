from audioop import cross
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def home():
    return 'OK'

df = []

@app.route('/getSpy')
@cross_origin()
def getSpy():
    global df
    url = 'https://www.slickcharts.com/sp500'
    request = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs(request.text, "lxml")
    stats = soup.find('table',class_='table table-hover table-borderless table-sm')
    df = pd.read_html(str(stats))[0]
    
    sp_df = df[['#', 'Company', 'Symbol', 'Price', 'Weight']]
    sp_dict = sp_df.to_dict(orient='records')
    return jsonify(sp_dict)

@app.route('/getStock')
@cross_origin()
def getStocks():
    # input = request.args.get('input')
    # global df

    # if df == []:
    #     getSpy()

    # stockList = []

    # for index, row in df.iterrows() :
    #     try:
    #         if row
    #         index = row['Symbol'].index(input)
    #     except:
    #         continue
        
    #     print(index)

    return 'HELLO'


if __name__ == "__main__":
    app.run(debug=True)