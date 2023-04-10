// Refactor it to use the rest operator & an arrow function:
const filterOutOdds = (...nums) => nums.filter((num) => num % 2 === 0);

// findMin
const findMin = (...nums) => nums.reduce((prev, curr) => (curr < prev ? curr : prev), nums[0]);

// mergeObjects
const mergeObjects = (obj1, obj2) => ({ ...obj1, ...obj2 });

// doubleAndReturnArgs
const doubleAndReturnArgs = (arr, ...args) => [...arr, ...args.map((num) => num * 2)];

// removeRandom
const removeRandom = (items) => {
  const i = Math.floor(Math.random * items.length);
  return [...items.slice(0, i), ...items.slice(i + 1)];
};

// extend
const extend = (arr1, arr2) => [...arr1, ...arr2];

// addKeyVal
const addKeyVal = (obj, key, val) => ({ ...obj, [key]: val });

// removeKey
const removeKey = (obj, key) => {
  ({ [key]: undefined, ...obj } = obj);
  return obj;
};

// combine
const combine = (obj1, obj2) => {
  return { ...obj1, ...obj2 };
};

// update
const update = (obj, key, val) => ({ ...obj, [key]: val });
