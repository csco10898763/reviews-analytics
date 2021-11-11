# 讀取檔案

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 10000 == 0:
            print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')
# print('-------------------')
# print(data[0])
# print('-------------------')
# print(data[1])
sum_len = 0
for d in data:
    sum_len += len(d)
    print(sum_len)

print('留言的平均長度為', sum_len / len(data))


# 篩選留言字數低於 100 的
new = []
for d in data:
    if len(d) < 100:
        new.append(d)

print('留言字數低於 100 的總共有', len(new), '筆資料')
print(new[0])
print(new[1])