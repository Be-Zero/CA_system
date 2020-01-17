import demo

operator = {'1': demo.autograph, '2': demo.authenticate, '3': demo.eliminate, '4': demo.Encryption, '5': demo.Decryption, '0': demo.Exit}
while 1:
    print('------1.autograph\n------2.authenticate\n------3.eliminate\n------4.Encryption\n------5.Decryption\n------0.exit\n\t请输入：', end='')
    option = input()
    operator.get(option)()
    print()
