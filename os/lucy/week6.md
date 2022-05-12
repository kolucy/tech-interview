# Synchronization

## Cooperating processes
- 서로 영향을 주고 받음
- share a logical address space - thread
- share data - shared memory, message passing
- 공유 데이터에 concurrent(동시) access => ``data inconsistency``(불일치)
- **orderly execution**을 보장해야 함 -> **maintain data consistency**
- ``Integrity of data`` (데이터 무결성)
    - Concurrent execution
        - context switch 발생 위치에 따라 register 값이 달라짐
        - interleaved in some arbitrary order (임의의 순서로 삽입됨)
        - ``Race Condition``
    - Parallel execution
- 'count++' in machine language
    ``` c
    register = count
    register = register + 1
    count = register
    ```

## Race Condition (경쟁 상태)
- 공유 자원을 동시에 접근하는 상황
- same/shared data를 concurrently하게 실행하려할 때, 실행 결과(outcome)는 access가 발생하는 특정 순서에 따라 달라진다
- race condition 해결 방법
    - **Synchronization**: 한 번에 한 프로세스만 공유 데이터를 조작하도록 한다 (프로세스/스레드 동기화)
- race condition 사례 - kernel 영역: fork()

<br>

## The Critical Section Problem (임계 영역)
- a segment of code
- in which the process may be accessing and updating data
- that is shared with at least one other process.
- 한 프로세스가 임계 영역에서 실행중일 때, 다른 프로세스는 임계 영역에서 실행할 수 없다 => **동시에 두 프로세스가 임계 영역에서 실행할 수 없다**
- 동기화(synchronize)를 이루고 cooperatively share data할 수 있다
- Sections of codes  
    1. entry section (진입 영역)  
    2. critical section (임계 영역)  
    3. exit section  
    4. remainder section  
- 해결 조건  
    1. ``Mutual Exclution`` (상호 배제)  
    2. ``Progress``(진행)  
      - 임계 영역에 들어갈 프로세스를 결정    
      - deadlock 방지(avoid)  
      - deadlock: 무한대로 진입이 연기되는 상황
    3. ``Bounded Waiting``(한정 대기)  
      - starvation(기아) 방지(avoid)  
      - 프로세스가 임계 영역에 들어갈 수 있는 횟수 제한
- 3가지를 다 만족해야 임계 영역 문제를 해결하지만, 다 푸는 방법은 어렵다(현실 적용 가능성x)
- Mutual Exclution만 적용하고, 나머지 두 상황은 발생하면 해결
- single-core 환경에서의 간단한 해결책
    - Prevent interrupts (인터럽트 방지) - disable interrupt
    - 멀티프로세스 환경에서는 불가능(not feasible)
- non-preemptive kernel
    - race condition 발생 가능성 x
    - 하지만 non-preemptive는 느리기 때문에 현대에서 사용 x
- preemptive kernel
    - 디자인하기 어렵지만, responsive하기 때문에 유리하다

<br>

=> 동기화(Synchronization): 데이터의 무결성(integrity)을 보장

<br>

---
동기화문제 해결책