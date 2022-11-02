import hashlib

admin_hs = "70fdc61e86c7b376d488ae331f093c9676158cbe80d7d77ed38c98a130a84595"

print('パスワードを入力してください')
pswd = input()
hs = hashlib.sha256(pswd.encode()).hexdigest()

if admin_hs == hs:
    print('ようこそ！')
else:
    print('パスワードが違います')