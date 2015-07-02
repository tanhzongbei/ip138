#coding:utf8
"""
Created on Jun 18, 2014

@author: ilcwd
"""
import logging.config
import logging
import os

import yaml

from testIP.core import application, C, misc

_parent = os.path.join(os.path.dirname(__file__), 'deployment')
logging_config_path = os.path.join(_parent, 'logging.yaml')
app_config_path = os.path.join(_parent, 'config.json')

if __name__ != '__main__':
    with open(logging_config_path, 'r') as f:
        logging.config.dictConfig(yaml.load(f))

C.load_json_config(app_config_path)

# register APIs after `C.load_config()`
from testIP.views import default
from testIP.apis import (
                        version,
                        getip
                        )
application.register_blueprint(version.app, url_prefix='/testIP/version')
#application.register_blueprint(getip.app, url_prefix='/testIP/ip')

def main():
    """Debug Mode"""
    import sys
    _logger = logging.getLogger()
    _logger.setLevel(logging.DEBUG)
    _logger.addHandler(logging.StreamHandler(stream=sys.stdout))

    host, port = '0.0.0.0', 8080
    application.run(host, port, debug=True, use_reloader=False)


if __name__ == '__main__':
    main()
