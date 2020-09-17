import os
path = 'text.txt'
with open('text.txt','w') as writer:
    w = writer.write('hi ayub')
    if os.path.exists('text.txt'):
        writer.close()
        with open(path,'r') as reader:
            print(reader.read())