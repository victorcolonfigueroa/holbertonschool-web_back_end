import kue from "kue";

// Create a Kue queue (uses Redis at 127.0.0.1:6379 by default)
const queue = kue.createQueue();

// Blacklisted phone numbers per spec
const blacklisted = ["4153518780", "4153518781"];

/**
 * Send a notification with progress tracking and blacklist handling.
 * - Always emit 0% progress at start
 * - If phoneNumber is blacklisted -> fail the job
 * - Otherwise emit 50% progress, log the message, and complete the job
 */
function sendNotification(phoneNumber, message, job, done) {
  // Track 0% progress as required
  job.progress(0, 100);

  // Fail fast when number is blacklisted
  if (blacklisted.includes(String(phoneNumber))) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Midway progress update and log the action
  job.progress(50, 100);
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );

  // Finish job successfully (creator will log completion)
  return done();
}

// Process jobs from the 'push_notification_code_2' queue with concurrency = 2
queue.process("push_notification_code_2", 2, (job, done) => {
  const { phoneNumber, message } = job.data || {};
  sendNotification(phoneNumber, message, job, done);
});
