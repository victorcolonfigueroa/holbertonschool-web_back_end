/**
 * 2-calcul_chai.js
 *
 * Same behavior as 1-calcul.js
 * calculateNumber(type, a, b)
 * - Rounds both a and b using Math.round
 * - 'SUM' => A + B
 * - 'SUBTRACT' => A - B
 * - 'DIVIDE' => A / B unless B === 0, then return 'Error'
 */
function calculateNumber(type, a, b) {
  const A = Math.round(a);
  const B = Math.round(b);

  switch (type) {
    case "SUM":
      return A + B;
    case "SUBTRACT":
      return A - B;
    case "DIVIDE":
      if (B === 0) return "Error";
      return A / B;
    default:
      throw new Error(
        `Invalid type: ${type}. Expected 'SUM', 'SUBTRACT', or 'DIVIDE'.`
      );
  }
}

module.exports = calculateNumber;
