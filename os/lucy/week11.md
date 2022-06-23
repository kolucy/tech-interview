# Virtual Memory

▪ Virtual Memory
- 메모리에 완전히 적재되지 않아도 프로세스의 실행을 가능하게 하는 기술
- 프로그램은 physical memory(실제 메모리)보다 클 수 있다
- main memory를 매우 큰 storage array로 추상화(abstract)한다 -> 즉 logical(virtual) memory로 둔다
- 실행이 필요한 부분만 실제 physical memory에 옮긴다
- 위 방법을 통해 logical memory와 physical memory의 완전한 분리가 가능하다
- 파일, 라이브러리 공유 및 프로세스 생성에 효율적인 메커니즘을 제공한다
- ![virtual_memory](./virtual_memory.PNG)
- physical memory가 실제 프로세스 실행의 main memory
- backing store(주로 HDD)는 sub memory(제2저장장치)

<br>

▪ Virtual Address Space
- 프로세스가 메모리에 저장되는 방식에 대한 logical(virtual) view
- ![shared_library](./shared_library.PNG)
- 보통 주소는 0으로 시작되며, 연속 메모리에 존재
- `stack`, `heap`은 고정 크기가 아니며, 함수를 호출하면 `stack` 영역이 늘어나고, 동적 메모리 할당 시 `heap` 영역이 늘어난다
    - 이 부분을 sparse address space(성긴 주소 공간)이라고 한다
    - sparse address space의 공백은 stack이나 heap 세그먼트가 확장될 때 사용되거나 프로그램 실행 중 동적으로 라이브러리를 링크할 필요가 있을 때 사용한다
- `stack`, `heap` 공간 사이에 `shared library`가 위치해 있고, `page sharing`를 통해 2개 혹은 더 많은 프로세스끼리 파일, 메모리를 공유할 수 있다
- ![memory_space](./memory_space.png)

<br>

# Demand Paging

▪ Demand Paging
- executable program은 secondary storage(보조 기억 장치)에서 메모리로 적재되어야 실행된다(process)
- 전체 프로그램을 physical memory에 load하면 용량이 부족할 수 있기 때문에 대안이 필요 -> Demand Paging(요청 페이징)
- 실행 중에 요청이 들어올 때만 필요한 페이지를 load한다
- 가상 메모리에서 주로 사용하는 기법. 중요

<br>

▪ Basic Concepts of the Demand Paging
- 프로세스가 실행중일 때 몇몇 페이지들은 memory에 있고, 몇몇은 secondary storage에 있다
- 페이지가 어디에 위치해 있는지 구별하기 위해
    - `valid-invalid bit` scheme 사용
    - page table에 frame과 valid-invalid bit
    - valid: 페이지가 legal하고, 메모리에 있다
    - invalid: 페이지가 illegal하거나 secondary storage에 있다
    - dirty bit를 사용해서 illegal한 경우와 secondary storage에 있는 경우를 나눌 수 있다

<br>

▪ Page Fault
- main memory에 load되지 않은 page에 접근했을 때 발생
- page fault가 발생하면 MMU가 OS에 trap을 발생시킨다
- page fault 발생 시 해결 절차
    1. process의 internal table(일반적으로 PCB(프로세스 제어 블록)과 함께 보관)에서 reference가 valid or invalid memory access인지 확인한다
    2. reference가 invalid인 경우 프로세스를 종료하고, valid bit이지만 page fault인 경우 page in된다
    3. free frame을 찾는다 (free-frame list에서 하나 선택)
    4. secondary storage를 스케줄링하여 필요한 페이지를 새로 할당된 frame으로 이동시킨다
    5. storage read가 완료되면, 프로세스와 함께 유지되는 internal table과 page table을 수정해서 page가 지금 memory에 있음을 나타낸다
    6. trap에 의해 중단된 instruction을 restart한다
- ![handling_page_fault](./handling_page_fault.PNG)

<br>

