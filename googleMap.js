var data = {
    lat: null,
    lng: null,
    type: null
};

let markers = [];

function makeInfoBox(controlDiv, map) {
    // Set CSS for the control border.
    var controlUI = document.createElement('div');
    controlUI.style.boxShadow = 'rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px';
    controlUI.style.backgroundColor = '#fff';
    controlUI.style.border = '2px solid #fff';
    controlUI.style.borderRadius = '2px';
    controlUI.style.marginBottom = '22px';
    controlUI.style.marginTop = '10px';
    controlUI.style.textAlign = 'center';
    controlDiv.appendChild(controlUI);

    // Set CSS for the control interior.
    var controlText = document.createElement('div');
    controlText.style.color = 'rgb(25,25,25)';
    controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
    controlText.style.fontSize = '100%';
    controlText.style.padding = '6px';
    controlText.textContent = 'Where did you see the pet?';
    controlUI.appendChild(controlText);
}

/**
 * Creates a map object with a click listener and a heatmap.
 */
function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -31.956073336954443, lng: 115.85927305072086 },
        zoom: 15,
        styles: [{
            featureType: 'poi',
            stylers: [{ visibility: 'off' }]  // Turn off POI.
        },
        {
            featureType: 'transit.station',
            stylers: [{ visibility: 'off' }]  // Turn off bus, train stations etc.
        }],
        disableDoubleClickZoom: true,
        streetViewControl: false,
    });

    // Create the DIV to hold the control and call the makeInfoBox() constructor
    // passing in this DIV.
    var infoBoxDiv = document.createElement('div');
    makeInfoBox(infoBoxDiv, map);
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(infoBoxDiv);

    map.addListener('click', function (e) {
        data.lat = e.latLng.lat();
        data.lng = e.latLng.lng();
        console.log(data.lat);
        console.log(data.lng);
        window.localStorage.setItem('lat', data.lat);
        window.localStorage.setItem('lng', data.lng);
        addSighting(map, data)
    }
    );


    function addSighting(map, data) {
        new google.maps.Marker({
            position: { lat: data.lat, lng: data.lng },
            map
        });
    }
}

