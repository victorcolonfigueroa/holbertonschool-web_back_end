export default class Currency {
  constructor(code, name) {
    if (typeof code === 'string') {
      this._code = code;
    } else {
      throw TypeError('Code must be a string');
    }

    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  get code() {
    return this._code;
  }

  set code(newCode) {
    this._code = newCode;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = newName;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
