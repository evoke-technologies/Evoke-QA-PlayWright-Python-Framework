import configparser

def read_config(section, key):
    config = configparser.ConfigParser()
    config.read('config/config.properties')
    return config.get(section, key)