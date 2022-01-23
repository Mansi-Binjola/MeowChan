import json
import requests
# import pandas as pd

class CatApi:
    def __init__(self):
        self.cred = {
        "api_key":"5a0210e7-d00e-4aad-8b66-8f07531d9487",
        "url":"https://api.thecatapi.com/v1/images/search"
        }
    def get_url(self,search=""):
        self.r = requests.get(self.cred['url']+search,headers={'x-api-key':self.cred['api_key']}).json()
        if(len(self.r)==0):
            return(self.msg())
        return(self.r[0])
        # id = r[0]['id']
        # info = requests.get("https://api.thecatapi.com/v1/images/"+id+"/analysis",headers={'x-api-key':api_key})
        # print(info.text)

    def get_info(self):
        id = self.get_url()['id']
        info = requests.get("https://api.thecatapi.com/v1/images/"+id+"/analysis",headers={'x-api-key':self.cred['api_key']}).json()
        # v = info.json()
        # v = pd.DataFrame(v)
        # print(v.labels)
        return(info)
    
    def save_image(self):
        url = self.r[0]
        name = url['url'].split('/')[-1]
        self.r = requests.get(url['url'])
        if(self.r.status_code ==200):
            try:
                with open(name, 'wb') as f:
                    f.write(self.r.content)
                return("saved")
            except:
                self.msg()    
        else:
            self.msg()

    def msg():
        return("There is some problem, try again later.")