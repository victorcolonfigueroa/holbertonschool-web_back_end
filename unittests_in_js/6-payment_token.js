// 6-payment_token.js
// Exports getPaymentTokenFromAPI(success) which resolves when success is true.

/**
 * getPaymentTokenFromAPI
 * - When success is true, returns a resolved Promise with
 *   { data: 'Successful response from the API' }.
 * - Otherwise, the function does nothing (returns undefined).
 */
function getPaymentTokenFromAPI(success) {
  // If success, resolve immediately with the expected payload
  if (success === true) {
    return Promise.resolve({ data: "Successful response from the API" });
  }
  // Otherwise do nothing (undefined)
}

module.exports = getPaymentTokenFromAPI;
