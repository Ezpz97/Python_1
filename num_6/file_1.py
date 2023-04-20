import os.path

infile = open("phones.txt", 'r', encoding="UTF8")
s = infile.readline()
print(s)
s = infile.readline()
print(s)
s = infile.readline()
print(s)
infile.close()
print("")
infile2 = open("phones.txt", 'r', encoding='UTF8')
line = infile2.readline()
while line != "":
    print(line)
    line = infile2.readline()
infile2.close()

outfile = open('phones2.txt', 'w')
outfile.write('홍길동 010-1234-5678\n')
outfile.write('김철수 010-1234-5679\n')
outfile.write('김영희 010-1234-5680\n')

outfile.close()

outfile2 = open('phones2.txt', 'w')
print("")
if os.path.isfile('phones2.txt'):
    print('동일한 이름의 파일이 이미 존재합니다.')
else:
    outfile2.write('홍길동 010-1234-5678\n')
    outfile2.write('김철수 010-1234-5679\n')
    outfile2.write('김영희 010-1234-5680\n')
outfile2.close()
