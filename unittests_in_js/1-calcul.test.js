// 1-calcul.test.js
/**
 * Test the calculateNumber(type, a, b) function
 * - Rounds a and b (Math.round)
 * - type: 'SUM' | 'SUBTRACT' | 'DIVIDE'
 * - DIVIDE: if rounded b === 0 -> returns 'Error'
 * Requirements:
 * - Use assert
 * - Organize with describe blocks
 */
const assert = require("assert");
const calculateNumber = require("./1-calcul.js");

describe("calculateNumber(type, a, b)", () => {
  describe("SUM", () => {
    it("rounds (1.4, 4.5) and returns 6", () => {
      assert.strictEqual(calculateNumber("SUM", 1.4, 4.5), 6);
    });
    it("rounds (1, 3.7) and returns 5", () => {
      assert.strictEqual(calculateNumber("SUM", 1, 3.7), 5);
    });
    it("rounds (1.2, 3.7) and returns 5", () => {
      assert.strictEqual(calculateNumber("SUM", 1.2, 3.7), 5);
    });
    it("rounds (1.5, 3.7) and returns 6", () => {
      assert.strictEqual(calculateNumber("SUM", 1.5, 3.7), 6);
    });
    it("rounds (-1.5, 3.5) and returns 3 (mixed signs)", () => {
      assert.strictEqual(calculateNumber("SUM", -1.5, 3.5), 3);
    });
  });

  describe("SUBTRACT", () => {
    it("rounds (1.4, 4.5) and returns -4", () => {
      assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 4.5), -4);
    });
    it("rounds (3.7, 1.2) and returns 3", () => {
      assert.strictEqual(calculateNumber("SUBTRACT", 3.7, 1.2), 3);
    });
    it("rounds (-1.5, -3.5) and returns 2", () => {
      assert.strictEqual(calculateNumber("SUBTRACT", -1.5, -3.5), 2);
    });
    it("rounds (1.49, 1.5) and returns -1 (boundary)", () => {
      assert.strictEqual(calculateNumber("SUBTRACT", 1.49, 1.5), -1);
    });
  });

  describe("DIVIDE", () => {
    it("rounds (1.4, 4.5) and returns 0.2", () => {
      assert.strictEqual(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);
    });
    it("rounds (4.5, 1.4) and returns 5", () => {
      assert.strictEqual(calculateNumber("DIVIDE", 4.5, 1.4), 5);
    });
    it("returns 'Error' when rounded denominator is 0: (1.4, 0)", () => {
      assert.strictEqual(calculateNumber("DIVIDE", 1.4, 0), "Error");
    });
    it("returns 'Error' when both round to 0: (0.4, 0.4)", () => {
      assert.strictEqual(calculateNumber("DIVIDE", 0.4, 0.4), "Error");
    });
    it("rounds (-1.5, 3.5) and returns -0.25", () => {
      assert.strictEqual(calculateNumber("DIVIDE", -1.5, 3.5), -0.25);
    });
    it("rounds (3.5, -1.5) and returns -4", () => {
      assert.strictEqual(calculateNumber("DIVIDE", 3.5, -1.5), -4);
    });
  });
});
