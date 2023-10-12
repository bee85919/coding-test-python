const arr = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const sta = [];
const ans = [];

const len = arr.shift();

for (let i = 0; i < len; i++) {        
    switch(arr[i]) {
        case 'pop': 
          ans.push(sta.pop() || -1);
          break;

        case 'size': 
          ans.push(sta.length);
          break;

        case 'empty': 
          ans.push(sta[0] ? 0 : 1);
          break;

        case 'top': 
          ans.push(sta[sta.length - 1] || -1);
          break;

        default: 
          sta.push(arr[i].split(" ")[1]);
          break;
    }
}

console.log(ans.join('\n'));