import yaml
import os


def get_config_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                              'data', 'config.yml')


def get_config():
    """ Return config as dict """
    return yaml.load(open(get_config_path()).read())


def save_config(config):
    yaml.dump(config, get_config_path())


def get_password():
    """ Retreive password from configuration file """
    def get_new_password():
        chars = '!@#$%^&*()'
        password = ''.join(random.choice(string.ascii_letters + string.digits + chars) for _ in range(24))
        print 'Store encryption password for recovery purposes:\n{}'.format(password)
        return password

    config = get_config()
    if 'password' not in config.keys():
        password = get_new_password()
        config['password'] = password
        save_config(config)
    return config['password']


def get_output_path():
    """ Return String output path

    The output path is used by mycrypt to store encrypted data for fast
    retrieval and for potential backup in case of device borking/malfunction.

    It is recommended that this path be part of a mount dedicated to backup.
    This can be a directory managed by Dropbox, Sia, Storj, etc.
    """
    config = get_config()
    if 'output_path' not in config.keys():
        path = 'asdf;lkj'
        while not os.path.exists(path):
            path = raw_input('Enter file path to save encryption information: ')
        set_output_path(path)
        return path
    return config['output_path']


def get_storage_json():
    """ Return dictionary loaded from MyCrypto JSON """
    json_fp = os.path.join(get_output_path(), 'mycrypto.json')
    if not os.path.exists(json_fp): json.dump({},json_fp)
    return json.loads(json_fp)


def get_storage_path():
    """ Return path to where encrypted files are stored """
    return os.path.join(get_output_path(), 'files')
