
function initMap() {
  let options = {
    lat: 34.8526,
    lng: -82.3940
  }
 
  let map = new google.maps.Map(document.getElementById("map"), {
    center: options,
    zoom: 10,
  });

  let geocoder = new google.maps.Geocoder()
  const cityInput = document.getElementById("city").placeholder
  const stateInput = document.getElementById("state").placeholder

  // const address = document.getElementById("address")
  // geocoder.geocode({ address: `${cityInput}, ${stateInput}` })
  let cityAndState = `${cityInput}, ${stateInput}`;
  console.log(cityAndState)
  
   geocoder.geocode({ address: `${cityInput}, ${stateInput}` }, (results, status) => {
      if (status === 'OK') {
        // Get the coordinates of the user's location
        const userLocation = results[0].geometry.location;

        // Create a marker
        new google.maps.Marker({
          position: userLocation,
          map,
        });

        // Zoom in on the geolocated location
        map.setCenter(userLocation);
        map.setZoom(13);
      } else {
        console.log(`Geocode was unsuccessful for the following reason: ${status}`);
      }
    });
  
}




