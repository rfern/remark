var heatmap = null;

function onShowHideCarDensity() {
    console.log("SHOW/HIDE");
    if (heatmap == null) {
        $.get(apiUrl + "/api/carOwnership", function(data) {
            var heatMapData = [ ];

            $.each(data, function(index) {
                var f = data[index];
                row = { location: new google.maps.LatLng(
                          parseFloat(f.lng),
                          parseFloat(f.lat)),
                      weight: parseInt(f.CarsPerSQKM)
                  };
                heatMapData.push(row);
            });

            heatmap = new google.maps.visualization.HeatmapLayer({ data: heatMapData, map: window.map, disapating: true, radius: 120 });
        });
    } else {
        heatmap.setMap(null);
        heatmap = null;
    }
}

