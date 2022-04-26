# Thread

하나의 프로세스는 여러개의 스레드 컨트롤을 가질 수 있다.  
<br>

## 스레드는
- a lightweight process
- CPU 활용의 기본 단위
- 프로세스 안에 여러 스레드가 있으면 pid가 아닌 tid(thread ID)가 CPU를 점유
- PC(program counter), register set(레지스터 정보), 스택(stack)이 스레드별로 다르다

<br>

## 멀티스레드
- 서버에 요청이 들어오면 응답을 위한 스레드 생성
- 장점
1. Responsiveness  
    (특히 유저 인터페이스 처리에서) 논블로킹으로 계속 실행할 수 있다
2. Resource Sharing  
    IPC의 공유 메모리나 메세지 패싱보다 간단하다
3. Economy  
    프로세스 생성보다 싸기 때문에 경제성이 좋다
    컨텍스트 스위칭(PCB)보다 스레드 스위칭이 오버헤드가 낮다
4. Scalability  
    확장성이 좋다 - 프로세스가 멀티프로세서 아키텍처를 활용할 수 있다

<br>

## Java
- 프로그램 실행의 기본 모델이 스레드
- 명시적으로 스레드를 생성하는 세 가지 기술  
    1. Thread 클래스 상속받기 (but 자바는 다중 상속 불가)
    2. Runnable 인터페이스 구현하기 (new class 정의)
    3. Runnable 람다 표현식 사용하기(익명 스레드) - 클래스 선언 없이
- thread.start();
- 부모 스레드의 대기는 join (wait - 프로세스)
- 스레드의 종료는 interrupt

<br>

# Multicore Programming

## 멀티코어 시스템에서의 멀티스레딩
- 멀티코어를 통한 concurrency 향상
- 싱글코어에서는 스레드가 interleaved(사이사이 끼워넣어짐) 된다
- 멀티코어에서는 스레드가 병렬적으로(parallel) 실행될 수 있다
- 멀티코어 시스템에서 문제가 많이 생긴다
- 멀티코어 시스템에서의 Programming Challenges
1. Identifying tasks  
    어떤 부분들이 독립적으로 실행될 수 있는지 찾는다 (병렬 처리)
2. Balance  
    동일한 value로 동일한 작업을 하도록 한다
3. Data splitting  
    각 코어에 실행될 수 있는 데이터가 나뉘어져야 한다
4. Data dependency  
    실행할 때 데이터가 종속되도록 잘 동기화되었는지 확인한다 (의존성 처리)
5. Testing and debugging  
    싱글스레드보다 테스트/디버깅이 훨씬 어렵다

## 병렬처리
- data parallelism, task parallelism
- 지금은 분산 시스템이 됐기 때문에 둘을 구분할 필요가 없어짐

## Amdahl's law (암달의 법칙)
- 코어는 무조건 많을수록 좋은가 - 꼭 그렇지는 않다
- 전부 다 병렬처리 가능한 것이 아니면 큰 의미 X

<br>

# Multithreading Models
## thread 타입
- user threads
    - 사용자 모드에서 사용하는 스레드 (user space)
    - 운영체제와 무관한 스레드 (Java: Virtual Machine)
    - 커널 위에서 지원되고 커널 지원 없이 관리
- kernel threads
    - 커널 모드에서 사용하는 스레드 (kernel space)
    - 운영체제 CPU 코어에서 직접 제어하는 스레드
    - 운영체제가 직접 지원하고 관리

## user threads와 kernel threads와의 관계
1. Many-to-One Model (커널스레드 1 - 유저스레드 N)
2. One-to-One Model
3. Many-to-Many Model

<br>

# Thread Libraries
- 스레드를 생성하고 관리하는 API 제공  
- 요즘 사용되는 주요 스레드
    - POSIX Pthreads (Linux, Unix)
        - just a specification for thread behavior, not an implementation
    - Windows thread
    - Java thread

<br>

# Implicit Threading
concurrent하면서 parallel한 응용 프로그램을 디자인하는 것은 멀티코어 시스템에서 멀티스레딩을 하는 응용 프로그램을 만드는 것과 같다 ··· 너무 어려움  
=> 컴파일러/라이브러리가 알아서 하도록 바꾼다 (암시적 스레딩)

## Four alternative approaches using implicit threading
1. Thread Pools  
    - 여러 개의 스레드를 만들어서 스레드 풀(await work)에 저장해놓고, 필요한 스레드를 꺼내서 쓴다  
    - 라이브러리 제공
2. Fork & Join
    - explicit threading이지만 implicit threading을 위한 방법도 있다
    - 라이브러리
3. OpenMP
    - 컴파일러 지시어를 줘서 아주 쉽게 C/C++에서 병렬처리를 할 수 있도록 지원해준다
    - parallel regions(병렬 영역)만 지정하면 그 코드 블럭을 알아서 병렬적으로 실행시켜준다
    - 컴파일러에게 지시(compiler directive) -> OpenMP 라이브러리가 해당 부분을 병렬처리할 수 있는 스레드로 만들어준다
4. Grand Central Dispatch (GCD)
    - Apple에서 macOS/iOS 운영체제용으로 개발