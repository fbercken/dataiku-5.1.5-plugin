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
                $scope.applications = [] 
            });
        } else {
            $scope.tenants = [] 
            $scope.applications = [] 
        }
    };
  

    var tenantChange = function() {
        if ( $scope.config.selectedTenant ) {
            $scope.callPythonDo({ "method": "applications" }).then(function(data) {
                $scope.applications = data.applications;
                $scope.config.selectedApplication = $scope.applications[0]
                console.log(data)
            }, function(data) {
                $scope.applications = [];
            });
        } else {
            $scope.applications = [] 
        }
    };
    
  //  updateTenants();
    $scope.$watch('config.selectedTenant', tenantChange);
});


 
  