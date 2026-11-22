const button = document.querySelector('#add_item');
const list = document.querySelector('ul.my_list');

button.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});
