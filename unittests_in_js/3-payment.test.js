// 3-payment.test.js
// Verifies sendPaymentRequestToApi uses Utils.calculateNumber('SUM', a, b)
// and logs the expected message. Uses a Sinon spy and restores stubs after.

const sinon = require("sinon");
const { expect } = require("chai");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe("sendPaymentRequestToApi", () => {
  let calcSpy;
  let logStub;

  beforeEach(() => {
    calcSpy = sinon.spy(Utils, "calculateNumber");
    logStub = sinon.stub(console, "log");
  });

  afterEach(() => {
    calcSpy.restore();
    logStub.restore();
  });

  it("calls Utils.calculateNumber with SUM, 100, 20 and logs the total", () => {
    sendPaymentRequestToApi(100, 20);
    expect(calcSpy.calledOnceWithExactly("SUM", 100, 20)).to.equal(true);
    expect(logStub.calledOnceWithExactly("The total is: 120")).to.equal(true);
  });
});
