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

# 篩選留言內有包含 good 的筆數
good = []
for d in data:
    if 'good' in d: # 如果 good 有在 d 裡面則為 True
        good.append(d)
print('一共有', len(good), '筆留言提到 good')
print(good[0])

# 篩選 good 字串功能, 清單快寫法(list comprehension)

#              運算          變數       清單           篩選條件
#               ↓             ↓          ↓                ↓
# output = [(number-1) for number in reference if number % 2 == 0]

#       d for d 的 前面的 d 是 good.append(d) 的 d
#       ↓
good = [d for d in data if 'good' in d]

# bad = []                            # 
# for d in data:                      #
#     bad.append('bad' in d)          #

# bad = ['bad' in d for d in data] # 53 - 55 快寫法 list comprehension
# print(bad[0])
# print('一共有', len(bad), '筆留言提到 bad')


bad = []                            # 
for d in data:                      #
    bad.append(d)                   #

# bad = ['bad' in d for d in data] # 53 - 55 快寫法 list comprehension
bad = [d for d in data if 'bad' in d] # 53 - 55 快寫法 list comprehension

print(bad[0])
print('一共有', len(bad), '筆留言提到 bad')
