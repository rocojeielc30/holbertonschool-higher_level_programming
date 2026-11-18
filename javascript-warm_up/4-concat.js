#!/usr/bin/node
function print () {
  const firstWord = process.argv[2];
  const secondWord = process.argv[3];
  if (firstWord === undefined && secondWord === undefined) {
    console.log('undefined is undefined');
  } else if (secondWord === undefined) {
    console.log(firstWord + ' is undefined');
  } else {
    console.log(firstWord + ' is ' + secondWord);
  }
}
print();
