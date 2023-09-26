const apiKey = '1794df7061ed0488a4e038f766144600';
const apiUrl = 'https://api.openweathermap.org/data/3.0/onecall?lat=';

function getWeather() {
    const location = document.getElementById('locationInput').value;

    if (!location) {
        alert('Please enter a location.');
        return;
    }

    // Construct the API URL
    const url = `${apiUrl}?q=${location}&appid=${apiKey}`;

    // Make a GET request to the weather API
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Extract and display weather information
            const weatherDisplay = document.getElementById('weatherDisplay');
            weatherDisplay.innerHTML = `
                <h2>Weather in ${data.name}</h2>
                <p>Temperature: ${data.main.temp} °C</p>
                <p>Weather: ${data.weather[0].description}</p>
            `;
        })
        .catch(error => {
            alert('Weather data not found. Please enter a valid location.');
        });
}
