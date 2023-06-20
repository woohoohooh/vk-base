count = 0
older = []
tmp = []
with open('old.txt', encoding='utf8') as f:
    for i in f:
        older.append(i.strip())
lst = []
with open('vk.txt', encoding='utf8') as f:
    for i in f:
        lst.append(i.strip())
for i in lst:
    for i in lst:
        if i not in older and i not in tmp:
            if count < 25:
                with open('old.txt', 'a', encoding='utf8') as f:
                    f.write(i)
                    f.write('\n')
                    count += 1
                    tmp.append(i)
                    print(i)
            break
