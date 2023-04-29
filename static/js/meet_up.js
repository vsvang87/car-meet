const cityInput = document.getElementById("city");
const stateInput = document.getElementById("state");
const searchBtn = document.getElementById("search-button");

// Geolocation
const findMyState = () => {
 
  const success = (position) => {
    let cityEl = cityInput.value;
    let stateEl = stateInput.value;

    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    const geoApiUrl = `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en`

    fetch(geoApiUrl)
      .then((response) => response.json())
      .then((data) => {
        console.log(data)
        
        // findCity.textContent = data.city;
        // status.textContent = data.principalSubdivision;
    })
  }
  const error = () => {
    console.log("Error, unable to retrieve data")
  }
  navigator.geolocation.getCurrentPosition(success, error);

}
searchBtn.addEventListener("click", findMyState);


// google maps
function initMap() {
  
  let options = {
    lat: 34.5034,
    lng: -82.6501
  }
  let map = new google.maps.Map(document.getElementById("map"), {
    center: options,
    zoom: 13,
  });

  let marker = new google.maps.Marker({
    position: options,
    map: map
  })

}


