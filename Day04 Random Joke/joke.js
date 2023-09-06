const axios = require('axios');

async function fetchRandomJoke() {
  try {
    const response = await axios.get('https://v2.jokeapi.dev/joke/Any');
    
    if (response.status === 200) {
      const jokeData = response.data;
      
      if (jokeData.type === 'single') {
        console.log(jokeData.joke);
      } else if (jokeData.type === 'twopart') {
        console.log(jokeData.setup);
        console.log(jokeData.delivery);
      }
    } else {
      console.error('Failed to fetch a joke.');
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

fetchRandomJoke();
