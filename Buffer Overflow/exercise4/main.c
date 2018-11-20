/* #pragma GCC diagnostic ignored "-Wdeprecated-declarations" */

#include <stdio.h>
#include <stdlib.h>

char * gets ( char * str );

char mail_body[128];

void hello() {
  char mail_subject[32];

  printf("Enter the mail subject:\n");
  gets(mail_subject);
  
  printf("Enter the mail body:\n");
  gets(mail_body);

  return;
}

int main(int argc, char** argv) {
  hello();
  printf("Sending the email\n");
}
