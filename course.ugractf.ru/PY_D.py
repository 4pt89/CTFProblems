import pwn
import re

r = pwn.remote("netcalc.course.ugractf.ru", 1337)
print(r.recv())
token = b'd02877a634130269'
r.sendline(token)

x = r.recv()
print(x)



while True:
    v = x.decode('utf-8')
    nums = re.findall(r'\d+', v)
    nums = [int(i) for i in nums]
    if 'minus' in v:
        ww = str(nums[0]-nums[1])
        r.sendline(ww.encode('utf-8'))
    elif 'plus' in v:
        ww = str(nums[0]+nums[1])
        r.sendline(ww.encode('utf-8'))
    elif 'multiply' in v:
        ww = str(nums[0]*nums[1])
        r.sendline(ww.encode('utf-8')) 
    x = r.recv()
    print(x)
