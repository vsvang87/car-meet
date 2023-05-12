
function initMap() {
  let options = {
    lat: 34.9496,
    lng: -81.9320
  }
 
  let map = new google.maps.Map(document.getElementById("map"), {
    center: options,
    zoom: 13,
  });

  let geocoder = new google.maps.Geocoder()
  const cityInput = document.getElementById("city").placeholder
  const stateInput = document.getElementById("state").placeholder
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
        map.setZoom(15);
      } else {
        console.log(`Geocode was unsuccessful for the following reason: ${status}`);
      }
    });
  
  let marker = new google.maps.Marker({
    position: options,
    map: map
  })

}




