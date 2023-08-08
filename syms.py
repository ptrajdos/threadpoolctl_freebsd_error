import ctypes
import os
import sys
from ctypes.util import find_library

_RTLD_NOLOAD = os.RTLD_NOLOAD
_SYSTEM_UINT = ctypes.c_uint64 if sys.maxsize > 2 ** 32 else ctypes.c_uint32
_SYSTEM_UINT_HALF = ctypes.c_uint32 if sys.maxsize > 2 ** 32 else ctypes.c_uint16

class _dl_phdr_info(ctypes.Structure):
        _fields_ = [
        ("dlpi_addr", _SYSTEM_UINT),  # Base address of object
                                ("dlpi_name", ctypes.c_char_p),  # path to the library
                                        ("dlpi_phdr", ctypes.c_void_p),  # pointer on dlpi_headers
                                                ("dlpi_phnum", _SYSTEM_UINT_HALF),  # number of elements in dlpi_phdr
                                                    ]

def match_library_callback(info, size, data):
    print("match_library_callback")
                    # Get the path of the current library
    filepath = info.contents.dlpi_name
    if filepath:
        filepath = filepath.decode("utf-8")
        print(filepath)

                                                # Store the library controller if it is supported and selected
     #   self._make_controller_from_path(filepath)
        return 0

def call_dl():
    so = b'./test.so'
    parent = ctypes.CDLL(None)
    
    dlopen = parent.dlopen
    dlopen.restype = ctypes.c_void_p

    dlsym = parent.dlsym
    dlsym.restype = ctypes.c_void_p

    # lib = dlopen(so, os.RTLD_LOCAL)
    # print("LIB:", lib)

    # foo = parent.dlsym(lib,b'foo')
    # print("FOO: ", foo)

    RTLD_DEFAULT=-2
    dl_iterate_phdr_ptr = dlsym(RTLD_DEFAULT, b'dl_iterate_phdr')
    # it is a pointer probably

    print("XX",dl_iterate_phdr_ptr)

    #CALL
    FUNKY = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

    c_func_signature = ctypes.CFUNCTYPE(
                        ctypes.c_int,  # Return type
                                    ctypes.POINTER(_dl_phdr_info),
                                                ctypes.c_size_t,
                                                            ctypes.c_char_p,
                                                            )

    FUNKY.argtypes = [ c_func_signature, ctypes.c_void_p ]
    #FUNKY.restype = ctypes.c_int
    c_match_library_callback = c_func_signature(match_library_callback)
    data = ctypes.c_char_p(b"")

    #libc_name = find_library("c")
    #print("libc_name="+libc_name)
    #libc = ctypes.CDLL(libc_name, mode=_RTLD_NOLOAD)

    #x = libc.dl_iterate_phdr
    #print("libc x:", x)
    #x(c_match_library_callback, data)

    #v = ctypes.CDLL._FuncPtr()

    FUNKY(dl_iterate_phdr_ptr)(c_match_library_callback, data) # failing line
    

if __name__ == '__main__':
    call_dl()
