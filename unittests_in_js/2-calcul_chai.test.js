// 2-calcul_chai.test.js
/**
 * Rewrite of 1-calcul.test.js using Chai's expect API
 */
const { expect } = require("chai");
const calculateNumber = require("./2-calcul_chai.js");

describe("calculateNumber(type, a, b) - Chai expect", () => {
  describe("SUM", () => {
    it("rounds (1.4, 4.5) and returns 6", () => {
      expect(calculateNumber("SUM", 1.4, 4.5)).to.equal(6);
    });
    it("rounds (1, 3.7) and returns 5", () => {
      expect(calculateNumber("SUM", 1, 3.7)).to.equal(5);
    });
    it("rounds (1.2, 3.7) and returns 5", () => {
      expect(calculateNumber("SUM", 1.2, 3.7)).to.equal(5);
    });
    it("rounds (1.5, 3.7) and returns 6", () => {
      expect(calculateNumber("SUM", 1.5, 3.7)).to.equal(6);
    });
    it("rounds (-1.5, 3.5) and returns 3 (mixed signs)", () => {
      expect(calculateNumber("SUM", -1.5, 3.5)).to.equal(3);
    });
  });

  describe("SUBTRACT", () => {
    it("rounds (1.4, 4.5) and returns -4", () => {
      expect(calculateNumber("SUBTRACT", 1.4, 4.5)).to.equal(-4);
    });
    it("rounds (3.7, 1.2) and returns 3", () => {
      expect(calculateNumber("SUBTRACT", 3.7, 1.2)).to.equal(3);
    });
    it("rounds (-1.5, -3.5) and returns 2", () => {
      expect(calculateNumber("SUBTRACT", -1.5, -3.5)).to.equal(2);
    });
    it("rounds (1.49, 1.5) and returns -1 (boundary)", () => {
      expect(calculateNumber("SUBTRACT", 1.49, 1.5)).to.equal(-1);
    });
  });

  describe("DIVIDE", () => {
    it("rounds (1.4, 4.5) and returns 0.2", () => {
      expect(calculateNumber("DIVIDE", 1.4, 4.5)).to.equal(0.2);
    });
    it("rounds (4.5, 1.4) and returns 5", () => {
      expect(calculateNumber("DIVIDE", 4.5, 1.4)).to.equal(5);
    });
    it("returns 'Error' when rounded denominator is 0: (1.4, 0)", () => {
      expect(calculateNumber("DIVIDE", 1.4, 0)).to.equal("Error");
    });
    it("returns 'Error' when both round to 0: (0.4, 0.4)", () => {
      expect(calculateNumber("DIVIDE", 0.4, 0.4)).to.equal("Error");
    });
    it("rounds (-1.5, 3.5) and returns -0.25", () => {
      expect(calculateNumber("DIVIDE", -1.5, 3.5)).to.equal(-0.25);
    });
    it("rounds (3.5, -1.5) and returns -4", () => {
      expect(calculateNumber("DIVIDE", 3.5, -1.5)).to.equal(-4);
    });
  });
});
