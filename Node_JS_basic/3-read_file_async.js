const fs = require('fs');

async function countStudents(path) {
  try {
    const listCS = [];
    const listSWE = [];

    const data = await fs.promises.readFile(path, 'utf8');

    const rows = data.trim().split('\n');

    for (let i = 1; i < rows.length; i += 1) {
      const row = rows[i].split(',');

      if (row[3] === 'CS') listCS.push(row[0]);
      else if (row[3] === 'SWE') listSWE.push(row[0]);
    }

    console.log(`Number of students: ${rows.length - 1}`);
    console.log(`Number of students in CS: ${listCS.length}. List: ${listCS.join(', ')}`);
    console.log(`Number of students in SWE: ${listSWE.length}. List: ${listSWE.join(', ')}`);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
