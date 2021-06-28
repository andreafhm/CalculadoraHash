
import md5


trans_5C = bytearray((x ^ 0x5c) for x in range(256))
trans_36 = bytearray((x ^ 0x36) for x in range(256))
blocksize = md5().block_size # 64

def hmac_md5(key, msg):
    if len(key) > blocksize:
        key = md5.MD5(key).digest()
    key = key + bytearray(blocksize - len(key))
    o_key_pad = key.translate(trans_5C)
    i_key_pad = key.translate(trans_36)
    return md5.MD5(o_key_pad + md5.MD5(i_key_pad + msg).digest())