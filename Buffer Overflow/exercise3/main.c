#include <stdio.h>
#include <string.h>

char * pwd = "pwd0";

void print_my_pwd() {
  printf("your pwd is: %s\n", pwd);
}

int check_user(char * uname, char * upwd) {
  char name[8];
  strcpy(name, uname);
  
  if (strcmp(pwd, upwd)) {
    printf("non authorized\n");
    return 1;
  }
  printf("authorized\n");
  print_my_pwd();
  return 0;
}

int main(int argc, char ** argv) {
  char name[8];

  if (argc < 3) {
    printf("Use ./main <user> <password>\n");
    return 1;
  }

  printf("Start\n");
  printf("Hello %s\n",argv[1]);

  check_user(argv[1], argv[2]);

  printf("End\n");
  return 0;
}
