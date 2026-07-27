console.log("test")

var clickOrder = []

var validPlots = ["plot1"]

var seed = []

var plot1Planted = ""


function clickSeed(sid,color) {
    console.log("seed Clicked!",sid)
    seed = [sid,color]
}

function plantSeed(plotid) {
   
    if (
        validPlots.includes(plotid) && seed != []
    ) {
        var element = document.querySelector('.Result')
        
        element.style.backgroundColor = seed[1];
        console.log("Passed")
        plot1Planted = seed[0]

    } else if (
        validPlots.includes(plotid)==false
    ) {
        var element = document.querySelector('.Result')
        element.style.backgroundColor = 'brown';

        console.log("Failed")
        seed = []
    }
}