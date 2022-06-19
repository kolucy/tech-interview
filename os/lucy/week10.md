# Main Memory

▪ A process is a program in execution
- a set of instructions kept in a *main memory*

▪ Memory
- 구성
    - a large *array of bytes*
    - each with its own *address*
- CPU는 program counter를 사용해 메모리에서 명령(instructions)을 가져온다(fetch)
- instructions은 메모리에 load 또는 store 할 수 있다

▪ Memory Space
- each process has a *separate memory space*
- A pair of registers: **base register** and **limit register**
    - legal address space를 정의

▪ Protection of memory space
- CPU 하드웨어를 사용하여 메모리 공간 보호
- user mode에서 생성된(generated) 모든 주소를 register와 비교
- CPU가 address access할 때 base register보다는 크거나 같고, base+limit 보다는 작을 때 메모리 엑세스 허용

## Address Binding