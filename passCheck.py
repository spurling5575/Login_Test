admin_pswd = 'shiitake'
print('パスワードを入力してください')
pswd = input()

if admin_pswd == pswd:
    print('ようこそ！')
else:
    print('パスワードが違います')