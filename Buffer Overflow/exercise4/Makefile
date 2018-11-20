all: main shell

main: main.c
	gcc -fno-stack-protector -z execstack -O0  -ggdb -o main main.c

shell:
	python shell.py

attack: main shell
	./solution4.py > text; ./main < text
