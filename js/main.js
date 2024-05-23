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

document.getElementById('whatsappForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Stop the form from submitting normally
    var message = "Enquiry direct whatsapp date time availablity feature implementation. Needs rafii confirmation for UI changes";
    var encodedMessage = encodeURIComponent(message);
    var phoneNumber = '+919633096006'; // Replace with the number you want to send the message to
    var whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodedMessage}`;
    window.open(whatsappUrl); // Open WhatsApp in a new tab/window
});