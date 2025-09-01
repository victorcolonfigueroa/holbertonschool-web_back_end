/**
 * api.js
 *
 * Express app that exposes:
 *   - GET / -> "Welcome to the payment system"
 *   - GET /cart/:id (numeric only) -> "Payment methods for cart :id"
 *   - GET /available_payments -> JSON object with payment methods
 *   - POST /login -> JSON body with { userName: string }
 *
 * When run directly (node api.js), the app listens on port 7865 and logs a message.
 * When required (for tests), the app is exported without binding a port.
 */
const express = require("express");
const app = express();

// Enable JSON body parsing for POST requests
app.use(express.json());

// Index route
app.get("/", (req, res) => {
  res.send("Welcome to the payment system");
});

// Cart route with numeric-only id validation in the path definition
app.get("/cart/:id(\\d+)", (req, res) => {
  const { id } = req.params;
  res.send(`Payment methods for cart ${id}`);
});

// Available payments route returns a JSON object with payment methods
app.get("/available_payments", (_req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

// Login route expects a JSON body with { userName: string }
app.post("/login", (req, res) => {
  const { userName } = req.body || {};
  if (!userName) {
    return res.status(400).send("Missing userName");
  }
  res.send(`Welcome ${userName}`);
});

// Only start the server when this file is executed directly
if (require.main === module) {
  app.listen(7865, () => {
    console.log("API available on localhost port 7865");
  });
}

module.exports = app;
