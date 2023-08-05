
.PHONY: all clean

example4:example4.c
	gcc -Wl,--export-dynamic ./example4.c -o example4 -ldl -g
