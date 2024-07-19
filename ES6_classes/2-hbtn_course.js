class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this._validateName(name);
    this._length = this._validateLength(length);
    this._students = this._validateStudents(students);
  }

  // Validate name
  _validateName(name) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    return name;
  }

  // Validate length
  _validateLength(length) {
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    return length;
  }

  // Validate students
  _validateStudents(students) {
    if (!Array.isArray(students) || !students.every(student => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    return students;
  }

  // Getter and setter for name
  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = this._validateName(newName);
  }

  // Getter and setter for length
  get length() {
    return this._length;
  }

  set length(newLength) {
    this._length = this._validateLength(newLength);
  }

  // Getter and setter for students
  get students() {
    return this._students;
  }

  set students(newStudents) {
    this._students = this._validateStudents(newStudents);
  }
}

// Example usage
const course = new HolbertonCourse('JavaScript', 10, ['John Doe', 'Jane Smith']);
console.log(course.name); // JavaScript
console.log(course.length); // 10
console.log(course.students); // ['John Doe', 'Jane Smith']

course.name = 'Python';
course.length = 12;
course.students = ['Alice', 'Bob'];

console.log(course.name); // Python
console.log(course.length); // 12
console.log(course.students); // ['Alice', 'Bob']
