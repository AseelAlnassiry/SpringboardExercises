// Quick Question #1
new Set([1, 1, 2, 2, 3, 4]); // -> {1, 2, 3, 4}

// Quick Question #2
const q2 = [...new Set('referee')].join(''); // -> 'ref'

// Quick Questions #3
let m = new Map();
m.set([1, 2, 3], true);
m.set([1, 2, 3], false);
// -> 0: {Array(3) => true}
// -> 1: {Array(3) => false}

// hasDuplicate
const hasDuplicate = (arr) => new Set(arr).size !== arr.length;

// vowelCount
const vowelCount = (str) => {
  const vowels = 'aieou';
  const res = new Map();
  for (let c of str.toLowerCase()) {
    if (vowels.includes(c)) {
      if (res.has(c)) res.set(c, res.get(c) + 1);
      else res.set(c, 1);
    }
  }

  return res;
};
