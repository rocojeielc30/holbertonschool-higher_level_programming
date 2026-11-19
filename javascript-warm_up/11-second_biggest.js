#!/usr/bin/node
function secondBiggest () {
  const argumentCount = process.argv.length - 2;
  if (argumentCount <= 1) {
    console.log(0);
    return;
  }

  let biggest = -Infinity;
  let second = -Infinity;
  let i = 2;

  while (i < process.argv.length) {
    const current = parseInt(process.argv[i]);
    if (current > biggest) {
      second = biggest;
      biggest = current;
    } else if (current < biggest && current > second) {
      second = current;
    }
    i++;
  }
  console.log(second);
}
secondBiggest();
