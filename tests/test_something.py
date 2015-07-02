# coding: utf8
#
# testIP - test_something
# 
# Author: ilcwd 
# Create: 15/5/11
#


import base


def test_version():
    versionInfo = base.rpc('/testIP/version', {})
    assert isinstance(versionInfo, dict), versionInfo
    assert 'version' in versionInfo, versionInfo


def test_IP():
    res = base.rpc('/testIP/ip138')
    print res

def main():
    test_IP()


if __name__ == '__main__':
    main()