▪ Pure Demand Paging
- 요청받을 때까지 page를 memory로 가져오지 않는다
- 메모리에 페이지가 없는 프로세스 실행을 시작할 때
    - OS가 (non-memory resident page에 있는) 프로세스의 first instruction으로 instruction pointer를 설정하고
    - 프로세스는 즉시 page fault가 발생한다
    - 프로세스의 페이지가 page in된다
    - 메모리에 있어야 할 모든 page가 들어올 때까지 faulting하면서 프로세스를 실행한다
- 그때그때 페이지를 로딩해와야 하기 때문에 메모리는 절약되나 속도가 상당히 느리다
- 많이 사용하는 방법은 x, 보통 프로세스 일부 페이지를 미리 로드하고 시작한다

<br>

▪ Locality of References
- 이론적으로 일부 프로그램은 각 instruction execution이 여러 새 메모리 페이지에 access할 수 있으므로 instruction(명령)당 여러 page fault가 발생할 수 있다
- 실행 중인 프로그램을 분석한 결과 이러한 행위가 거의 발생하지 않는 것으로 나타났다 -> locality of reference의 특성 덕분
- 프로그램에는 locality of reference(참조 지역성)을 가지는 경향이 있다
- locality of reference: 프로세서가 짧은 시간 동안 동일한 메모리 위치 집합에 반복적으로 access하는 경향
- Temporal Locality(시간적 지역성): 어떤 지역(data 또는 instruction)이 참조되면 그것은 가까운 미래에 다시 참조될 가능성이 높다 - 반복문, 서브루틴, 스택
- 공간적 지역성: 참조된 지역의 근처에 위치해 있는 메모리는 가까운 미래에 참조될 가능성이 높다 (명령어, 배열 내 요소)
- locality of reference는 demand paging에서 합리적인 성능을 보인다
- 데이터 구조와 프로그래밍 구조를 신중하게 선택하면 코드나 데이터의 지역성을 높일 수 있다 -> page fault 비율을 낮추고 시스템 성능을 향상시킨다

<br>

▪ Hardware Support to Demand Paging
- Demand Paging 처리를 위해 하드웨어 지원이 필요하다
- `Page table`(가상 테이블)은 페이지 유효/무효 여부를 체크한다
- `Secondary memory(=swap space)`는 메인 메모리에 없는 page를 보유한다 secondary memory는 주로 high-speed disk 또는 nvm 장치

<br>

▪ Instruction Restart
- Demand Paging의 중요 requirement - page fault 후 instruction을 다시 시작하는 기능
- page fault가 발생하면
    - interrupt된 프로세스의 상태(registers, condition code, instruction counter 등)가 저장된다
    - page가 page out된다(trap에 의해 wait queue로 이동)
    - page in되면 정확히 같은 상태와 위치에서 restart해야 한다
- 프로세스별로 page table을 잘 관리해야 한다(page table 동시 접근 방지 위함)
- instruction fetch(명령을 가져오는) 중에 page fault가 발생하면 다시 instruction을 fetch해서 restart한다
- operand(연산) fetch 중에 page fault 발생하면 instruction을 fetch and decode한 다음 다시 연산을 fetch한다

<br>

▪ Free Frame List
- Linked List로 frame을 관리하는 Pool로, page fault를 해결하기 위해 os는 free frame list를 가진다
- page fault가 발생하면 secondary storage에서 memory로 페이지를 가져오는데, 이 때 free(비어있는) frame list로 접근한다
- 프로세스의 stack 또는 heap segments가 확장될 때도 free frame이 할당되어야 한다

<br>

▪ Performance of Demand Paging
- demand-paged memory의 `Effective Access Time`을 계산
- ma: memory-access time
- p: page fault가 발생할 확률(probability)
- EAT = (1 - p) * ma + p * (page fault time)
- page fault 처리에서 많은 시간을 차지하는 three major activities(작업)
    - Service the page-fault interrupt - page fault 인터럽트를 처리
    - Read in the page - page를 읽어들이는 과정(가장 많은 시간 차지)
    - Restart the process - 프로세스 재시작

<br>

▪ Copy-on-Write
- ![copy_on_write](./copy_on_write.PNG)
- write할 때 copy하자
- 프로세스가 shared page에 `write`할 때만 해당 shared page를 copy한다
- fork(), exec()에서 발생할 수 있는 상황
- copy 후 page table 수정