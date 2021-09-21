build:
	$(CC) quiz_de.c -o quiz_de

dist: build
	strip quiz_de
