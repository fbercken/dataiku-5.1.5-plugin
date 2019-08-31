from blueRest import BlueData

def do(payload, config, plugin_config, inputs):
    choices = ['aggg', 'b', 'c'] # fetch it however you like.
    
    restClient = BlueData( { "hostname": "35.177.158.117", "user": "admin", "password": "admin123" } )
    restClient.connect()
    
    choices = [ restClient.headers['X-BDS-SESSION'] ]
    
    return {'choices' : choices}
