
// google maps
function initMap() {
  let options = {
    lat: 34.8726,
    lng: 82.3625
  }
  const basicMap = new google.maps.Map(document.getElementById("map"), {
    center: options,
    zoom: 10
  })

}


