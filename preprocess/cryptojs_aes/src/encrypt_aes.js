const CryptoJS = require("crypto-js");

// Encrypt data using AES algorithm
function encryptText(data, secretKey) {
    let encrypted = CryptoJS.AES.encrypt(data, secretKey);
    return encrypted.toString();
}

// Parameters should be provided on command line
const secretKey = process.argv[2];
const data = process.argv[3];

// console.log(`data: ${data}`);
// console.log(`secretKey: ${secretKey}`);

// Verify if arguments were provided
if (!data || !secretKey) {
    console.error('Expected 2 arguments: "key" and "data"');
    process.exit(1);
}

// Encrypt data
const encryptedText = encryptText(data, secretKey);

// Exibe o resultado
console.log(encryptedText);
