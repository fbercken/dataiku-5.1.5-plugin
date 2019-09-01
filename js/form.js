var app = angular.module('myplugin.module', []);

app.controller('MyCustomFormController', function($scope) {
    
    var connect = function() {
        if ( $scope.config.hostname ) {
            $scope.callPythonDo({}).then(function(data) {
                $scope.tenants = data.tenants;
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
    
    updateTenants();
    $scope.$watch('config.hostname', updateTenants);
});


 
  