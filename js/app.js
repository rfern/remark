var heatmap = null;

function onShowHideCarDensity() {
    console.log("SHOW/HIDE");
    if (heatmap == null) {
        $.get(apiUrl + "api/monitoring/Air%20quality", function(data) {
            var heatMapData = [ ];

            $.each(data, function(index) {
                var f = data[index];
                heatMapData.push({ location: new google.maps.LatLng(
                        parseFloat(f.Latitude),
                        parseFloat(f.Longitude)),
                    weight: 5
                });
            });
            heatmap = new google.maps.visualization.HeatmapLayer({ data: heatMapData, map: window.map });
        });
    } else {
        heatmap.setMap(null);
        heatmap = null;
    }
}

