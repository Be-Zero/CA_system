import os, RSA, function, config


def autograph():
    print('请输入姓名：', end='')
    name = input()
    print('请输入用户私钥文件路径：', end='')
    privkey_path = input()
    CApubkey = RSA.creat_key(5120)
    text = function.read_file(privkey_path)
    text = RSA.rsaEncrypt(text, CApubkey)
    function.save_file(config.certificate + name + '.pem', text)
    print('CA私钥文件路径为：', config.CAprivkey_path)
    print('申请认证成功！')

def authenticate():
    print('请输入姓名：', end='')
    name = input()
    print('请输入CA私钥文件路径：', end='')
    CAprivkey_path = input()
    if os.path.exists(config.certificate + name + '.pem'):
        CAprivkey = RSA.read_privkey(CAprivkey_path)
        text = function.read_file(config.certificate + name + '.pem')
        text = RSA.rsaDecrypt(text, CAprivkey)
        function.save_file(config.certificate + name + '.pem', text)
        print('认证成功！')
    else:
        print('认证失败！')


def eliminate():
    print('请输入姓名：', end='')
    name = input()
    if os.path.exists(config.certificate + name + '.pem'):
        function.Delete(config.certificate + name + '.pem')
        function.Delete(config.CApubkey_path)
        function.Delete(config.CAprivkey_path)
        print('吊销证书成功！')
    else:
        print('吊销证书失败！')


def Encryption():
    print('请输加密文件路径：', end='')
    file_path = input()
    print('请输入用户公钥文件路径：', end='')
    pubkey_path = input()
    pubkey = RSA.read_pubkey(pubkey_path)
    text = function.read_file(file_path)
    text = RSA.rsaEncrypt(text, pubkey)
    function.save_file(file_path, text)
    print('文件加密成功！')


def Decryption():
    print('请输入姓名：', end='')
    name = input()
    print('请输解密文件路径：', end='')
    file_path = input()
    privkey_path = config.certificate + name + '.pem'
    privkey = RSA.read_privkey(privkey_path)
    text = function.read_file(file_path)
    text = RSA.rsaDecrypt(text, privkey)
    function.save_file(file_path, text)
    print('文件解密成功！')


def Exit():
    os._exit(1)
