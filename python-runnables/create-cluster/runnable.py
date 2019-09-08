from blueRest import BlueData
from dataiku.runnables import Runnable

class MyRunnable(Runnable):
    def __init__(self, project_key, config, plugin_config):
        self.project_key = project_key
        self.config = config
        self.plugin_config = plugin_config
        
    def get_progress_target(self):
        return None

    def run(self, progress_callback):
        restClient = BlueData(self.config)
        restClient.connect()
        
        clusterLabel = { "name": self.config['clustername'], "description": self.config['clusterdescription'] }
        clusterSpec = self.config['selectedTemplate']['_embedded']['clusterspec']
        
        clusterGroup = { "catalog_entry_distro_id": clusterSpec['catalog_entry_distro_id'], "config_choice_selections": clusterSpec['config_choice_selections'] }
        data = restClient.createCluster( clusterLabel, clusterGroup)
        
        #data = restClient.createCluster()
        #return '<div>The values in the form are:</div><pre class="debug">%s</pre>' % self.config % restClient.getTenants()
        
        return '<div>The values in the form are:</div><pre class="debug">%s</pre>' % data 