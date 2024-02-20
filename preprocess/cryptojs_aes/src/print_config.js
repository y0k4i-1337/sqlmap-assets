const CryptoJS = require("crypto-js");
// This is a simple debug script to print
// actual key and IV used by CryptoJS when a secret key is provided by user

// Parameter provided on command line
const secretKey = process.argv[2];

// Verify if argument was provided
if (!secretKey) {
    console.error('Expected "key" as argument');
    process.exit(1);
}

var encrypted = CryptoJS.AES.encrypt("Test message", secretKey);

console.log("=== User provided config ===");
console.log(`secret key: ${secretKey}`);
console.log();
console.log("=== CryptoJS derived key and IV ===");
console.log(`key: ${encrypted.key.toString()}`);
console.log(`iv : ${encrypted.iv.toString()}`);
