d = {
    'a:': '我',
    'b:': '是',
    'c:': '中',
    'd:': '国',
    'e:': '人'
}


with open(r'C:\workspace\iDEAS_sit\case\test_case\bb.txt', 'w', encoding='utf-8') as f:
    for key, value in d.items():
        f.writelines(key+value)
        f.write('\n')
