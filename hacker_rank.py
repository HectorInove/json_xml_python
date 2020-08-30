__version__ = "1.3"

import json
import requests


def h_r():

    dataset = fetch(4, 1)
    print(dataset)

    data = transform(dataset)

    print(data)

def fetch(page_number, location_id):
    
    url = "https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page={}".format(page_number)
    response = requests.get(url)
    json_response = response.json()
  
    filtering_data = [{"userId": x.get("userId", ""), "amount": x.get("amount", ""), "location_id": x["location"].get("id")} for x in json_response["data"]]
    filtering_data2 = [{"userId": x.get("userId", ""), "amount": x.get("amount", "")} for x in filtering_data if x.get("location_id") == location_id]

    return filtering_data2

    


def transform(dataset):

    #filter1 = [[x.get("userId"), x.get("amount")] for x in dataset]

    #filter2 = [x[1:] if x==str else x for x in filter1[0]]
    
   


    #filter2 = [x(float(re.sub(r'[^\d\-.]', '')) if x != int else x for x in filter1]  
       
    #filter2 = [float(x) if x != float else x for x in filter1]


    #[[2, '$1,142.55'], [1, '$2,705.07'], [4, '$3,972.79']]
    #[{'userId': 2, 'amount': '$1,142.55'}, {'userId': 1, 'amount': '$2,705.07'}, {'userId': 4, 'amount': '$3,972.79'}]
    

    dataset[0][amount] = float(re.sub(r'[^\d\-.]', '', amount_str)
    print(dataset)
    
    
    






    






    











if __name__ == "__main__":

    h_r()