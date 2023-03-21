document.getElementById("prev").addEventListener("click", prev)
document.getElementById("next").addEventListener("click", next)
let carousel = document.getElementsByClassName("carousel-inner")[0].children
counter = 0

function next() {
    if (carousel.length - 1 !== counter) {
        carousel[counter].classList.remove("active")
        carousel[counter + 1].classList.add("active")
        counter++
    }
}

function prev() {
    if (counter !== 0) {
        carousel[counter].classList.remove("active")
        carousel[counter - 1].classList.add("active")
        counter--
    }
}