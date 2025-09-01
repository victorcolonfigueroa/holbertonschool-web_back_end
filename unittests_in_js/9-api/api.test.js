// 9-api/api.test.js
// Integration tests for index and cart routes using the exported app

const { expect } = require("chai");
const request = require("request");
const app = require("./api");

describe("Index page", function () {
  let server;
  const baseUrl = "http://localhost:7865";

  before(function (done) {
    this.timeout(5000);
    server = app.listen(7865, done).on("error", done);
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

describe("Cart page", function () {
  let server;
  const baseUrl = "http://localhost:7865";

  before(function (done) {
    this.timeout(5000);
    server = app.listen(7865, done).on("error", done);
  });

  after(function (done) {
    this.timeout(5000);
    if (!server) return done();
    server.close(done);
  });

  it("Correct status code when :id is a number", function (done) {
    request.get(`${baseUrl}/cart/12`, (err, res) => {
      if (err) return done(err);
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it("Correct result for numeric id", function (done) {
    request.get(`${baseUrl}/cart/12`, (err, res, body) => {
      if (err) return done(err);
      expect(body).to.equal("Payment methods for cart 12");
      done();
    });
  });

  it("404 for non-numeric id", function (done) {
    request.get(`${baseUrl}/cart/hello`, (err, res) => {
      if (err) return done(err);
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
