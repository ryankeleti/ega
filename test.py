import re
tags = []
with open("tags", 'r') as f:
  for line in f:
    line = re.sub(r",.*", "", line)
    tags.append(line)

print(len(tags))
print(len(set(tags)))


