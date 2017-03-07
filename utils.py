import re

p = r"M[ri]s*\.";
pattern = re.compile(p)

def NameChange(name):
       arr = pattern.findall(name);
       l = len(arr);
       if l == 0:
              return 3;
       elif arr[0] == 'Mr.':
              return 0;
       elif arr[0] == 'Mrs.':
              return 1;
       elif arr[0] == 'Miss.':
              return 2;

name = 'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)';

print(NameChange(name));
