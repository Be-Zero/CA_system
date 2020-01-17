import rsa


def read_privkey(privkey_path):
    with open(privkey_path, 'rb') as privfile:
        p = privfile.read()
    privkey = rsa.PrivateKey.load_pkcs1(p)
    return privkey


def read_pubkey(privkey_path):
    with open(privkey_path, 'rb') as privfile:
        p = privfile.read()
    privkey = rsa.PublicKey.load_pkcs1(p)
    return privkey


# 生成密钥
def creat_key(Len):
    pubkey, privkey = rsa.newkeys(Len)
    pub = pubkey.save_pkcs1()
    with open('data/CApubkey.pem', 'wb+')as f:
        f.write(pub)
    pri = privkey.save_pkcs1()
    with open('data/CAprivkey.pem', 'wb+')as f:
        f.write(pri)
    return pubkey


# rsa加密
def rsaEncrypt(text, pubkey):
    text = rsa.encrypt(text, pubkey)
    return text


# rsa解密
def rsaDecrypt(text, privkey):
    text = rsa.decrypt(text, privkey)
    return text
