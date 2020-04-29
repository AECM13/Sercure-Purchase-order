from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
import datetime

#file to verify
order='PurchaseOrder.docx'

#sign verification
def sign_verification(hash_to_verify,signature,pub_key):
    check = PKCS1_v1_5.new(pub_key).verify(hash_to_verify,signature)
    if check == True:
        print("The signature is valid.")
    else:
        print("The signature is not valid.")

#import timestamp of file signing
def timestamp_import():
    f = open('time.txt','rb')
    time = f.read()
    f.close()
    return time

#import signature for verification
def signature_import(sig_file):
    f = open(sig_file,'rb')
    signature = f.read()
    f.close()
    return signature

#import public key
def pub_key_import(pub_file):
    f = open(pub_file,'r')
    pub_key = RSA.importKey(f.read())
    f.close()
    return pub_key

#create a hash out of a file and add timestamp
def hash_generator(order):
    with open(order, 'rb') as f:
        fb = f.read()
        file_hash =SHA512.new(fb)
        file_hash.update(timestamp_import())
        f.close()
        return file_hash

def main():
    file_hash = hash_generator(order)
    signed = signature_import("signature.txt")
    mypubkey = pub_key_import("mypubkey.pem")
    sign_verification(file_hash,signed,mypubkey)

main()
