const toggleDarkTheme = () => {
    const skills = document.querySelectorAll("#content p");
    skills.forEach(skill => skill.classList.toggle("highlight"));
};

const updateLastUpdatedTime = () => {
    const footerTime = document.getElementById("footer-time");
    const currentDate = new Date();
    footerTime.textContent = "Last Updated: " + currentDate.toLocaleString();
};

const toggleProfileImage = () => {
    const profileImage = document.getElementById("profile-image");
    profileImage.classList.toggle("hidden");
};

document.getElementById("btnChangeTheme").addEventListener("click", () => {
    toggleDarkTheme();
    updateLastUpdatedTime();
});

document.getElementById("btnToggleProfileImage").addEventListener("click", () => {
    toggleProfileImage();
});

const animateWelcomeFontSize = () => {
    const welcomeTitle = document.getElementById("welcome-title");
    let currentSize = parseInt(window.getComputedStyle(welcomeTitle).fontSize);
    const targetSize = (currentSize === 32) ? 48 : 32; // Toggle between 32px and 48px
    const increment = (targetSize > currentSize) ? 1 : -1;

    const animationInterval = setInterval(() => {
        if (currentSize === targetSize) {
            clearInterval(animationInterval);
        } else {
            currentSize += increment;
            welcomeTitle.style.fontSize = currentSize + "px";
        }
    }, 100); // Adjust animation speed as needed
};

// Event listener for "Welcome" title animation
document.getElementById("welcome-title").addEventListener("click", () => {
    animateWelcomeFontSize();
});
