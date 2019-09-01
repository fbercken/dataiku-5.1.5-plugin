from blueRest import BlueData


#restClient = restClient if restClient else {}



def connect(config):
    restClient = BlueData( { "hostname": config["hostname"], "username": config["username"], "password": config["password"] } )
    restClient.connect()
    tenants = restClient.getTenants()
    sessionid = restClient.getSessionId()
    return { 'sessionid': sessionid, 'tenants': tenants, 'applications': [] }
  
    
def applications(config):
    tenant = config["selectedTenant"]
    #restClient.setTenant( tenant['_links']['self']['href'], tenant['label']['name'])
    #applications = restClient.getApplications()
    applications = [] #restClient.getTenants()
    return { "applications": applications }


actions = {
    "connect": connect,
    "applications": applications
}


def do(payload, config, plugin_config, inputs):
    
    return actions[payload["method"]](config)
    #return {'tenants': tenants, "method": payload, "config": config, "plugin_config": plugin_config, "inputs": inputs }
