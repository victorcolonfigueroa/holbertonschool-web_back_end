import redis from "redis";

// Create a client pointing to localhost:6379 (default)
const client = redis.createClient();

// Log when connected successfully
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

// Log errors when connection fails
client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
