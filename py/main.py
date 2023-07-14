import A  # 並不會重複執行
from A import A
from A import A as AA
from B import B

print(A == AA)# True
print(A == B)# True
print(A is AA)# True
print(A is B)# True

from HaveStatus import count
from HaveStatus import count as countOther
from HaveStatus import plusOne
from HaveStatus import plusOne as plusOneOther
from HaveStatus import printCount

printCount() # 0

# not like js, no TypeError: Assignment to constant variable.
count = 100

printCount() # 0

print(count) # 100
plusOne()
printCount() # 1
print(count) # 100
plusOne()
printCount() # 2
print(count) # 100

print(countOther) # 0
plusOneOther()
printCount() # 3
print(countOther) # 0
plusOneOther()
printCount() # 4
print(countOther) # 0

print(count == countOther) # False

from HaveStatus import count as countFinal

print(countFinal) # 4

from HaveStatus import personA
from HaveStatus import personA as personAA

print(personA == personAA) # True
print(personA is personAA) # True

# not like js, no TypeError: Assignment to constant variable.
personA = { 'name': 'personA' }

print(personA == personAA) # True
print(personA is personAA) # False

print('main.py finished')
