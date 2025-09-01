/**
 * api.js
 *
 * Express app that exposes:
 *   - GET / -> "Welcome to the payment system"
 *   - GET /cart/:id (numeric only) -> "Payment methods for cart :id"
 *
 * When run directly (node api.js), the app listens on port 7865 and logs a message.
 * When required (for tests), the app is exported without binding a port.
 */
const express = require("express");
const app = express();

// Index route
app.get("/", (req, res) => {
  res.send("Welcome to the payment system");
});

// Cart route with numeric-only id validation in the path definition
app.get("/cart/:id(\\d+)", (req, res) => {
  const { id } = req.params;
  res.send(`Payment methods for cart ${id}`);
});

// Only start the server when this file is executed directly
if (require.main === module) {
  app.listen(7865, () => {
    console.log("API available on localhost port 7865");
  });
}

module.exports = app;
