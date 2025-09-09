// createPushNotificationsJobs
// Creates Kue jobs in the 'push_notification_code_3' queue from a list of job payloads.
// - Validates that `jobs` is an array, otherwise throws Error('Jobs is not an array')
// - For each job: logs creation, completion, failure, and progress events

export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }

  jobs.forEach((data) => {
    const job = queue.create("push_notification_code_3", data);
    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    job.on("complete", () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on("failed", (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    job.on("progress", (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}
