var app = angular.module('myplugin.module', []);

app.controller('MyCustomFormController', function($scope) {
    
    $scope.connect = function(config) {
        if ( config.hostname ) {
            $scope.callPythonDo({ "method": "connect"}).then(function(data) {
                $scope.tenants = data.tenants;
                console.log(data)
            }, function(data) {
                $scope.tenants = [];
            });
        } else {
            $scope.tenants = [] 
        }
    };

    var updateApplications = function() {
        if ( $scope.config.tenant ) {
            $scope.callPythonDo({}).then(function(data) {
                $scope.applications = data.applications;
            }, function(data) {
                $scope.applications = [];
            });
        } else {
            $scope.applications = [] 
        }
    };
    
  //  updateTenants();
    $scope.$watch('config.tenants', updateApplications);
});


 
  