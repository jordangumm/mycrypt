import yaml
import os

from mycrypt import decrypt_message, decrypt_file, encrypt_message, encrypt_file 
from datautils import get_config, get_password, get_output_path, get_storage_json, get_storage_path


def save_file(input_fp):
    if not os.path.exists(input_fp): sys.exit('{} does not exist!'.format(input_fp))
    output_fp = os.path.join(get_storage_path(), input_fp.split('/')[-1])
    while os.path.exists(output_fp):
        output_fp = output_fp + '~'
    encrypt_file(input_fp, os.path.join(get_storage_path(), input_fp.split('/')[-1]))


def restore_file(file_name, output_fp=None):
    input_fp = os.path.join(get_storage_path(), file_name)
    if not os.path.exists(input_fp): sys.exit('{} does not exist!')
    if not output_fp: output_fp = file_name # write to active directory
    decrypt_file(input_fp, output_fp)


def save_message():
    pass

def restore_message():
    pass
