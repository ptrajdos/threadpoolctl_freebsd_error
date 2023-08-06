CC=clang
EXPORT_DYNAMIC=-rdynamic
.PHONY: all clean

example4:example4.c
	${CC}  ${EXPORT_DYNAMIC} $< -o $@ -ldl -g -D_GNU_SOURCE

example3:example3.c
	${CC} ${EXPORT_DYNAMIC}  $< -o $@ -ldl -g -D_GNU_SOURCE

example2:example2.c
	${CC} ${EXPORT_DYNAMIC} $< -g -o $@ -D_GNU_SOURCE

mwe:mwe.c
	${CC} ${EXPORT_DYNAMIC} $< -g -o $@ -D_GNU_SOURCE
