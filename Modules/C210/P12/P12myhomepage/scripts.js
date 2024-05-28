window.onload = function (){
    alert("This is C210 L12 Ex 3 & 4!");
};

// ex 3A 
document.getElementById("showFullName").addEventListener("click", ()=>{
    document.getElementById("welcome-title").textContent += " - Nithul Chandralal";
});

// ex 3B
const images = document.querySelectorAll('img')
images.forEach(img => {
    img.style.width = "50px";     //change the dimension
    img.style.height = "50px";
    img.style.border = "20px solid blue"; //add a border 
});

// ex 3C
// Step 1 - select all list items under the div of "module-list"
const listItems = document.querySelectorAll(".module-list li");

// Step2 - Iterate over each list item
for (let i = 0; i < listItems.length; i++){
    let theItem = listItems[i]; // the nth item    

    // Step 3 - Add the click event 
    theItem.addEventListener("click", function(){
        this.style.color = "blue";
    });
}


// Change the Facebook image to Discord image
// Ex 4A
// Add a click event listener to the button
let btnChangeDiscord = document.getElementById('buttonDiscord');
btnChangeDiscord.addEventListener('click', function() {
    // Select the Facebook link and image using their ids
    let fbLink = document.getElementById('fbLink');
    let fbImage = document.getElementById('fbImg');
 
    // Change the Facebook link to a Discord link
    fbLink.href = 'http://www.discord.com/yourDiscordLink'; // replace with your Discord link
 
    // Change the Facebook image to a Discord image
    fbImage.src = 'discord.png'; // replace with your Discord image file
    fbImage.alt = 'Discord';
});


// Ex 4A
// Add a click event listener to the button
let btnChangeFB = document.getElementById('buttonFB');
btnChangeFB.addEventListener('click', function() {
    // Select the Facebook link and image using their ids
    let fbLink = document.getElementById('fbLink');
    let fbImage = document.getElementById('fbImg');
 
    // Change the Facebook link to a Discord link
    fbLink.href = 'http://www.facebook.com/replublicpolytechnic'; // replace with your Discord link
 
    // Change the Facebook image to a Discord image
    fbImage.src = 'fb.jpg'; // replace with your Discord image file
    fbImage.alt = 'Facebook';
});