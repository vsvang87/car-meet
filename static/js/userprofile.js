const modalOpenBtns = document.querySelectorAll(".update-btn");
const modalCloseBtn = document.getElementById("modal-close-btn");
const modalContainer = document.getElementById("modal")
const modalBg = document.querySelector(".modal-bg")

for (let btn of modalOpenBtns) {
  btn.addEventListener("click", () => {
    let btnSlice = btn.id.slice(2)
    console.log(btnSlice)
    let meetUpId = document.getElementById("meet_up_id")
    meetUpId.value = btnSlice
  
    modalBg.classList.add("bg-active")
    modalContainer.style.display = 'block'
    
})
}

modalCloseBtn.addEventListener("click", () => {
  modalContainer.style.display = 'none'
  modalBg.classList.remove("bg-active")
})

