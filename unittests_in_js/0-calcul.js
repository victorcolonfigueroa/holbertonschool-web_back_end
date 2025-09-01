/**
 * Calculate the sum of two numbers
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function calculateNumber(a, b) {
  return Math.round(a) + Math.round(b);
}

// CommonJS export to match the test's `require` usage
module.exports = calculateNumber;
