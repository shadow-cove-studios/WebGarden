console.log("test")

var clickOrder = []

function clicka(bid) {
    console.log("Button Clicked")

    if (clickOrder.length == 2) {
        clickOrder = []
    }

    clickOrder.push(bid)
    checkClick()
}

function checkClick() {
    console.log(clickOrder.length)
    console.log(clickOrder.length == 2)
    console.log(clickOrder[0] == 1)
    console.log(clickOrder[1] == 2)
    if (
        clickOrder.length == 2 &&
        clickOrder[0] == 1 &&
        clickOrder[1] == 2
    ) {
        var element = document.querySelector('.Result')
        element.style.backgroundColor = 'yellow';
        console.log("Passed")
    } else if (
        clickOrder.length == 2 &&
        clickOrder[0] != 1 ||
        clickOrder[1] != 2
    ) {
        var element = document.querySelector('.Result')
        element.style.backgroundColor = 'red';
        console.log("Failed")
    }
}