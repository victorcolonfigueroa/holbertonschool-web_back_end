class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw new TypeError('Name must be a string');
    if (typeof length !== 'number') throw new TypeError('Legnth must be a number');
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw new TypeError('Student must be an array of strings');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === 'string' && newName.length > 0) {
      this._name = newName;
    } else {
      console.error('Invalid name');
    }
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength === 'number' && newLength > 0) {
      this.length = newLength;
    } else {
      console.error('Invalid length');
    }
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if(Array.isArray(newStudents)) {
      this._students = newStudents;
    } else {
      console.error('Invalid students array');
    }
  }
}
