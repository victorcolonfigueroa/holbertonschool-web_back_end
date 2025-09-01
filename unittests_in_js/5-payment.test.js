// 5-payment.test.js
// Verifies console.log output for sendPaymentRequestToApi using a single spy

const sinon = require("sinon");
const { expect } = require("chai");
const sendPaymentRequestToApi = require("./5-payment");

describe("sendPaymentRequestToApi", () => {
  let logSpy;

  beforeEach(() => {
    // Use a single spy on console.log for all tests
    logSpy = sinon.spy(console, "log");
  });

  afterEach(() => {
    // Restore the spy to avoid cross-test pollution
    logSpy.restore();
  });

  it("logs 'The total is: 120' once for inputs 100 and 20", () => {
    sendPaymentRequestToApi(100, 20);
    expect(logSpy.calledOnceWithExactly("The total is: 120")).to.equal(true);
    expect(logSpy.calledOnce).to.equal(true);
  });

  it("logs 'The total is: 20' once for inputs 10 and 10", () => {
    sendPaymentRequestToApi(10, 10);
    expect(logSpy.calledOnceWithExactly("The total is: 20")).to.equal(true);
    expect(logSpy.calledOnce).to.equal(true);
  });
});
