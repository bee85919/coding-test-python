const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

const input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n")
  .slice(1)
  .map((i) => i.split(" ").map((i) => Number(i)));

function solution(testCase) {
  return testCase.sort((a, b) => {
    if (a[0] === b[0]) {
      return a[1] - b[1];
    }
    return a[0] - b[0];
  });
}

const result = solution(input)
  .map((i) => i.join(" "))
  .join("\n");

console.log(result);
