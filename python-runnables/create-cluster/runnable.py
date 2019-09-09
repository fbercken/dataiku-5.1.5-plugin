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
        #clusterGroup = clusterSpec['nodegroup']
        
        zz = {
            "label": { "name": "err", "description": "ddd"},
            "nodegroup": {
                "role_configs": [
                    {"node_count": 1, "flavor_name": "Medium", "role_id": "controller"}, 
                    {"node_count": 1, "flavor_name": "Small", "role_id": "worker" }
                ], 
                "catalog_entry_distro_id": "bluedata/hdp31-ambari27-7x",
                "config_choice_selections": [
                    {"choice_id": "apps", "selection_id": False },
                    {"choice_id": "all_ha", "selection_id": False }, 
                    {"choice_id": "kerberos", "selection_id": False }, 
                    {"choice_id": "use_local_repo", "selection_id": False }
                ]
            }
        }
        
        data1 = json.dumps(clusterSpec)
        
        clusterId = restClient.createCluster(clusterSpec)
        
        data = restClient.getCluster(clusterId)

        #return '<div>The values in the form are:</div><pre class="debug">%s</pre>' % self.config % restClient.getTenants()
        
        return '<div>The Cluster has been created sucessfully:</div><pre class="debug">%s</pre>' % data 