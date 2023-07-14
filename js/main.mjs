import './A.mjs';
import './A.mjs';
import './A.mjs'; // 並不會重複執行

import A from './A.mjs';
import AA from './A.mjs';
import B from './B.mjs';

console.log(A === AA); // true
console.log(A === B); // true

import { count, plusOne } from './HaveStatus.mjs';
import { count as countOther, plusOne as plusOneOther } from './HaveStatus.mjs';

// TypeError: Assignment to constant variable.
// count = 100;

console.log(count); // 0
plusOne();
console.log(count); // 1
plusOne();
console.log(count); // 2

console.log(countOther); // 2
plusOneOther();
console.log(countOther); // 3
plusOneOther();
console.log(countOther); // 4

console.log(count === countOther); // true

import { personA } from './HaveStatus.mjs';
import { personA as personAA } from './HaveStatus.mjs';

// TypeError: Assignment to constant variable.
// personA = { name: 'new personA' };

console.log(personA === personAA); // true

console.log('main.mjs finished');
