#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  /*
    main 함수의 매개변수 
    - int argc : main 함수에 전달되는 정보의 개수
    - char **argv : main 함수에 전달되는 정보, 문자열 타입의 배열 형식, 첫 번째 문자열은 프로그램의 실행경로로 고정
  */
  // for (int i = 0; i < argc; i++) // 옵션의 개수만큼 반복
  // {
  //   printf("%d : %s\n",argc, argv[i]); // 옵션 문자열 출력
  // }

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
      wait(NULL);
      execve("./a.out", args, NULL);
      printf("y%d\n", i);
    }
  }
  printf("bye-end\n");
  exit(0);
}

