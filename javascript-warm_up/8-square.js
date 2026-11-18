#!/usr/bin/node
function print () {
  const size = parseInt(process.argv[2]);
  if (Number.isNaN(size)) {
    console.log('Missing size');
  }
  for (let i = 0; i != size; i++) {
    let row = '';
    for (let i = 0; i != size; i++) {
      row += 'X';
    }
    console.log(row);
  }
}
print();
