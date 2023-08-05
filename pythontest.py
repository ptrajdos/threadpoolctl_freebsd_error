from threadpoolctl import threadpool_info
from pprint import pprint
#import numpy
if __name__ == '__main__':
    #print("Hello World!")
    
    f = open("./test_file.txt", "w")
    print("XX", file=f,flush=True)
    print(threadpool_info(),file=f, flush=True)
    #threadpool_info()
