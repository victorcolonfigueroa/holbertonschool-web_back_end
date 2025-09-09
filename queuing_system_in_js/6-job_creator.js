import kue from "kue";

// Create a Kue queue (uses Redis at 127.0.0.1:6379 by default)
const queue = kue.createQueue();

// Job data payload per specification
const jobData = {
  phoneNumber: "+15555550123",
  message: "This is the code to verify your account",
};

// Create a job in the 'push_notification_code' queue with the jobData
const job = queue.create("push_notification_code", jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Log when the job completes
job.on("complete", () => {
  console.log("Notification job completed");
});

// Log when the job fails
job.on("failed", () => {
  console.log("Notification job failed");
});
