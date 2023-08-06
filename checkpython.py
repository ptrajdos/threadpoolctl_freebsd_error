from distutils import sysconfig
if __name__ == '__main__':

    print("LDSHARED:", sysconfig.get_config_var('LDSHARED'))
    print("CC: ", sysconfig.get_config_var('CC'))
    print("CXX: ", sysconfig.get_config_var('CXX'))
