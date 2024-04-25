from flask import Flask, jsonify
from flask_cors import CORS

app=Flask(__name__)
cors=CORS(app, origins='*')

@app.route("/api/lentaru", methods=['GET'])

def lentaru():
    import requests
    import json
    from bs4 import BeautifulSoup 
    # Making a GET request 
    r = requests.get('https://www.lenta.ru') 

    # Making a GET request
    soup = BeautifulSoup(r.content, 'html.parser') 
    
    textdata = soup.find('div', class_='last24__body _main js-tabs-body _active') 
    textcontent = textdata.find_all('div', class_='card-mini__text')
    imgcontent = textdata.find_all('div', class_='card-mini__image-wrap')
    
    # #print(content)
    texts = []
    pictures = []
    overall = {}

    #Here goes only text content
    print('#Here goes only text content')
    for line in textcontent:
        texts.append(line.text)

    #Here goes only image content
    print('#Here goes only image content')
    for line in imgcontent:
        justimage = line.find_all('img', class_='card-mini__image')
        for image in justimage:
            pictures.append(image['src'])

    #Gathering all together in JSON
    for i in range(len(pictures)):
        overall[pictures[i]] = texts[i]

    print(overall)

    return jsonify(
        {
            "lentaru": 
                overall
        }
        )

if __name__=="__main__":
    app.run(debug=True, port=8080)