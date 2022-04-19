#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

#define MAX_COUNT 200

void ChildProcess (void);
void ParentProcess (void);

int main(void) {
    pid_t pid;
    pid = fork();

    if (pid==0)
       ChildProcess();
    else
       ParentProcess();
}

void ChildProcess(){
     int i;
     pid_t pid = getpid();

     for(i=1 ; i<=MAX_COUNT; i++)
        printf("  This line is from child process(PID:%d), value = %d\n",pid,i);
     printf("*** Child Process is done ***\n");
}

void ParentProcess(){
     int i;
     pid_t pid = getpid();

     for(i=1 ; i<=MAX_COUNT;i++)
         printf("This line is from parent process(PID:%d), value = %d\n",pid,i);
     printf("*** Parent is done ***\n");
}
