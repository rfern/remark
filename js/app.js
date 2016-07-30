var apiUrl = "http://144.6.239.142:8080/";

function getMonitoringLocations() {
    $.get(apiUrl + "api/monitoring/All", function(data) {
      console.log("Load was performed.");
    })
    .done(function() {
        console.log("success");
    })
    .fail(function() {
        console.log("error");
    });
}

