// ES2015 Arrow Functions Shorthand
function double(arr) {
  return arr.map((val) => val * 2);
}

// Refactor the following function to use arrow functions:
const squareAndFindEvens = (numbers) => {
  const squares = numbers.map((num) => num ** 2);
  const evens = squares.filter((square) => square % 2 === 0);
  return evens;
};
