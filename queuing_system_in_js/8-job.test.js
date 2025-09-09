import kue from "kue";
import { expect } from "chai";
import createPushNotificationsJobs from "./8-job.js";

// Create a test queue instance
const queue = kue.createQueue();

describe("createPushNotificationsJobs", () => {
  // Enter test mode before the suite (no processing of jobs)
  before(() => {
    queue.testMode.enter();
  });

  it("create zero jobs when passed an empty array", () => {
    createPushNotificationsJobs([], queue);
    expect(queue.testMode.jobs.length).to.equal(0);
  });

  it("create multiple jobs and preserve payload & type", () => {
    const jobs = [
      { phoneNumber: "1111111111", message: "A" },
      { phoneNumber: "2222222222", message: "B" },
      { phoneNumber: "3333333333", message: "C" },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(3);

    queue.testMode.jobs.forEach((job, idx) => {
      expect(job.type).to.equal("push_notification_code_3");
      expect(job.data).to.deep.equal(jobs[idx]);
      // In test mode, ids are assigned as string unique ids
      expect(job.id).to.exist;
    });
  });

  it("throws for various invalid inputs (non-array)", () => {
    const invalids = [null, undefined, 42, "str", { a: 1 }];
    invalids.forEach((val) => {
      expect(() => createPushNotificationsJobs(val, queue)).to.throw(
        Error,
        "Jobs is not an array"
      );
    });
  });

  // Clear any created jobs after each test
  afterEach(() => {
    queue.testMode.clear();
  });

  // Exit test mode after the suite
  after(() => {
    queue.testMode.exit();
  });

  it("display a error message if jobs is not an array", () => {
    expect(() => createPushNotificationsJobs("not an array", queue)).to.throw(
      Error,
      "Jobs is not an array"
    );
  });

  it("create two new jobs to the queue", () => {
    const jobs = [
      {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account",
      },
      {
        phoneNumber: "4153518781",
        message: "This is the code 4562 to verify your account",
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate jobs in the test queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Check first job
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);

    // Check second job
    expect(queue.testMode.jobs[1].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
