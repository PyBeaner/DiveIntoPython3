__author__ = 'PyBeaner'

def to_json(pyobj):
    if isinstance(pyobj,bytes):
        return {
            "__class__":"bytes",
            "__value__":list(pyobj)
        }

    if isinstance(pyobj,tuple):
        return {
            "__class__":"tuple",
            "__value__":list(pyobj)
        }
    raise TypeError(repr(pyobj) + ' is not JSON serializable')