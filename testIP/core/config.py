# coding: utf8
#
# testIP - config
# 
# Author: ilcwd 
# Create: 15/5/11


import json


def _dict_get_key_by_path(dictobj, path):
    def _get_value_by_path_list(dobj, path_list):
        if not path_list:
            return dobj

        if not isinstance(dobj, dict):
            raise TypeError("expect a dict, but `%s`" % (type(dobj)))

        key = path_list.pop(0)
        return _get_value_by_path_list(dobj[key], path_list)

    return _get_value_by_path_list(dictobj, path.split('.'))


class ConfigValue(object):
    def __init__(self, path):
        self.path = path


class ConfigOptionalValue(ConfigValue):
    def __init__(self, path, option):
        super(ConfigOptionalValue, self).__init__(path)
        self.option = option


class _Config(object):
    """
    configuration utils.
    """

    def load_json_config(self, config_file):
        with open(config_file, 'r') as f:
            dictconfig = json.loads(f.read())

        self.load_dict_config(dictconfig)

    def load_dict_config(self, dictconfig):
        for k in dir(self):
            v = getattr(self, k)
            if not isinstance(v, ConfigValue):
                continue

            try:
                value = _dict_get_key_by_path(dictconfig, v.path)
            except KeyError:
                if isinstance(v, ConfigOptionalValue):
                    value = v.option
                else:
                    raise

            setattr(self, k, value)


class _C(_Config):
    """
    Global configuration for application.
    """

    # Define your attributes here first.
    DEBUG = ConfigOptionalValue('debug', False)

    MYSQL_MYDB_PARAMETERS = ConfigValue('mysql.mydb')

    BAIDU_AK = ConfigValue('BAIDU_AK')


C = _C()


def main():

    d = {
        'debug': True,
        'mysql': {
            'mydb': {
                'host': '10.0.0.1',
                'user': 'python'
            }
        }
    }

    C.load_dict_config(d)
    print C.DEBUG
    print C.MYSQL_MYDB_PARAMETERS


if __name__ == '__main__':
    main()