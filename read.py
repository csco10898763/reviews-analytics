# 讀取檔案

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 10000 == 0:
            print(len(data))
print('檔案讀取玩了,總共有', len(data), '筆資料')
# print('-------------------')
# print(data[0])
# print('-------------------')
# print(data[1])
