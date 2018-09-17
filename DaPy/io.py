from os import path
from string import atof, atoi, strip
from distutils.util import strtobool

__all__ = ['read', 'encode', 'str2value', 'parse_addr']

TRANS_FUN_SET = {float: atof,
                 int: atoi,
                 bool: strtobool,
                 str: strip}

def read(addr, dtype='col', **kward):
    '''dp.read('file.xlsx') -> return DataSet object
    '''
    from core import DataSet
    data = DataSet()
    data.read(addr, dtype, **kward)
    return data

def save(addr, data, encode='utf-8'):
    '''dp.save('file.xlsx', [1,2,3,4]) -> save list into file
    '''
    from core import DataSet
    data = DataSet(data)
    data.save(addr, encode)

def encode(code='cp936'):
    import sys
    stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
    reload(sys)
    sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde
    sys.setdefaultencoding(code)
    return

def str2value(value, prefer_type=None):
    if prefer_type is str:
        return value

    elif value.isdigit() or value[1:].isdigit():
        if prefer_type is float:
            return atof(value.replace(',', ''))
        return atoi(value)
    
    elif value.count('.') == 1:
        return atof(value.replace(',', ''))

    elif prefer_type is bool:
        try:
            return strtobool(value)
        except ValueError:
            pass
        
    return strip(value)

def parse_addr(addr):
    file_path, file_name = path.split(addr)
    if file_name.count('.') > 1:
        file_base = '.'.join(file_name.split('.')[:-1])
        file_type = file_name.split('.')[-1]
    else:
        file_base, file_type = file_name.split('.')
    return file_path, file_name, file_base, file_type
