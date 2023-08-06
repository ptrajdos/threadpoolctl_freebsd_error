#include <link.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

/**
 * mwe.c
 * Compile via: 
 * gcc -rdynamic mwe.c -o mwe -g -D_GNU_SOURCE
 * or
 * clang -rdynamic mwe.c -o mwe -g -D_GNU_SOURCE 
*/
static int callback(struct dl_phdr_info *info, size_t size, void *data) {
	//A simple callback function
 	printf("Name: \"%s\" (%d segments)\n", info->dlpi_name, info->dlpi_phnum);
 	return 0;
}

typedef int (*lib_func)(int (*callback)(struct dl_phdr_info *, size_t, void *), void* data);

int call_from_libc(){
	/**
	 * Calls dl_iterate_phdr indirectly by loading libc via dlopen
	 * */
	void     *handle  = NULL;
	lib_func  func    = NULL;
	handle = dlopen("/lib/libc.so.7",RTLD_NOW|RTLD_NOLOAD);// Put the name of your libc shared object
	if (handle == NULL){
		fprintf(stderr, "Unable to open lib: %s\n", dlerror());
		return -1;
	 }
	func = dlsym(handle, "dl_iterate_phdr");

	if (func == NULL) {
		fprintf(stderr, "Unable to get symbol\n");
		return -1;
	}

	func(callback, NULL);
	return 0;
}

int main(int argc, char *argv[]) {
	printf("Direct call:\n");
 	dl_iterate_phdr(callback, NULL);//It works

	printf("Indirect call:\n");
 	call_from_libc();//It causes 'ld-elf.so.1: Can't find module with TLS index 1'

 	exit(EXIT_SUCCESS);
}
