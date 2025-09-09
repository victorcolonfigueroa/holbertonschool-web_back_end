import kue from "kue";

// Create a Kue queue (uses Redis at 127.0.0.1:6379 by default)
const queue = kue.createQueue();

// Simple notification sender (logs per spec)
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs from the 'push_notification_code' queue
// Each job contains: { phoneNumber: string, message: string }
queue.process("push_notification_code", (job, done) => {
  const { phoneNumber, message } = job.data || {};
  sendNotification(phoneNumber, message);
  done();
});
