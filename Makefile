
.PHONY: all clean

example4:example4.c
	gcc -Wl,--export-dynamic ./example4.c -o example4 -ldl -g

example3:example3.c
	gcc -Wl,--export-dynamic ./example3.c -o example3 -ldl -g
