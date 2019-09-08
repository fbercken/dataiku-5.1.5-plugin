var app = angular.module('myplugin.module', []);

app.controller('MyCustomFormController', function($scope) {
    
    $scope.config.hostname = "35.177.158.117"
    $scope.config.username = "admin"
    $scope.config.password = "admin123"
    $scope.config.sessionid = ""
    
    $scope.connect = function() {
        if ( $scope.config.hostname ) {
            $scope.callPythonDo({ "method": "connect" }).then(function(data) {
                $scope.tenants = data.tenants
                $scope.config.sessionid = data.sessionid
                $scope.config.selectedTenant = $scope.tenants[0]
                $scope.tenantChange()
                console.log(data)
            }, function(data) {
                $scope.tenants = [];
                $scope.templates = [] 
            });
        } else {
            $scope.tenants = [] 
            $scope.templates = [] 
        }
    };
    
    
    $scope.templateChange = function() {
        if ( $scope.config.selectedTemplate ) {
            currentTemplate = $scope.config.selectedTemplate
            $scope.config.clustername = currentTemplate['_embedded']['label']['name']
            $scope.config.clusterdescription = currentTemplate['_embedded']['label']['description']
        }
    }
  

    var tenantChange = function() {
        if ( $scope.config.selectedTenant ) {
            $scope.callPythonDo({ "method": "templates" }).then(function(data) {
                $scope.templates = data.templates;
                $scope.config.selectedTemplate = $scope.templates[0]
                templateChange()
                console.log(data)
            }, function(data) {
                $scope.templates = [];
            });
        } else {
            $scope.templates = [] 
        }
    };
    
    

    
  //  updateTenants();
    $scope.$watch('config.selectedTenant', tenantChange);
    $scope.$watch('config.selectedTemplate', templateChange);
});


 
  