const searchBtn = document.getElementById("search-button");
const searchContent = document.getElementById("search-content");

fetch('/meet_up')
  .then((response) => response.json())
  .then((serverData) => {
    searchContent.innerHTML = serverData.meetups
  })

