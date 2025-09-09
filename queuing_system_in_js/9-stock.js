// 9-stock.js
// Express + Redis stock reservation demo
// - Provides product listing and reservation endpoints
// - Uses Redis to persist current available quantity per product
// - Leverages util.promisify for async/await with Redis client

import express from "express";
import redis from "redis";
import { promisify } from "util";

// ------------------ Data ------------------
export const listProducts = [
  { itemId: 1, itemName: "Suitcase 250", price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: "Suitcase 450", price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: "Suitcase 650", price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: "Suitcase 1050", price: 550, initialAvailableQuantity: 5 },
];

export function getItemById(id) {
  return listProducts.find((p) => p.itemId === id);
}

// ------------------ Redis ------------------
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

function stockKey(itemId) {
  return `item.${itemId}`;
}

export async function reserveStockById(itemId, stock) {
  // Set the current available stock for the item in Redis
  await setAsync(stockKey(itemId), stock);
}

export async function getCurrentReservedStockById(itemId) {
  const value = await getAsync(stockKey(itemId));
  if (value === null || value === undefined) return null;
  const n = Number(value);
  return Number.isNaN(n) ? null : n;
}

// ------------------ Server ------------------
const app = express();
const port = 1245;

// List all products (static fields only)
app.get("/list_products", (req, res) => {
  res.json(listProducts);
});

// Product detail with current quantity (from Redis if present)
app.get("/list_products/:itemId", async (req, res) => {
  const id = Number.parseInt(req.params.itemId, 10);
  const item = getItemById(id);
  if (!item) return res.json({ status: "Product not found" });

  const current = await getCurrentReservedStockById(id);
  const currentQuantity = current === null ? item.initialAvailableQuantity : current;

  return res.json({ ...item, currentQuantity });
});

// Reserve one unit if available
app.get("/reserve_product/:itemId", async (req, res) => {
  const id = Number.parseInt(req.params.itemId, 10);
  const item = getItemById(id);
  if (!item) return res.json({ status: "Product not found" });

  const current = await getCurrentReservedStockById(id);
  const available = current === null ? item.initialAvailableQuantity : current;

  if (available <= 0) {
    return res.json({ status: "Not enough stock available", itemId: id });
  }

  const newQty = available - 1;
  await reserveStockById(id, newQty);
  return res.json({ status: "Reservation confirmed", itemId: id });
});

app.listen(port, () => {
  // Log for convenience when running locally
  // console.log(`Server listening on http://localhost:${port}`);
});

export default app;
