/** Node: node for a singly linked list. */

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

/** LinkedList: chained together nodes. */

class LinkedList {
  constructor(vals = []) {
    this.head = null;
    this.tail = null;
    this.length = 0;

    for (let val of vals) this.push(val);
  }

  /** push(val): add new value to end of list. */

  push(val) {
    if (!this.head) {
      this.head = new Node(val);
      this.tail = this.head;
    } else if (!this.head.next) {
      this.head.next = new Node(val);
      this.tail = this.head.next;
    } else {
      this.tail.next = new Node(val);
      this.tail = this.tail.next;
    }
    this.length++;
  }

  /** unshift(val): add new value to start of list. */

  unshift(val) {
    if (!this.head) {
      this.push(val);
    } else {
      const newNode = new Node(val);
      newNode.next = this.head;
      this.head = newNode;
      this.length++;
    }
  }

  /** pop(): return & remove last item. */

  pop() {
    // normal scenario
    if (this.length === 1) {
      this.length = 0;
      let res = this.head.val;
      this.head = this.tail = null;
      return res;
    }
    let currNode = this.head;
    while (currNode.next && currNode.next.next) currNode = currNode.next;
    const res = currNode.next.val;
    this.tail = currNode;
    this.tail.next = null;
    this.length--;
    return res;
  }

  /** shift(): return & remove first item. */

  shift() {
    if (this.length === 1) {
      let res = this.head.val;
      this.head = this.tail = null;
      this.length--;
      return res;
    } else {
      let res = this.head.val;
      this.head = this.head.next;
      this.length--;
      return res;
    }
  }

  /** getAt(idx): get val at idx. */

  getAt(idx) {
    let currNode = this.head;
    let i = 0;
    while (i < idx) {
      i++;
      currNode = currNode.next;
    }

    return currNode.val;
  }
  /** setAt(idx, val): set val at idx to val */

  setAt(idx, val) {
    let currNode = this.head;
    let i = 0;
    while (i < idx) {
      i++;
      currNode = currNode.next;
    }
    currNode.val = val;
  }

  /** insertAt(idx, val): add node w/val before idx. */

  insertAt(idx, val) {
    if (idx === 0) {
      this.unshift(val);
    } else if (idx === this.length) {
      this.push(val);
    } else {
      let currNode = this.head;
      let i = 0;
      while (i < idx - 1) {
        i++;
        currNode = currNode.next;
      }
      let transpose = currNode.next;
      currNode.next = new Node(val);
      currNode.next.next = transpose;
      this.length++;
    }
  }

  /** removeAt(idx): return & remove item at idx, */

  removeAt(idx) {
    if (idx === 0) {
      this.shift();
    } else if (idx >= this.length - 1) {
      this.pop();
    } else {
      let currNode = this.head;
      let i = 0;
      while (i < idx - 1) {
        i++;
        currNode = currNode.next;
      }
      res = currNode.next;
      currNode.next = currNode.next.next;
      return res.val;
    }
  }

  /** average(): return an average of all values in the list */

  average() {
    if (this.length === 0) return 0;
    let sum = 0;
    let currNode = this.head;
    while (currNode) {
      sum += currNode.val;
      currNode = currNode.next;
    }
    return sum / this.length;
  }
}

module.exports = LinkedList;
