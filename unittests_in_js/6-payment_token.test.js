// 6-payment_token.test.js
// Tests async result of getPaymentTokenFromAPI using Mocha's done callback

const { expect } = require("chai");
const getPaymentTokenFromAPI = require("./6-payment_token");

describe("getPaymentTokenFromAPI", () => {
  it("resolves with expected data when success is true", (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({
          data: "Successful response from the API",
        });
        done();
      })
      .catch((err) => done(err));
  });
});
