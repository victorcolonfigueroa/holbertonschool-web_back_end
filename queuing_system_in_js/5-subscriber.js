import redis from "redis";

// Node-redis v2 API (matches package.json redis@^2.8.0)
const client = redis.createClient();
const CHANNEL = "holberton school channel";

client.on("connect", () => {
  console.log("Redis client connected to the server");
  // Subscribe once connected
  client.subscribe(CHANNEL);
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Receive messages from the subscribed channel
client.on("message", (channel, message) => {
  console.log(message);
  if (message === "KILL_SERVER") {
    client.unsubscribe(channel);
    client.quit();
  }
});
