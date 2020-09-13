function createSighting(opts) {
    console.log('Posting sighting');
    console.log(JSON.stringify(opts))
    fetch('#', {
        method: 'post',
        body: JSON.stringify(opts)
    }).then(function (response) {
        return response.json();
    }).then(function (data) {
        console.log('Reported Sighting', data.html_url);
    });
}

function submitSighting() {
    var lat = parseFloat(window.localStorage.getItem('lat'));
    var lng = parseFloat(window.localStorage.getItem('lng'));
    var description = document.querySelector('#description').value;
    var species = document.querySelector('#species').value;
    if (description) {
        createSighting({
            latitude: lat,
            longitude: lng,
            description: description,
            species: species
        });
    } else {
        console.log('Please select a position on map and enter description');
    }
}

var submitBtn = document.querySelector('button');
submitBtn.addEventListener('click', submitSighting);