import redis from "redis";

// Using node-redis v2 API (matches package.json redis@^2.8.0)
const client = redis.createClient();

client.on("connect", () => {
  console.log("Redis client connected to the server");

  const key = "HolbertonSchools";
  const entries = [
    ["Portland", 50],
    ["Seattle", 80],
    ["New York", 20],
    ["Bogota", 20],
    ["Cali", 40],
    ["Paris", 2],
  ];

  // Set fields sequentially so we can display after all are written
  const setNext = (i) => {
    if (i >= entries.length) {
      // After all hset, display the stored hash
      client.hgetall(key, (err, obj) => {
        if (err) {
          console.log(err);
          return;
        }
        console.log(obj);
      });
      return;
    }

    const [field, value] = entries[i];
    client.hset(key, field, value, (err, reply) => {
      // Print confirmation for each hset
      redis.print(err, reply);
      setNext(i + 1);
    });
  };

  setNext(0);
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
