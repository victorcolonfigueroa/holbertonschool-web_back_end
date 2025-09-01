// 8-api/api.test.js
// Integration tests for the index route using request and the exported app

const { expect } = require("chai");
const request = require("request");
const app = require("./api");

describe("Index page", function () {
  let server;
  let baseUrl;

  before(function (done) {
    this.timeout(5000);
    // Start the app directly to avoid child process/port race issues
    server = app
      .listen(7865, () => {
        baseUrl = "http://localhost:7865";
        done();
      })
      .on("error", done);
  });

  after(function (done) {
    this.timeout(5000);
    if (!server) return done();
    server.close(done);
  });

  it("Correct status code?", function (done) {
    request.get(`${baseUrl}/`, (err, res) => {
      if (err) return done(err);
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it("Correct result?", function (done) {
    request.get(`${baseUrl}/`, (err, res, body) => {
      if (err) return done(err);
      expect(body).to.equal("Welcome to the payment system");
      done();
    });
  });

  it("Other? (Content-Type header)", function (done) {
    request.get(`${baseUrl}/`, (err, res) => {
      if (err) return done(err);
      expect(res.headers["content-type"]).to.match(/text\/html/);
      done();
    });
  });
});
