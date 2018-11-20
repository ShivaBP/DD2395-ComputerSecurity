main: main.c
	gcc -O0 -ggdb -o main main.c -fno-stack-protector

attack: main
	./solution3.py > text; xargs --null < text -I{} ./main {} hello
clean:
	rm main
