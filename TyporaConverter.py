# 이 파일을 변환파일(.md)과 같은 폴더에 위치시킬 것
# typora에서 이미지 상대경로 설정 및 저장위치 asset으로 설정
# 실행 후 (ctrl + F5) 텍스트명 입력

# input file_name
input_name = input()
file_name = "./" + str(input_name) +".md"

#read file
readFile = open(file_name, "r", encoding='UTF8')
contents = readFile.readlines()

# write file
writeFile = open(file_name, "w", encoding='UTF8')
for i in range(len(contents)):
    text = contents[i]
    if text[0:7] == '![image' :
        split_text = text.split(']')
        new_text = "<img src='" + split_text[1][1:-2] +"'/>" 
        writeFile.write(new_text)
    else:
        writeFile.write(text)
readFile.close()
writeFile.close()

print("complete change file")
