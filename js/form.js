var app = angular.module('myplugin.module', []);

app.controller('MyCustomFormController', function($scope) {

    var updateTenants = function() {
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
    
    updateTenants();
    $scope.$watch('config.hostname', updateTenants);
});


 
  