import { code } from "esutils";

export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') throw new TypeError('Code must be a string');
    if (typeof name !== 'string') throw new TypeError('Name must be a string');
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(newCode) {
    if (typeof newCode == 'string' && newCode.length > 0) {
        this._code = newCode;
    } else {
        console.error('Invalid code');
    }
  }
   
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName == 'string' && newName.length > 0) {
        this._name = newName;
    } else {
        console.error('Invalid name');
    }
  }

  displayFullCurrency() {
    return '${this._name} (${this._code})';
  }
}
