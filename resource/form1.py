from blueRest import BlueData

def do(payload, config, plugin_config, inputs):
    
    if ( payload.method == "connect"):
        restClient = BlueData( { "hostname": config.hostname, "user": config.username, "password": config.password } )
        restClient.connect()
        tenants = [ restClient.headers['X-BDS-SESSION'] ]
    
    return {'tenants' : tenants, "method": payload, "config": config }
