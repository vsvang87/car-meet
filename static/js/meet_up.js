// const searchBtn = document.getElementById("search-button");

// const findMyState = () => {
  
//   const success = (position) => {
//   console.log(position)
   
//     const latitude = position.coords.latitude;
//     const longitude = position.coords.longitude;

//     const geoApiUrl = `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en`;

//     fetch(geoApiUrl)
//       .then((response) => response.json())
//       .then((data) => {
//         console.log(data)
//         document.getElementById('findCity').innerHTML = data.city;
//         document.getElementById('findState').innerHTML = data.principalSubdivision;
//     })
//   }
//   const error = () => {
//     console.log("Error, unable to retrieve data")
//   }
//   navigator.geolocation.getCurrentPosition(success, error);
// }
// searchBtn.addEventListener("click", findMyState());


// google maps
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
        map.setZoom(18);
      } else {
        alert(`Geocode was unsuccessful for the following reason: ${status}`);
      }
    });
  
  let marker = new google.maps.Marker({
    position: options,
    map: map
  })

  // geocodeLatLng(geocoder,map)
}

//  function geocodeLatLng(geocoder, map) {
  
// }


