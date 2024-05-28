
var images = ["image1.jpg", "image2.jpg", "image3.jpg"];


function showNextImage() {
    var currentIndex = images.indexOf(document.getElementById("slideshow"));
    if (currentIndex < images.length - 1) {
        document.getElementById("slideshow") = images[++currentIndex];
        setTimeout(showNextImage, 5000);
    } else {
        hideAllImgs();
    }
}

hideAllImgs();
showNextImage();
