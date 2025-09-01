// run-mocha.js
const { spawn } = require("child_process");

const argv = process.argv.slice(2);

// If first arg looks like a filename starting with a digit, prefix with ./
const normalized =
  argv.length && /^[0-9]/.test(argv[0]) && !argv[0].startsWith("./")
    ? ["./" + argv[0], ...argv.slice(1)]
    : argv;

const args = normalized.length ? normalized : ["./*.test.js"];

const child = spawn("mocha", args, {
  stdio: "inherit",
  shell: true,
});

child.on("exit", (code) => process.exit(code));
