orig_s = ''
orig_s += input('班级：')
orig_s += input('姓名：')
orig_s += ' | '
print('请在下方输入内容⬇，回车后开始转换')
orig_s += input('>>> ')

uni_s = ''
for ch in orig_s:
    if ch in '\n\t\'':
        continue
    uni_s += ch

gbk_s = list(uni_s.encode('gbk'))

# print(gbk_s)

idx = 0
codes = []
while idx < len(gbk_s):
    if gbk_s[idx] <= 0x7f:
        codes.append(gbk_s[idx] + 0xa380)
        idx += 1
    else:
        codes.append((gbk_s[idx] << 8) + gbk_s[idx+1])
        idx += 2

retstr = 'v2.0 raw\n'
for code in codes:
    retstr += '{:04x} '.format(code)

with open('out.txt', 'w') as f:
    f.write(retstr)

print('搞定！输出文件存放在当前目录下的 out.txt 中！')
