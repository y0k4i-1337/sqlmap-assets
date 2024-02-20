const CryptoJS = require("crypto-js");

// Decrypt data using AES algorithm
function decryptText(data, secretKey) {
    let decryptedBytes = "";
    try {
        decryptedBytes = CryptoJS.AES.decrypt(data, secretKey);
    } catch (error) {
        console.error("Error while decrypting data: ", error);
    }
    const decryptedText = decryptedBytes.toString(CryptoJS.enc.Utf8);

    return decryptedText;
}

// Parameters should be provided on command line
const secretKey = process.argv[2];
const data = process.argv[3];

//console.log(`data: ${data}`);
//console.log(`secretKey: ${secretKey}`);

// Verify if arguments were provided
if (!data || !secretKey) {
    console.error('Expected 2 arguments: "key" and "data"');
    process.exit(1);
}

// Decrypt data
const decryptedText = decryptText(data, secretKey);

// Print result
console.log("=== DECRYPTED DATA ===");
console.log(decryptedText);
