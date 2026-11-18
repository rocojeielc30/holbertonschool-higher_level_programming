#!/usr/bin/node
function print () {
  const toPrint = process.argv[2];
  if (!Number.isNaN(toPrint)) {
    console.log('Not a number');
  } else {
    const converted = Number(toPrint);
    console.log(converted);
  }
}
print();
