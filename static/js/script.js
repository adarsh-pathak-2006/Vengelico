var menuButton = document.querySelector(".menu-btn");
var navLinks = document.querySelector(".nav-links");
var contactForm = document.getElementById("contact-form");
var addButtons = document.querySelectorAll(".product button");
var revealItems = document.querySelectorAll(".reveal");

if (menuButton && navLinks) {
    menuButton.addEventListener("click", function () {
        navLinks.classList.toggle("open");
    });
}

if ("IntersectionObserver" in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
            }
        });
    }, { threshold: 0.15 });

    revealItems.forEach(function (item) {
        revealObserver.observe(item);
    });
} else {
    revealItems.forEach(function (item) {
        item.classList.add("visible");
    });
}

addButtons.forEach(function (button) {
    button.addEventListener("click", function () {
        button.textContent = "Added";
        setTimeout(function () {
            button.textContent = "Add to Bag";
        }, 1200);
    });
});

if (contactForm) {
    contactForm.addEventListener("submit", function (event) {
        var formMessage = contactForm.querySelector(".form-message");

        event.preventDefault();
        formMessage.textContent = "Thank you. Vengelico will contact you soon.";
        contactForm.reset();
    });
}
