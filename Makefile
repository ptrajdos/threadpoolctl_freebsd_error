CC=clang
.PHONY: all clean

example4:example4.c
	${CC} -Wl,--export-dynamic ./example4.c -o example4 -ldl -g -D_GNU_SOURCE

example3:example3.c
	${CC} -Wl,--export-dynamic ./example3.c -o example3 -ldl -g -D_GNU_SOURCE
