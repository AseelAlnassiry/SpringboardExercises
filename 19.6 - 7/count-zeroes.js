function countZeroes(arr) {
  let l = 0;
  if (arr[l] === 0) return arr.length;
  let r = arr.length - 1;
  let m = Math.floor((r + l) / 2);
  while (l <= r) {
    m = Math.floor((r + l) / 2);
    if (arr[m] === 0 && arr[m - 1] && arr[m - 1] === 1) return arr.length - m;
    else if (arr[m] === 1) l = m + 1;
    else r = m - 1;
  }

  return 0;
}

module.exports = countZeroes;

