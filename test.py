import md4

test_vector = {
    b'a': 'bde52cb31de33e46245e05fbdbd6fb24',
    b'abc': 'a448017aaf21d8525fc10ae87aa6729d',
    b'message digest': 'd9130a8164549fe818874806e1c7014b',
    b'abcdefghijklmnopqrstuvwxyz': 'd79e1c308aa5bbcdeea8ed63df412da9',
    b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789': '043f8582f241db351ce627e153e7f0e4',
    b'12345678901234567890123456789012345678901234567890123456789012345678901234567890': 'e33b4ddc9c38f2199c3e7b164fcc0536' }
for m, h in test_vector.items():
    print("Holaa"+md4.MD4(m).hexdigest())


