def read_file(file_name):
    f = open(file_name)
    result = f.read()
    return result


# 读取人物名字
# fName = open('./test_1st/name.txt')
# data = fName.read()
data = read_file('./test_1st/name.txt')
print(data)

# 读取武器名字
# fName2 = open('./test_1st/weapon.txt')
# # data2 = fName2.read()
# # data2 = readFile('./test_1st/weapon.txt')
# # print(data2)
#
# i = 1
# for line in fName2.readlines():
#     if i % 2 == 1:
#         print(line.strip('\n'))
#     i += 1

# fSanguo = open('./test_1st/sanguo.txt',encoding='GB18030')
# print(fSanguo.read().replace('\n',''))
