window.onload = function () {
    alert("This is C210 L12 Ex1e !")
}

document.getElementById("myButton").addEventListener("click", function () {
    alert("I am clicked!")
})

document.getElementById("confirmButton").addEventListener("click", function () {
    const userResponse = confirm("Do you agree");
    if (userResponse) {
        alert (" You have agreed with me ");
    } else {
        alert("You do not agree with me????");
    }
})

function display_greeting() {
    alert("JavaScript is fun!");
}

setInterval(display_greeting, 5000); //every 5 secs