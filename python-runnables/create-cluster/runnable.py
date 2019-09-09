from blueRest import BlueData
from dataiku.runnables import Runnable

import json

class MyRunnable(Runnable):
    def __init__(self, project_key, config, plugin_config):
        self.config = config
        self.project_key = project_key
        self.plugin_config = plugin_config
        
    def get_progress_target(self):
        return None

    def run(self, progress_callback):
        restClient = BlueData(self.config)
        restClient.connect()
        tenant = self.config["selectedTenant"]
        restClient.setTenant( tenant['_links']['self']['href'], tenant['label']['name'])
        
        clusterSpec = self.config['selectedTemplate']['_embedded']['clusterspec']
       # del clusterSpec['cluster_type']
        #del clusterSpec['_links']
        clusterSpec['label'] = { "name": self.config['clustername'], "description": self.config['clusterdescription'] }

        
        clusterId = restClient.createCluster(clusterSpec)
        data = restClient.getCluster(clusterId)

        #return '<div>The values in the form are:</div><pre class="debug">%s</pre>' % self.config % restClient.getTenants()
        
        return '<div>The Cluster has been created sucessfully:</div><pre class="debug">%s</pre>' % data 