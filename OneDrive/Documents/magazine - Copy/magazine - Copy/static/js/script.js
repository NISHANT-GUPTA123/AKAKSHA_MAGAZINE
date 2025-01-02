// Select the shapes for rotation
const shape = document.querySelector('.shape');
const shapeOrange1 = document.querySelector('.shape_orange-1');

// Initial rotation angle
let rotation1 = 0; // Rotation for shape
let rotation2 = 0; // Rotation for shapeOrange1
let lastScrollY = 0;

window.addEventListener('scroll', () => {
    const currentScrollY = window.pageYOffset;
    const scrollDirection = currentScrollY > lastScrollY ? 'down' : 'up';
    const scrollDelta = Math.abs(currentScrollY - lastScrollY);
    const rotationChange = scrollDelta * 0.1; // Adjust speed as needed

    // Corrected opposite rotation for each shape
    if (scrollDirection === 'down') {
        rotation1 -= rotationChange; // Rotate left for shape
        rotation2 += rotationChange; // Rotate right for shapeOrange1
    } else {
        rotation1 += rotationChange; // Rotate back to initial for shape
        rotation2 -= rotationChange; // Rotate back to initial for shapeOrange1
    }

    // Use transform-origin to rotate around the top-center
    shape.style.transformOrigin = 'top center';
    shapeOrange1.style.transformOrigin = 'top center';

    // Apply rotation to each shape separately
    shape.style.transform = `rotateZ(${rotation1}deg)`;
    shapeOrange1.style.transform = `rotateZ(${rotation2}deg)`;

    lastScrollY = currentScrollY;
});

// Toggle dropdown menu visibility
function toggleDropdown() {
    const menuBox = document.querySelector(".small-box1");
    menuBox.classList.toggle("active"); // Toggle active class for dropdown visibility
}

// Close the dropdown when clicking outside
window.onclick = function(event) {
    if (!event.target.matches('.small-box1 h3')) {
        const dropdown = document.querySelector(".small-box1");
        if (dropdown.classList.contains('active')) {
            dropdown.classList.remove('active');
        }
    }
}

// Image slideshow setup
let currentIndex = 0; // Index for image arrays
const images = [
    "https://cdn.prod.website-files.com/650880e89fe967ec5185e43c/654d5c3ba2e2c9c8d6ce98a3_Cut-Paper%20Textured%20Forms%20Layer%2016.webp",
    "https://cdn.prod.website-files.com/650880e89fe967ec5185e43c/65f1b3b1714878c4d1d27014_GN-Textured-Stone-Multi-05-400.png",
    "https://example.com/photograph3.jpg" // Placeholder image
];

// Change images every 5 seconds
function changeImages() {
    const photoBoxes = document.querySelectorAll('.photo-box img');
    photoBoxes.forEach((img, index) => {
        img.src = images[(currentIndex + index) % images.length];
    });
    currentIndex += 1; // Move to the next image
}
setInterval(changeImages, 5000);

// Another image slideshow (make sure you don't duplicate variable names)
const changingImages = [
    "https://fot.du.ac.in/userfiles/images/FacultyPhotos/fot/cs/dr_unmesh_shuklaa.jpg",
    "https://www.google.com/imgres?q=images&imgurl=https%3A%2F%2Fletsenhance.io%2Fstatic%2F8f5e523ee6b2479e26ecc91b9c25261e%2F1015f%2FMainAfter.jpg&imgrefurl=https%3A%2F%2Fletsenhance.io%2F&docid=-t22bY2ix3gHaM&tbnid=tYmxDgFq4MrkJM&vet=12ahUKEwibrpep5LWJAxX3UGcHHWwZE6QQM3oFCIIBEAA..i&w=1280&h=720&hcb=2&ved=2ahUKEwibrpep5LWJAxX3UGcHHWwZE6QQM3oFCIIBEAA",
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vecteezy.com%2Ffree-photos%2Fgreen-yellow-abstract-background%3Fpage%3D85&psig=AOvVaw1JVa-lOpjN8mFoeKJ68Rmy&ust=1735304705519000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKjjrYPAxYoDFQAAAAAdAAAAABAD"
];
let changingIndex = 0;

function changeImage() {
    const changingImage = document.getElementById('changing-image');
    changingImage.classList.add('hidden'); // Hide current image
    changingIndex = (changingIndex + 1) % changingImages.length; // Update index
    changingImage.src = changingImages[changingIndex]; // Change source
    changingImage.classList.remove('hidden'); // Show new image
}
setInterval(changeImage, 3000); // Change image every 3 seconds
const swiper = new Swiper('#heroCarousel_01', {
    loop: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

// signup
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
  container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
  container.classList.remove("right-panel-active");
});

document.getElementById("subscribe-button").addEventListener("click", function() {
    const email = document.getElementById("email").value;
    if (email) {
        alert("Thank you for subscribing with " + email);
        document.getElementById("email").value = ""; // Clear the input
    } else {
        alert("Please enter a valid email address.");
    }
});

document.getElementById("privacy-policy").addEventListener("click", function(event) {
    event.preventDefault();
    showModal("This is the Privacy Policy content.");
});

document.getElementById("terms-of-service").addEventListener("click", function(event) {
    event.preventDefault();
    showModal("This is the Terms of Service content.");
});

function showModal(text) {
    document.getElementById("modal-text").innerText = text;
    document.getElementById("modal").style.display = "block";
}

document.querySelector(".close").addEventListener("click", function() {
    document.getElementById("modal").style.display = "none";
});

window.onclick = function(event) {
    if (event.target == document.getElementById("modal")) {
        document.getElementById("modal").style.display = "none";
    }
}
