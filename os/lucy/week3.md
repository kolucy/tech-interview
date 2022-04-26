# IPC

### 프로세스가 concurrently하게 실행되는 2가지 경우
1. 독립적으로 실행 - 공유하는 데이터도, 주고받을 메세지도 없음. cpu 스케줄링 잘 하면 별 문제 없이 잘 진행됨  
2. **협력적** 실행 - 서로 영향을 주고받을 수 있음. 서로 데이터/메세지를 주고받으려할 때 문제가 생김 -> 이걸 어떻게 해결할거냐 => **IPC** 

<br>

### IPC(Inter-Process Communication)
- 프로세스 간 통신 문제  
- 협력하는 프로세스들은 IPC 메커니즘이 필요  
- 기본적인 IPC 메커니즘은 결국 데이터를 exchange하는 과정  

### IPC의 2가지 모델
1. 공유 메모리 사용(`Shared memory`) - 운영체제가 만들어 줌.
2. 메세지 전달(`Message Passing`) - 메세지 큐를 통해. 운영체제(커널)에게 맡김. 

<br>

### Producer-Consumer Problem
협력하는 프로세스 간 가장 기본적인 문제, 이 문제를 풀 수 있으면 기본적인 통신 문제를 풀 수 있다.  
: 생산자는 정보를 생산하고, 소비자는 정보를 소비하는 모델  
ex) 컴파일러가 어셈블리어를 생산하면 어셈블러가 어셈블리어를 소비해서 기계어 생산  
브라우저가 request하면 웹서버가 html 파일을 생산하고 브라우저가 그걸 소비(뿌려줌)  

### Producer-Consumer Problem의 해결방법  
1. 공유 메모리를 사용하는 방법  
두 개의 프로세스가 명시적으로 약속한 공유 메모리에 read/write 한다.  
컨텍스트 스위칭을 통해 타임셰어링하며 두개가 동시에 실행  
-> 중간에 `*버퍼(buffer)`를 사용  
생산자는 버퍼를 채우고, 소비자는 버퍼를 비운다(가져간다).  
대부분은 bounded buffer. 따라서 버퍼가 가득 차면 생산자는 wait  
버퍼가 비어있으면 소비자는 버퍼가 찰 때까지 wait - `버퍼를 통해 동기화`가 잘 이루어짐  
=> 버퍼를 공유 메모리로 만든다.  
공유 메모리는  생산자과 소비자 프로세스가 공유하고 있는 메모리 영역을 의미한다.  
공유메모리 방식의 문제점: 메모리 영역을 공유하게 되면, 메모리 영역에 명시적으로 접근하고 사용하는걸 응용프로그래머가 다 구현해야 한다.  

2.  메세지 패싱 방식  
os가, 협력하는 프로세스들에게 수단(API)을 제공해준다.  
메세지 패싱의 두가지 작업: `send, receive`  
`communication link`를 만들어서 전송한다 - 받고, 주는 두 개의 시스템콜만 적용하면 된다(세부 작업은 os가 알아서 해줌).  
send, receive 하는 과정에서 반드시 mailbox/port를 사용한다.  
<br>

### Communication Link 구현 방식
- **direct / indirect** 
    - direct
        - recipient(수신자)와 sender(발신자)를 `명시적`으로 정한다.
        - 링크가 *자동적으로 생성된다.
        - 프로세스 쌍에 정확히 하나의 링크만 존재한다.
    - indirect
        - mailbox나 port로부터 메세지가 보내지고 받아진다.
        - `추상적`으로 객체를 볼 수 있다.
        - A로 보내고, A에서 받는다 => send(A, message) , receive(A, message)
        - 두 프로세스가 공유된 메일박스가 있을 때만 프로세스 간의 링크가 생성된다.
        - 링크가 두 개 이상의 프로세스와 연결될 수 있다.
        - 여러개의 서로 다른 링크가 존재할 수 있다.  
        => OS가 제공하는 메커니즘
            - 새 메일박스를 생성
            - 메일박스에 메세지를 보내고 받는다
            - 메일박스를 삭제한다
