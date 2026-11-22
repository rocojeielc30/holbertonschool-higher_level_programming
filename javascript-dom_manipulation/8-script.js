document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const element = document.querySelector('#hello');

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      element.textContent = data.hello;
    })
    .catch((error) => {
      console.error('Fetch failed:', error);
    });
});
