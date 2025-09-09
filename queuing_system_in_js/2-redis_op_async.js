import redis from "redis";
import { promisify } from "util";

// Create a Redis client (defaults to localhost:6379)
// Using node-redis v2 API to match package.json (redis@^2.8.0)
const client = redis.createClient();

// Log when connected successfully
client.on("connect", () => {
  console.log("Redis client connected to the server");
  // Ensure 'Holberton' exists so the first display prints 'School'
  client.exists("Holberton", (err, reply) => {
    const proceed = async () => {
      await displaySchoolValue("Holberton");
      setNewSchool("HolbertonSanFrancisco", "100");
      await displaySchoolValue("HolbertonSanFrancisco");
    };
    if (err) {
      // If existence check fails, continue with demo calls
      proceed();
      return;
    }
    if (reply === 1) {
      proceed();
    } else {
      // Seed without redis.print to avoid extra output before 'School'
      client.set("Holberton", "School", () => proceed());
    }
  });
});

// Log when connection fails
client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Promisify get to use async/await
const getAsync = promisify(client.get).bind(client);

// Set a key with a value, using callback style. redis.print prints "Reply: OK" etc.
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Get a key's value and log it to the console using async/await
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.log(err);
  }
}
