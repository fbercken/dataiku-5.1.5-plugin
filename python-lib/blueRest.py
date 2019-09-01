import json
import requests

class BlueData(object):
   
    def _sessionExists(self):
        return True if self.headers['X-BDS-SESSION'] != null else False;
    
    def getSessionId(self):
        return self.headers['X-BDS-SESSION']
        
        
    def _invoke(self, path, payload={}, verb="GET"):
        count = 0
        while count <= self.retries:
             try:
                 response = requests.request( verb, self.base + path, headers=self.headers, data=json.dumps(payload), verify=False)
                 if response.ok:
                     return response
                 else:
                     response.raise_for_status()
             except IOError:
                 count += 1
                 #response.raise_for_status()
                 time.sleep(5)
        return response


    def __init__(self, config, retries=10):
        self.config = config
        self.retries = retries
        self.sessionid = config['sessionid']
        self.base = "http://" + config['hostname'] + ":8080"
        self.user = { "name":  config['username'], "password": config['password'] }
        self.session = { "password": config['password'], "tenant": "/api/v2/tenant/1", "role": "/api/v1/role/1", "site_admin_view ": True }
        self.headers =  { "Accept": "applicaiton/json", "Content-type": "application/json", 'X-BDS-SESSION': self.sessionid }


    def connect(self):
        response = self._invoke( "/api/v2/session/", self.user, "POST")
        self.sessionid = response.headers['Location']
        self.headers['X-BDS-SESSION'] = self.sessionid 


    def setTenant(self,tenantKey="/api/v2/tenant/1",tenantName="Site Admin"):
        self.session["tenant"] = tenantKey
        self.session["tenant_name"] = tenantName
        print("zz")
        response = self._invoke( "/api/v2/session/", self.session, "POST")
      #  self.headers['X-BDS-SESSION'] = response.headers['Location']
        print("eee")
        print(response)


    def getTenants(self):
        response = self._invoke("/api/v2/tenant/")
        if response.ok:
            data = json.loads(response.content)
            return data["_embedded"]["tenants"]
        else: 
            return []


    def getApplications(self):
        response = self._invoke("/api/v2/template/")
        print(response)
        if response.ok:
            data = json.loads(response.content)
            return data["_embedded"]["templates"]
        else: 
            return []

    def createApplication(self,application):
        pass

  