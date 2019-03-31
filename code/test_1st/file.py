file1 = open('test.txt','w')
file1.write('Hello world!')
file1.close()

file1 = open('test.txt','r')
print(file1.read())
file1.close()

file1 = open('test.txt','a')
file1.write('Python')
file1.close()

file1 = open('test.txt','r')
print(file1.read())
file1.close()

