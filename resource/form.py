from blueRest import BlueData


def connect(config):
    restClient = BlueData(config)
    #{ "hostname": config["hostname"], "username": config["username"], "password": config["password"] } )
    restClient.connect()
    tenants = restClient.getTenants()
    sessionid = restClient.getSessionId()
    return { 'sessionid': sessionid, 'tenants': tenants, 'templates': [] }
  
    
def templates(config):
    restClient = BlueData(config)
    restClient.connect()
    tenant = config["selectedTenant"]
    restClient.setTenant( tenant['_links']['self']['href'], tenant['label']['name'])
    templates = restClient.getTemplates()
    return { "templates": templates }


actions = {
    "connect": connect,
    "templates": templates
}


def do(payload, config, plugin_config, inputs):  
    return actions[payload["method"]](config)
