import os.path

if os.path.isfile('myfile.txt'):
    print('file存在')
else:
    print('file不存在')
    
fo=open('myfile.txt','w')
fo.write('you')
fo.close()

fo=open('myfile.txt','r')
theFile=fo.read()
print(theFile)
fo.close()

fo=open('myfile.txt','a')

fo.write('and me')
print('and me')
fo.close()
