// defining our app and restangular
var app = angular.module('angApp', ['restangular']);

// Configuring the application for api connection
app.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl(
        'http://127.0.0.1:8000/api/'); 
});

// Define the controller for data searching from databases
app.controller('angCtrl', function($scope, Restangular) {
    Restangular.all('contactlist').getList().then(function(contactlist) {
        $scope.results = contactlist;
    });
});

// Standardize data format (extract from meta-data where needed)
app.config(function(RestangularProvider) {
    // add a response intereceptor
    RestangularProvider.addResponseInterceptor(function(data, operation, what, url, response, deferred) {
      var extractedData;
      //to look for getList operations
      if (operation === "getList") {
        //and handle the data and meta data
        extractedData = data.results;
      } else {
        extractedData = data;
      }
      return extractedData;
    });
});
// restrict for limitTo directive to four digit number on keypress
app.directive("limitTo", function() {
    return {
        restrict: "A",
        link: function(scope, elem, attrs) {
            var limit = parseInt(attrs.limitTo);
            angular.element(elem).on("keypress", function(e) {
                if (this.value.length == limit) e.preventDefault();
            });
        }
    }
});