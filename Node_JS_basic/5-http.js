const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  const { url } = req;
  const path = process.argv[2];

  if (url === '/') {
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    if (path !== null) {
      const message = 'This is the list of our students\n';
      try {
        const students = await countStudents(path);
        res.end(`${message}${students.join('\n')}`);
      } catch (err) {
        res.end(`${message}${err.message}`);
      }
    }
  } else {
    res.write('Not Found');
    res.end();
  }
});

app.listen(1245);

module.exports = app;
