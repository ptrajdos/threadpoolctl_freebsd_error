from distutils import sysconfig
from sys import platform
if __name__ == '__main__':

    print("Platform: ", platform)
    print("LDSHARED:", sysconfig.get_config_var('LDSHARED'))
    print("CC: ", sysconfig.get_config_var('CC'))
    print("CXX: ", sysconfig.get_config_var('CXX'))
