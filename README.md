# Webscraper

This project consists of two parts. The second part is the server part, and you are viewing it now. The first part is the client part via a link in another repository https://github.com/CorbenYkt/webscraper-client

## Server side :computer:	
Flask
![image](https://github.com/CorbenYkt/webscraper-server/assets/117908636/f1de1dec-496a-4b8c-986f-126efd71f0b2)


The server part starts server on port 8080 and waits for incoming GET request. After that grads data (top last news) from www.lenta.ru and send's them to users if JSON format.
For webscrape the BeautifulSoup library is used.
```
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
```

Answer to users request:

```
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

```
