import re

a = 'one1two2three3'
infos = re.search('\d+',a)
print(infos)
print(infos.group())

b = '123-456-789'
new_b = re.sub('\D','',b)
print(new_b)