#!/usr/bin/node

const args = process.argv;

function randomNumber (min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
const pc = randomNumber(0, 2);
let playpc;
const playg = args[2];
if (pc === 0) {
  playpc = 'tijera';
} else if (pc === 1) {
  playpc = 'papel';
} else {
  playpc = 'piedra';
}

if (playpc === playg) {
  console.log('empty');
} else {
  if (playpc === 'tijera') {
    if (playg === 'piedra') {
      console.log('ganaste');
    } else {
      console.log('gana pc con ', playpc);
    }
  } else if (playpc === 'papel') {
    if (playg === 'tijera') {
      console.log('ganaste');
    } else {
      console.log('gana pc con ', playpc);
    }
  } else {
    if (playg === 'papel') {
      console.log('ganaste');
    } else {
      console.log('gana pc con ', playpc);
    }
  }
}
