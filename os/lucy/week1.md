# operating system(운영체제)
  -컴퓨터 하드웨어를 관리하는 소프트웨어  
  -하는 일: 어플리케이션 프로그램과 컴퓨터 유저, 그리고 컴퓨터 하드웨어 간의 중간 매개(intermediatry) 역할을 해준다.  
  -항상 실행되고 있는 하나의 프로그램. 주로 `kernel`이라 불림.
  -커널에서 시스템 프로그램과 응용 프로그램(application program)에 대한 인터페이스를 제공해준다.
  -운영체제의 커널 부분이 핵심이다.

<br>

### 컴퓨터 시스템의 4개 컴포넌트
    하드웨어, 운영체제, 어플리케이션 프로그램, 유저
  <!-- CPU, Proccessor, Core, Multicore, Multiprocessor   -->

<br>
시스템 프로그래밍, 어플리케이션 프로그래밍을 할 때 OS와 통신하면 하드웨어에 transparent하게 프로그래밍할 수 있다. <br> 
그 프로그램 중에는 컴파일러와 같은 시스템 프로그램, 어셈블러, 텍스트 에디터, 데이터베이스 시스템같은 응용 프로그램 등이 있다. <br> 
=> 어떤 종류의 응용프로그램이든 운영체제가 서비스를 제공해주는 형태로 진행할 수 있다. 따라서 사용자는 응용프로그램을 통해 시스템과 통신한다. <br> 


- morden computer system: 신경망 컴퓨터, 네트워크 컴퓨터, 양자 컴퓨터-> 폰노이만 구조를 따르지 않는 새로운 형태의 컴퓨터 시스템
- classical computer system: 전통적인 컴퓨터 시스템  
  => CPU(Central Processing Unit)가 있고, 버스를 통해 연결되어 있는 여러개의 디바이스 컨트롤러가 있다.
  CPU는 bus를 통해서 memory(RAM)와 연결되어 있고, disk controller를 통해서 디스크들과 연결되어 있고, USB controller를 통해 마우스, 키보드, 프린터와 연결되어 있고, 그래픽 어댑터(graphics adapter)를 통해 모니터와 연결되어 있다(I/O devices). 요즘은 블루투스 등과 같은 무선장치를 통한 RF 통신도 이루어진다. => 이런 형태의 컴퓨터 시스템을 OS가 제어해준다.

<br>

### bootstrap program
> 컴퓨터가 power on을 했을 때 처음으로 실행되는 간단한 프로그램(ROM에 저장되어 있는 프로그램) => 메모리에 운영체제(OS)를 로딩하는 일.
> power on을 했을 때 cpu가 제일 처음에 로딩할 때는 ROM에 저장되어있는 명령어를 불러옴(memory는 휘발성이라 처음 불러올 때 쓰레기 값이 들어있음)

### Interrupts
> 하드웨어가 언제든 interrupt를 trigger시킬 수 있다 - trigger시키면 CPU에 시스템 버스를 통해서 시그널을 전송한다. CPU는 그 시그널을 받아서 처리.
> 메모리에서 cpu로 instruction을 fetch-execute하는 것을 반복하는데, I/O device에서 입력된 값을 CPU에게 알려주는 것을 interrupt라는 방법으로 알려준다.
> CPU(process)와 I/O 디바이스와 통신하는 방법 중 하나가 Interrupt

### IR(Instrution Register)
>`fetch-excute cycle`을 von Neumann architecture라고 한다.
>instruction을 메모리에서 하나씩 가져오는 register를 `instruction register`라고 한다. 

<br> 

cpu-memory에서 메모리는 ram, 휘발성 메모리라서 비휘발성 저장장치가 필요한데, 비휘발성 저장장치(storage system)는 계층구조가 있다-용량에 따라, access time(접근속도)에 따라.
### [Storage-device hierarchy(계층)]
- 제일 빠른건 cpu 안에 있는 register(cpu 안에 회로로 묶여 있어서 엄청나게 빠름)
- ram도 빠르지만, register와 RAM 중간에 램보다 훨씬 더 빠른 cache 메모리가 있다 => 캐싱을 해야 함. cache는 램보다 빠르지만 훨씬 더 비싸기 때문에 용량을 크게할 수 없다.
- 그다음 main memory가 RAM이다.
- SSD(solid-state disk): 메모리 형태의 하드디스크 역할을 한다.
- hard disk: 자기장(마그네틱 카드)을 이용한 하드디스크(HDD)
- HDD로 저장하기에도 양이 많은 건 optical disk(광학 디스크)나 magnetic tapes에 저장한다 - 백업 용도로(은행같은 경우에도 5년-10년전 것들을 보존하기 위해 magnetic tape에 백업해 놓는다-보존하기에 가장 저렴)

