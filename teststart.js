var arDrone = require('ar-drone');
var client  = arDrone.createClient();

setTimeout(function() {
console.log('World!');
}, 2000);
console.log('Hello');