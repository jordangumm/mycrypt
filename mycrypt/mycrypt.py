from sys import exit
from simplecrypt import encrypt, decrypt
from datautils import get_password


def decrypt_message(message):
    """ Returns decrypted String message """
    if type(message) != type(''): exit('Message not of type String')
    password = get_password()
    return decrypt(password, message)


def decrypt_file(input_fp, output_fp):
    """ Encrypt input file """
    if not output_fp: output_fp = input_fp + '.unencrypted'
    password = get_password()

    plaintext = decrypt(password, open(input_fp).read())
    with open(output_fp, 'w+') as output:
        output.write(plaintext)


def encrypt_message(message):
    """ Returns encrypted String message """
    if type(message) != type(''): exit('Message not of type String')
    password = get_password()
    return encrypt(password, message)


def encrypt_file(input_fp, output_fp):
    """ Encrypt input file """
    if not output_fp: output_fp = input_fp + '.myencrypt'
    password = get_password()

    ciphertext = encrypt(password, open(input_fp).read())
    with open(output_fp, 'w+') as output:
        output.write(ciphertext)
