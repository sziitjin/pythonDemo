with open('jin.log','wt') as out_file:
    out_file.write('hello jin. \nmy name is suke.')

with open('jin.log','rt') as in_file:
    text = in_file.read()

print(text)