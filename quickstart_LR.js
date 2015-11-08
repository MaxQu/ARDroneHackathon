var arDrone = require('ar-drone');
var client  = arDrone.createClient();

client.takeoff();

client
  .after(100, function() {
    this.front(0.0);
  })
  .after(2000, function() {
    this.left(0.2);
  })
  .after(1000, function() {
    this.right(0.2);
  })
  .after(1000, function() {
    this.stop();
    this.land();
  });