// 4-payment.test.js
// Verifies sendPaymentRequestToApi uses Utils.calculateNumber('SUM', a, b)
// and logs the expected message. Uses a Sinon stub and restores stubs after.

const sinon = require("sinon");
const { expect } = require("chai");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./4-payment");

describe("sendPaymentRequestToApi", () => {
  let calcStub;
  let logStub;

  beforeEach(() => {
    // Stub Utils.calculateNumber to avoid running real logic and force return 10
    calcStub = sinon.stub(Utils, "calculateNumber").returns(10);
    logStub = sinon.stub(console, "log").returns();
  });

  afterEach(() => {
    calcStub.restore();
    logStub.restore();
  });

  it("stubs Utils.calculateNumber to 10 and logs 'The total is: 10'", () => {
    sendPaymentRequestToApi(100, 20);
    expect(calcStub.calledOnceWithExactly("SUM", 100, 20)).to.equal(true);
    expect(logStub.calledOnceWithExactly("The total is: 10")).to.equal(true);
  });
});
