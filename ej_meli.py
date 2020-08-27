__version__ = "1.3"

import json
import requests

import matplotlib.pyplot as plt
import matplotlib.axes

def ej_1():

    dataset = fetch()
    print(dataset)

    data = transform(dataset, 3000, 5000)
    print(data)

    
    report(data)

def fetch():
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'
    response = requests.get(url)
    json_response = response.json()
    results = [{"price": x.get("price", ""), "condition": x.get("condition", "")} for x in json_response["results"] if x.get("currency_id") == "ARS"]
    

    
    return results



def transform(dataset, min, max):

    min_count = [x for x in dataset if x.get("price") < min]
    min_max_count = [x for x in dataset if x.get("price") > min and x.get("price") < max]
    max_count = [x for x in dataset if x.get("price") > max]

    lista = [len(min_count), len(min_max_count), len(max_count)]
    return lista

def report(data):

    labels = ["min_count", "min_max_count", "max_count"]
   

    fig = plt.figure()
    fig.suptitle('ej 5', fontsize=16)
    ax = fig.add_subplot()

    

    ax.pie(data, labels=labels,
           autopct='%1.1f%%', shadow=True, startangle=90
           )
    
    ax.axis('equal')
    plt.show()




if __name__ == "__main__":

    ej_1()
   