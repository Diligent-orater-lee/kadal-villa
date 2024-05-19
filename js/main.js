document.addEventListener("DOMContentLoaded", function() {
    const elements = document.querySelectorAll('.image-description');
    const windowHeight = window.innerHeight;

    function checkVisibility() {
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i];
            const position = element.getBoundingClientRect();

            // Checking if the element is within the viewport
            if ((position.top + 100) < windowHeight && position.bottom >= 100) {
                element.classList.add('is-visible');
            }
        }
    }

    window.addEventListener('scroll', checkVisibility);
    checkVisibility(); // Initial check on load
});