### [I/O structure]
>실행되는 과정이 실처럼 생겨서 `thread`  
어떤 CPU가 thread of execution을 갖고 있는데,  
cache 메모리를 통해 RAM(memory)에 access하고,  
I/O 디바이스와 Interrupt하고 data 주고받고 I/O request를 보내는 복잡한 구조를 갖고 있다.

유튜브 동영상을 보여준다 - CPU가 할 일은 별로 없다. 네트워크로부터 데이터를 받는 건 네트워크 장치가 할 일이고, LCD에 화면 띄우는 것은 LCD display가 할 일이다. => CPU가 연산할 일은 별로 없음. => network hardware가 LCD에 다이렉트로 데이터를 보내고, 중간에 CPU가 정지/재생 등에 대해서만 처리해주면 된다.
```
=> 디바이스와 디바이스끼리 다이렉트로 access한다: DMA(Direct Memory Access)
+특정 하드웨어 하위 시스템이 CPU와 독립적으로 메인 시스템 메모리에 접근한다
```

<br> 
OS 커널은 굉장히 안정적임. 커널이 업그레이드 되는 경우는 작다.
OS code는 I/O를 managing하는데 dedicated 하다.
device를 제어하는 device controller를 만드는 게 운영체제 개발의 98% 이상. 커널 개발도 계속 발전하고 있지만 거의 안정화되어있다.

<br>

### [Symmetric multiprocessing(SMP, 대칭형 다중 처리)]
'cpu 하나, 메모리 하나' 이 구조는 더이상 사용하지 않음(초소형 임베디드 시스템이 아닌 이상).  
이제는 Symmetric multiprocessing할 수 있는 symmetric multi processor들이 탑재되어 있다.  
프로세서(CPU)가 하나가 아니라 여러개(multi)다.  
Asymmetric한 것도 있는데 거의 안쓰니까 무시해도 ok.  
Symmetric multiprocessing: `메모리 하나에 연결되어 있는 CPU가 여러개`(CPU는 각각의 registers와 cache를 가짐).


### [Multi-core design]
CPU 자체를 여러개 다는 것은 비용이 많이 들기 때문에, `CPU 하나의 칩 안에 각각의 registers와 cache를 가진 CPU core를 여러개 다는 회로 구성 방식`이 Multi-core 방식  
코어 개수에 따라 (single(1), dual(2), triple(3), quad(4), hexa(6), Octa(8), deca(10), dodeca(12), ... , multi-core)

#### [Multiprogramming]
program: a set of instruction, 일련의 지시  
옛날에는 프로그램을 메모리에 한개만 로딩해서 쓰고, 일 끝나면 메모리 버리고 새 메모리 로딩해서 쓰는 방식을 썼었음(OS는 그대로 두고).  
-> 여러 개의 프로그램을 동시에 올려놓고 동시에 실행시키면 되지 않냐   
=> 메모리에 여러개의 프로그램을 동시에 올리는 것(multiprogramming)
`한 번에 한개 이상의 프로그램이 실행되는 것`
메모리에 여러 프로세스가 동시에(siultaneously) 올라가있다(keep)  
=> CPU 사용 효율(utilization)을 높일 수 있다.

#### [Multitasking(=multiprocessing)]
````
multiprogramming을 통해 Multitasking(=multiprocessing)을 할 수 있게 됨.
multiprogramming의 logical extension이다.  
멀티프로그래밍이 되면, 하나의 CPU가 여러 프로세스를 자주 바꿔서 실행(switch)할 수 있다. => concurrency(병행성), parallelism(병렬성)  
-> 이런걸 하려면 **CPU scheduling(어떤 프로세스를 다음에 실행시켜서 CPU 효율을 높일 것인가)이 필요하다.  

cf. program: a set or instruction(일련의 지시), 한 프로그램에 여러 프로세스 진행 가능.
process: program in execution(실행중인 프로그램. 프로그램이 실행되면 이를 프로세스라 한다.) + 프로그램을 실행시키는 주체(인스턴스)


하나의 메모리에 프로세스를 동시에 여러개 올릴 수 있다 - 멀티 프로그래밍
멀티프로그래밍 된 프로세스들을 CPU가 timesharing하면서 동시에 component하게 실행시킬 수 있다 - 멀티프로세싱(멀티태스킹)
````
>멀티프로세스와 멀티프로그래밍  
https://www.geeksforgeeks.org/difference-between-multiprocessing-and-multiprogramming/

