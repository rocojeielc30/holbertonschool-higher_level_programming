const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const element = document.querySelector('#character');
fetch(url)
  .then((response) => response.json())
  .then((data) => {
    element.textContent = data.name;
  })
  .catch((error) => {
    console.error('Fetch failed:', error);
  })
