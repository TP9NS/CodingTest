function solution(arr) {
  const result = [];
  let prev = null;

  for (let i = 0; i < arr.length; i++) {
    const cur = arr[i];
    if (cur !== prev) {
      result.push(cur);
      prev = cur;
    }
  }
  return result;
}