<br> 
운영체제가 등장하면 operation mode가 중요해진다.

<br> 
 
### [operation의 두가지 모드]
`user mode`(어플리케이션 동작)와 `kernel mode`로 나눔
잘못된 프로그램으로 인해 다른 프로그램이 잘못 실행되도록 하지 않는다 - 운영체제의 역할
user process는 쭉 실행하다가 kernel에 system call(os에게 서비스 요청)을 한다 - 이때 kernel mode로 바꿔서 system call을 처리한 후에 다시 user mode로 변환한다.
kernel mode에서만 직접적인 하드웨어 제어를 할 수 있음 - 사용자가 악의적으로 하드웨어 제어하기 어려움

<br> 

---
#### 현대 컴퓨터 시스템
<br> 

#### [Virtualization(가상화)]
하드웨어 하나에 운영체제 여러개 - 하드웨어 위에 VMM(Virtual Machine Manager/Monitor)을 올려서 그 위에 운영체제를 여러개 올릴 수 있다.
CPU 스케쥴링 하듯이 VMM 스케쥴링 할 수 있다 - 동시에 여러 OS가 돌 수 있음.
VMware, XEN, WSL(Windows Subsystem for Linux)
cf. hypervisor(하이퍼바이저): 가상 머신(Virtual Machine, VM)을 생성하고 구동하는 소프트웨어. 호스트 컴퓨터에서 다수의 운영 체제(operating system)를 동시에 실행하기 위한 논리적 플랫폼(platform)

#### [Operating Systems in the Variety of Computing Enviroments]
- Traditional Computing: CPU 하나에 메모리 하나
- Mobile Computing
- Client-Server Computing: 서버와 클라이언트들. 대표적으로 Web(웹서버와 웹클라이언트(브라우저))
- Peer-to-Peer Computing: peer끼리 N:N 통신. 음악/영화 파일 공유 napster -> bittorrent(파일 조각을 나누어 중앙 서버 없이 운영), p2p에 원장(元帳, ledger)을 쓰자=>BitCoin(BlockChain기술 - p2p 컴퓨팅의 산물)
- Cloud Computing(=edge computing): AWS, Azure, GCP
SaaS(Software as a Service). 컴퓨터 하드웨어 자원은 네트워크를 통해 연결되는 UI(user interface)에 불과하고, 실제 모든 컴퓨팅 자원은 클라우드에 있다. 네트워크도 CDN(Content delivery network) 사용. 우리는 터미널을 통해 클라우드 서비스를 잘 조합하여 사용하면 된다. 
- Real-Time Embedded Systems: 화성탐사. VxWorks - 하드웨어를 직접 real-time으로 운영하는 운영체제가 필요 - RTOS(Real Time Operating System)
=> 운영체제보다 컴퓨팅 환경이 더 중요해진 현대 사회. 운영체제는 컴퓨팅 환경의 일부가 될 뿐.
이런 컴퓨팅 서비스들을 운영체제가 어떻게 반영해줄 것이냐가 핵심 이슈.

<br> 

#### [운영체제의 역할]
: 프로그램이 실행될 수 있는 환경을 제공.
- User interface
- Program execution(process management)
- I/O operation
- File-system manipulation
- Communications
- Error detection
- Resource allocation
- Logging
- Protection and security

<br> 

```
**Process와 thread
**multiprocessing, CPU scheduling
 synchronization, deadlock, memory management, virtual memory
```  
<br> 

#### [user가 OS에 interface하기 위한 방법]
- CLI(command line interface): 명령어 기반의 인터페이스
  -sh, bash, csh, tcsh, zsh, etc.
- GUI(graphical user interfae): 그래픽 사용자 인터페이스
  -Windows, Aqua for MacOS, KDE/GNOME for Linux, etc.
- 터치스크린 인터페이스
  -안드로이드/아이폰 UI, etc.

<br> 

#### [컴퓨터 응용 프로그램이 OS와 interface하는 방법]
- System calls
os가 제공해주는 서비스를 system call을 통해 호출한다.
read, write
시스템 함수를 호출하는 것 => `API (Application Programming Interface)`
OS의 API가 system call이다.
system call interface를 통해서 사용자가 open()해서 read/write한다. 하지만 항상 이렇게 user mode <-> kernel mode를 일일히 open()해서 system call을 하기 힘들다 => 라이브러리 제공(the standard C library) - Windows, UNIX system calls 중에 Process를 제어하는 대표적인 system call이 fork(), wait() & Communication을 위한 shm_open()