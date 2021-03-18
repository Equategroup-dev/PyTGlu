import requests
import json

class PyTglu():
    '''
    A Basic API caller to ITGlue, the API Key can be obtained via your ITGlue admin account.
    Current functionality includes making a get request, making a post request. I have also included
    two further functions that serve as an example of previous functions can be used to make calls
    '''
    def __init__(self, api, url):
        self.api = api
        self.url = url
        self.headers =  {"x-api-key": self.api,
                         "Content-Type": "application/json"}

    def getHeaders(self):
        return self.headers

    def getUrl(self):
        return self.url


    def makeGetRequest(self, endpoint):
        c = requests.get(url=self.getUrl()+'/'+endpoint, headers=self.getHeaders())
        return c

    def makePostRequest(self, endpoint, context):
        context = json.dumps(context)
        c = requests.post(url=self.getUrl() + endpoint, headers=self.getHeaders(), data=context )
        return c

    def getResults(self, c):
        try:
            # request has been made
            c.raise_for_status()
        except:
            # request failed
            print(c.text)
            raise
        returned_data = c.json()
        return returned_data

    def getOrganisations(self):
        enpoint = 'organizations?page[size]=1000'
        c = self.makeGetRequest(enpoint)
        results = self.getResults(c)
        return results

    def getConfigurations(self, organisation_id):
        endpoint = f'organizations/{organisation_id}/relationships/configurations'
        c = self.makeGetRequest(endpoint)
        results = self.getResults(c)
        return results



