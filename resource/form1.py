from blueRest import BlueData

restClient = {}

def connect(config,):
    restClient = BlueData( { "hostname": config["hostname"], "user": config["username"], "password": config["password"] } )
    restClient.connect()
    tenants = restClient.getTenants()
    return {'tenants': tenants }
  
def applications(config):
    tenant = config.selectedTenant
    #restClient.setTenant( tenant['_links']['self']['href'], tenant['label']['name'])
    #applications = restClient.getApplications()
    return { "applications": applications }

actions = {
    "connect": connect,
    "applications": applications
}


def do(payload, config, plugin_config, inputs):
    
    return actions[payload["method"]](config)
    
   # if ( payload["method"] == "connect"):
   #     restClient = BlueData( { "hostname": config["hostname"], "user": config["username"], "password": config["password"] } )
    #    restClient.connect()
    #    tenants = restClient.getTenants()

    #return {'tenants': tenants, "method": payload, "config": config, "plugin_config": plugin_config, "inputs": inputs }
