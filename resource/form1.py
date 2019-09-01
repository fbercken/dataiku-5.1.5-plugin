from blueRest import BlueData

def do(payload, config, plugin_config, inputs):
    
   # if ( payload["method"] == "connect"):
       # restClient = BlueData( { "hostname": plugin_config.hostname, "user": plugin_config.username, "password": plugin_config.password } )
       # restClient.connect()
       # tenants = [ restClient.headers['X-BDS-SESSION'] ]
    tenants = [] 
    return {'tenants' : tenants, "method": payload, "config": config, "plugin_config": plugin_config, "inputs": inputs }
