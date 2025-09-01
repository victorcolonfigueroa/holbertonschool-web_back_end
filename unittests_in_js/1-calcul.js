/**
 * 1-calcul.js
 *
 * calculateNumber(type, a, b)
 * - Rounds both a and b using Math.round
 * - Performs operation based on `type`:
 *   - 'SUM': return roundedA + roundedB
 *   - 'SUBTRACT': return roundedA - roundedB
 *   - 'DIVIDE': if roundedB === 0 return 'Error', else return roundedA / roundedB
 *
 * Notes:
 * - Uses CommonJS export to match the test's `require` usage.
 * - Assumes a and b are numbers, as per task statement.
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
      // Keep simple, but explicit error helps during development
      throw new Error(
        `Invalid type: ${type}. Expected 'SUM', 'SUBTRACT', or 'DIVIDE'.`
      );
  }
}

module.exports = calculateNumber;
