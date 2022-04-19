#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  int i = 0;
  int a;
  pid_t r; // pid_t 구조체 : 프로세스 고유의 id 값을 담기 위한 전용 구조체
  char *args[3] = {"a.out", "1", NULL};

  if(argc < 2) {
    printf("missing argument \n");
    exit(-1);
  }

  a = atoi(argv[1]);
  if(a == 1) {
    printf("bye-child\n");
    exit(0);
  }

  printf("hello\n");
  for(i = 0; i < 2; i++) {
    r = fork();
    if(r == 0) {
      printf("c%d\n", i);
    } else {
      printf("x%d\n", i);
      wait;
      execve("./a.out", args, NULL);
      printf("y%d\n", i);
    }
  }
  printf("bye-end\n");
  exit(0);
}

