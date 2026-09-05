const nums = [1, 2, 3, 4, 5];
const doubled = nums.map(x => x * 2);
const evens = nums.filter(x => x % 2 === 0);
console.log(doubled);   // 期望 [ 2, 4, 6, 8, 10 ]
console.log(evens);     // 期望 [ 2, 4 ]
