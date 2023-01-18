password = 'a123456'
i = 3
while i > 0:
     j = input('请输入密码：')
     if j == password:
         print('登入成功！')
         break
     else:
         print('密码错误！')
         i = i - 1
         if i > 0:
            print('还有',i,'次机会')
         else:
         	print('没机会尝试了！要锁账号了！')


      
         
