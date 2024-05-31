document.addEventListener('DOMContentLoaded', function() {
    const countdownElements = document.querySelectorAll('.countdown');

    countdownElements.forEach(function(element) {
        const eventDate = new Date(element.getAttribute('data-date')).getTime();

        function updateCountdown() {
            const now = new Date().getTime();
            const distance = eventDate - now;

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            element.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

            if (distance < 0) {
                element.innerHTML = "Event has passed";
            }
        }

        setInterval(updateCountdown, 1000);
    });
});
