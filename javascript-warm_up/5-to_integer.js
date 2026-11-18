#!/usr/bin/node
function print () {
  const toPrint = Number(process.argv[2]);
  if (!Number.isNaN(Number(toPrint))) {
    console.log('My number: ' + toPrint);
  } else {
    console.log('Not a number');
  }
}
print();
