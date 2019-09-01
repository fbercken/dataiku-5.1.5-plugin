from blueRest import BlueData

def do(payload, config, plugin_config, inputs):
    
    restClient = BlueData( { "hostname": "35.177.158.117", "user": "admin", "password": "admin123" } )
    restClient.connect()
    
    tenants = [ restClient.headers['X-BDS-SESSION'] ]
    
    return {'tenants' : tenants, "method": payload, "config": config }