- **synchronous(동기) & asynchronous(비동기)** 
    - blocking / non-blocking: blocking은 synchronous하고 non-blocking은 asynchronous하다.
    - blocking send: 메세지를 받을 때까지 sender가 block된다.
    - non-blocking send: sender는 메세지를 보내고 continue한다.
    - blocking receive: receiver는 메세지를 사용가능할 때까지 차단(block)한다.
    - non-blocking receive: receiver는 유효하거나 null인 메세지를 받는다.
- **automatic(자동) / explicit(명시적) buffering(메모리 관리)**  
  
<br>

### IPC 시스템의 예
- Shared Memory: POSIX Shared Memory 기법
    - POSIX: Portable Operating System Interface (for uniX)
    - uniX 운영체제의 표준화 시도
    - Linux도 POSIX 표준을 거의 도입하고 있음
    - `memory-mapped file`을 이용 (공유 메모리 영역을 파일과 연결)
    - 보통은 HDD의 저장공간에 영역을 잡는데, 메모리에 파일을 생성하면 매우 빠름
    - shared-memory 객체 생성 -> 크기(bytes) 설정 -> memory-mapped file 생성
- Message Passing: Pipes
    - UNIX 시스템의 초기 IPC 메커니즘 중 하나
    - 전통적으로 UNIX 시스템에서는 가장 기본적인 pipe 구조를 많이 사용
    - 두 프로세스가 커뮤니케이션하는 도구(conduit)로서 사용됨
    - Pipe 구현 시 4가지 이슈
        - unidirectional(단방향) or bidirectional(양방향)? => 단방향
        - two-way comm.의 경우 half-duplex or full-duplex? => full은 pipe 두개 만들면 됨
        - 커뮤니케이션 프로세스 간 relationship이 존재해야 하는가? => pipe는 구현 편의상 부모 자식 관계를 가짐
        - 네트워크에서 동작할 수 있는가? => pipe가 네트워크 통해서 가는건 쉽지 않음 - pipe는 네트워크에서 안쓰고, `네트워크에서 쓸 수 있는 pipe` 사용 => `socket`
    - Pipe의 두 가지 유형
        - Ordinary pipes
            - 생성한 프로세스 외부에서 접근 불가
            - 반드시 부모가 pipe를 만들어서 자식과 커뮤니케이션하는 데 쓴다.
            - producer-consumer fashion
            - unidirectional한 두 개의 pipe를 사용하여 two-way communication
        - Named pipes
            - 부모-자식 관계 없이도 접근 가능

<br>

### 클라이언트-서버 시스템
- Socket
    - 통신을 위한 endpoints - IP address와 port를 묶으면 socket
    - Java가 처음으로 소켓을 쉽게 쓸 수 있는 인터페이스 제공
    - **Socket** class: connection-oriented(**TCP**)
    - **DatagramSocket** class: connectionless(**UDP**)
    - **MulticastSocket** class: multiple recipients
- RPC (Remote Procedure Call)
    - 원격에 있는 Procedure를 호출
    - 원격 서비스의 가장 일반적인 형태 중 하나
    - Java는 RMI, WINDOWS는 COM(DCOM), ...
    - 클라이언트는 원격 호스트의 프로시저를 호출
    - RPC system
        - client side에 있는 stub을 통해 호출
        - 커뮤니케이션을 가능하게하는 세부 사항을 숨김(클라이언트 측에서 stub을 제공함으로써)
        - 원격 서비스를 이용하는 두 개의 API끼리 주고받는 데 데이터를 정렬하는 걸 `마샬링(Marshalling)`이라 한다.
        - 마샬링한 객체를 주고받는다

=> IPC(컴퓨터 내부에서 두개 프로세스 간 통신)의 확장이 RPC(원격 네트워크 컴퓨터끼리 통신)

<br>

프로세스 간 자원을 공유하면 문제가 생김 - 자원공유를 어떻게 할 것인가
프로세스로 처리하기엔 너무 무거우니까 - 프로세스 안에서 concurrency를 지원해주는 것이 스레드(thread)

Ch.3 핵심 개념 - https://parksb.github.io/article/7.html