current_space = '::'
data = open('Links.txt','r').read()
d_lines = data.splitlines()
for line in d_lines:
   if current_space not in line:
        if line.strip():
            print(line)