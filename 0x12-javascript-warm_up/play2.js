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

switch (playpc) {
    case "tijera":
        if (playg === "piedra"){
            console.log("ganaste ante ", playpc);
        } else if (playg === "papel"){
            console.log("gana pc con ", playpc);
        } else {
            console.log("empty");
        }
        break;

    case "papel":
        if (playg === "tijera"){
            console.log("ganaste ante ", playpc);
        } else if (playg === "piedra"){
            console.log("gana pc con ", playpc);
        } else {
            console.log("empty");
        }
        break;

    case "piedra":
        if (playg === "papel"){
            console.log("ganaste ante ", playpc);
        } else if (playg === "tijera"){
            console.log("gana pc con ", playpc);
        } else {
            console.log("empty");
        }
        break;

    default:
        break;
}
