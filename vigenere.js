let arguments = process.argv;

// get filesystem module
const fs = require("fs");

let buffer = fs.readFileSync(arguments[2]);
let keyString = buffer.toString().replace(/[^A-Za-z]+/g, '').toLowerCase();

console.log()
console.log()

console.log('Vigenere Key:')
console.log()

function printToConsole(file, limit) {
    for (let i = 0; i < file.length; i++) {
        process.stdout.write(file.charAt(i));

        if ((i + 1) % limit == 0)
            console.log();
    }
    console.log();
}

printToConsole(keyString, 80);

console.log()
console.log()

console.log('Plaintext:')
console.log()

buffer = fs.readFileSync(arguments[3]);
let plaintextString = buffer.toString().replace(/[^A-Za-z]+/g, '').toLowerCase();

function makingPlaintext(plaintextStr) {
    while (plaintextStr.length < 512)
        plaintextStr += 'x';

    if (plaintextStr.length > 512)
        return plaintextStr.substring(0, 512);

    return plaintextStr;
}

plaintextString = makingPlaintext(plaintextString)

printToConsole(plaintextString, 80);

console.log()
console.log()

function modifyKeyString(keyStr) {
    const initialKeyLen = keyStr.length;
    let keyTracker = 0;

    while (keyStr.length < 512) {
        // Notice the keyTracker post-increment
        keyStr += keyStr.charAt(keyTracker++);

        if (keyTracker >= initialKeyLen)
            keyTracker = 0;
    }

    return keyStr;
}

keyString = modifyKeyString(keyString);

function buildingCiphertext(keyString, plaintextStr) {
    let cipherStr = "";

    for (let i = 0; i < plaintextStr.length; i++) {
        let plainTextDec = plaintextStr.charAt(i).charCodeAt(0) - 'a'.charCodeAt(0);
        let keyDec = keyString.charAt(i).charCodeAt(0) - 'a'.charCodeAt(0);

        let addDec = (plainTextDec + keyDec) % 26;
        let cipherChar = String.fromCharCode(addDec + 'a'.charCodeAt(0));
        cipherStr += cipherChar;
    }

    return cipherStr;
}

cipherStr = buildingCiphertext(keyString, plaintextString);

console.log('Ciphertext:')
console.log()

printToConsole(cipherStr, 80);
