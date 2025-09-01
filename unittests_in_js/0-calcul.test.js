// 0-calcul.test.js
/**
 * Test the calculateNumber function
 * You can assume that a and b are always numbers
 * Test should be around the "rounded" part
 * You have to use assert
 * You should be able to run the thest suite using npm test 0-calcul.test.js
 * Every test should pass without any warning
 */
const assert = require("assert");
const calculateNumber = require("./0-calcul.js");

describe("calculateNumber", () => {
  it("rounds and returns the sum of 1 and 3 -> 4", () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it("rounds and returns the sum of 1 and 3.7 -> 5", () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });
  it("rounds and returns the sum of 1.2 and 3.7 -> 5", () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it("rounds and returns the sum of 1.5 and 3.7 -> 6", () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  // Edge cases
  it("rounds and returns the sum of 0 and 0.4 -> 0", () => {
    assert.strictEqual(calculateNumber(0, 0.4), 0);
  });
  it("rounds and returns the sum of 0 and 0.5 -> 1", () => {
    assert.strictEqual(calculateNumber(0, 0.5), 1);
  });
  it("rounds and returns the sum of -1.4 and -3.6 -> -5", () => {
    assert.strictEqual(calculateNumber(-1.4, -3.6), -5);
  });
  it("rounds and returns the sum of -1.5 and -3.5 -> -4 (Math.round halves go toward +Infinity)", () => {
    assert.strictEqual(calculateNumber(-1.5, -3.5), -4);
  });
  it("rounds and returns the sum of -1.5 and 3.5 -> 3 (mixed signs)", () => {
    assert.strictEqual(calculateNumber(-1.5, 3.5), 3);
  });
  it("rounds and returns the sum of 1.49 and 3.49 -> 4 (below .5)", () => {
    assert.strictEqual(calculateNumber(1.49, 3.49), 4);
  });
  it("rounds and returns the sum of 1.51 and 3.51 -> 6 (above .5)", () => {
    assert.strictEqual(calculateNumber(1.51, 3.51), 6);
  });
  it("rounds and returns the sum of large numbers 1000000.6 and 1000000.6 -> 2000002", () => {
    assert.strictEqual(calculateNumber(1000000.6, 1000000.6), 2000002);
  });
});
