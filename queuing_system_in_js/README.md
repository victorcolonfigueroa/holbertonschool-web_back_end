# Queuing System in JS

This project implements a basic queuing system using JavaScript. It demonstrates how to manage tasks or requests in a queue, process them sequentially, and handle asynchronous operations.

## Features

- Add tasks to the queue
- Process tasks one at a time
- Support for asynchronous task handling
- Simple and extensible design

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/queuing_system_in_js.git
cd queuing_system_in_js
```

## Usage

Import or require the queue module in your JavaScript project and use its API to add and process tasks.

## Example

```js
const Queue = require('./queue');

const queue = new Queue();

queue.add(() => {
    console.log('Task 1');
});

queue.add(async () => {
    await someAsyncFunction();
    console.log('Task 2');
});

queue.process();
```
