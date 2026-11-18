#!/usr/bin/node
function print () {
  const toPrint = process.argv[2];
  if (toPrint === undefined) {
    console.log('No argument');
  } else {
    console.log(toPrint);
  }
}
print();
