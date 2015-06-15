__author__ = 'PyBeaner'

import datetime

def to_json(pyobj):
    if isinstance(pyobj,bytes):
        return {
            "__class__":"bytes",
            "__value__":list(pyobj)
        }

    if isinstance(pyobj,datetime.datetime):
        return {
            "__class__":"datetime.datetime",
            "__value__":pyobj.strftime('%Y-%m-%d %H:%M:%S')
        }
    raise TypeError(repr(pyobj) + ' is not JSON serializable')

def from_json(json_obj):
    if "__class__" in json_obj:
        _class = json_obj["__class__"]
        _value = json_obj['__value__']
        if _class == "bytes":
            return bytes(_value)
        if _class == "datetime.datetime":
            return datetime.datetime.strptime(_value,'%Y-%m-%d %H:%M:%S')
    return json_obj
