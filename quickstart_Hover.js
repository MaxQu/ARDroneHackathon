var arDrone = require('ar-drone');
var client  = arDrone.createClient();

client.takeoff();

client
  .after(1000, function() {
    this.front(0.1);
  })
  .after(100, function() {
    this.right(0.0);
  })
  .after(4000, function() {
    this.stop();
    this.land();
  });