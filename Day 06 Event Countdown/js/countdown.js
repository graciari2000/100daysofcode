document.addEventListener("DOMContentLoaded", function () {
    // Function to update the countdown timer
    function updateCountdown() {
        // Get the user's input date and time
        const inputDate = document.getElementById("date").value;
        const inputTime = document.getElementById("time").value;

        // Combine the date and time strings into a single datetime string
        const inputDateTimeString = inputDate + "T" + inputTime;

        // Calculate the target date and time in milliseconds
        const targetDate = new Date(inputDateTimeString).getTime();

        const x = setInterval(function () {
            // Get the current date and time
            const now = new Date().getTime();

            // Calculate the time remaining in milliseconds
            const distance = targetDate - now;

            if (distance <= 0) {
                clearInterval(x);
                document.getElementById("countdown").innerHTML = "EXPIRED";
            } else {
                // Calculate days, hours, minutes, and seconds
                const days = Math.floor(distance / (1000 * 60 * 60 * 24));
                const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // Update the HTML elements with the countdown values
                document.getElementById("days").textContent = days;
                document.getElementById("hours").textContent = hours;
                document.getElementById("minutes").textContent = minutes;
                document.getElementById("seconds").textContent = seconds;
            }
        }, 1000);
    }

    // Attach the updateCountdown function to the form's submit event
    document.querySelector("form").addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent the default form submission
        updateCountdown(); // Update the countdown based on user input
    });
});
