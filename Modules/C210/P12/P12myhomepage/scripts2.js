window.onload= function(){alert("Hello")}
// ex 3a
document.getElementById("showFullName").addEventListener("click",()=>{
    document.getElementById("welcome-title").textContent+="- Nithul"
})
// ex 3b
const images= document.querySelectorAll("img")
images.forEach(img => {
    img.style.width= "50px";
    img.style.height="50px";
    img.style.border="2px solid pink";
})
//  ex 4
const listItems= document.querySelectorAll(".module-list li");
for(let i=0; i<listItems.length;i++){
    let theitem= listItems[i]; //the nth item
    theitem.addEventListener('click',function(){
        this.style.color= "blue";
    });
}
// ex 4a
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

// Ex 4B
function changeBkgrd(headers) {
    headers.style.backgroundColor = 'lightgrey';
  }
let btnChangeTheme = document.getElementById('buttonChangeHeader');
btnChangeTheme.addEventListener('click', function() {
    var headers = document.querySelectorAll('h1');
    headers.forEach(changeBkgrd);
    headers = document.querySelectorAll('h2');
    headers.forEach(changeBkgrd);
    headers = document.querySelectorAll('h3');
    headers.forEach(changeBkgrd);
});