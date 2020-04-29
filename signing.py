from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
import datetime


order='PurchaseOrder.docx'

#create a hash out of a file and add timestamp
def hash_generator(order):
    with open(order, 'rb') as f:
        fb = f.read()
        file_hash =SHA512.new(fb)
        file_hash.update(time_stamp())
        f.close()
        return file_hash

#create private and public key and export public key_pair
def key_generation():
    key_pair = RSA.generate(bits=2048)
    pubKey = key_pair.publickey()
    f = open('mypubkey.pem','wb')
    f.write(pubKey.exportKey('PEM'))
    f.close()
    return key_pair

#create and export timestamp
def time_stamp():
    time_now = str(datetime.datetime.now())
    time_now = bytes(time_now,'utf-8')
    f = open('time.txt','wb')
    f.write(time_now)
    f.close()
    return time_now

#sign hash with the timestamp
def sign_file(hash_to_sign,prv_key):
    signer = PKCS1_v1_5.new(prv_key)
    signature = signer.sign(hash_to_sign)
    f = open('signature.txt','wb')
    f.write(signature)
    f.close()
    return signature


def main():
    file_hash = hash_generator(order)
    signat = sign_file(file_hash,key_generation())
    print("The file is signed")
    print("The signature, time of signature and public key were exported")

main()
