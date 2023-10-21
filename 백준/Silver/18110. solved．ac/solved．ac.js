const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs
    .readFileSync(filePath)
    .toString()
    .trim()
    .split("\n")
    .slice(1)
    .map(Number);

function my_round(x) {
    return (x - Math.floor(x) >= 0.5) ? Math.floor(x) + 1 : Math.floor(x);
}

function solution(testCase) {
    const n = testCase.length;
    if (n === 0) return 0;

    const sortedOpinions = testCase.sort((a, b) => a - b);
    const average = my_round(n * 0.15);

    const idxStart = average;
    const idxEnd = n - average;
    let sum = 0;  
    for (let i = idxStart; i < idxEnd; i++) {
        sum += sortedOpinions[i];
    }

    return my_round(sum / (n - average * 2));
}

console.log(solution(input));