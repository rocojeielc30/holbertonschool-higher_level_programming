#!/usr/bin/node
function print () {
  const numOfArgs = process.argv.length;
  if (numOfArgs <= 2) {
    console.log('No argument');
  } else {
    const firstArg = process.argv[1];
    console.log(firstArg);
  }
}
print();
