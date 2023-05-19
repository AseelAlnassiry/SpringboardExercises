function sortedFrequency(arr, t) {
  const first = findFirst(arr, t);
  if (first === -1) return -1;
  const second = findLast(arr, t);
  return second - first + 1;
}

const findFirst = (arr, t) => {
  let l = 0;
  if (arr[0] === t) return 0;
  let r = arr.length - 1;
  let m = Math.floor((l + r) / 2);
  while (l <= r) {
    m = Math.floor((l + r) / 2);
    if (arr[m] === t && arr[m - 1] && arr[m - 1] < t) return m;
    else if (arr[m] >= t) r = m - 1;
    else l = m + 1;
  }

  return -1;
};

const findLast = (arr, t) => {
  let l = 0;
  let r = arr.length - 1;
  if (arr[r] === t) return r;
  let m = Math.floor((l + r) / 2);
  while (l <= r) {
    console.log(l, m, r);
    m = Math.floor((l + r) / 2);
    if (arr[m] === t && arr[m + 1] && arr[m + 1] > t) return m;
    else if (arr[m] > t) r = m - 1;
    else l = m + 1;
  }
  return -1;
};

module.exports = sortedFrequency;
