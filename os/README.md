# OS 스터디 

## 학습자료
- [인프런 운영체제 공룡책 강의](https://www.inflearn.com/course/%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C-%EA%B3%B5%EB%A3%A1%EC%B1%85-%EC%A0%84%EA%B3%B5%EA%B0%95%EC%9D%98)
- [Operating-System-Concepts-10th-edition](https://os.ecci.ucr.ac.cr/slides/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf)
- [참고 블로그1](https://parksb.github.io/article/5.html)

## 면접 예상질문
<details>
<summary>프로세스 생성 과정에 대해서 설명해보세요</summary>
<div markdown="1">
  
- 일반적인 프로세스 생성 과정
  - PCB가 생성되며 OS가 실행한 프로그램의 코드를 읽어들여 프로세스에 할당된 메모리의 Text segment에 저장한다.
  - 초기화된 전역 변수 및 static 변수를 data segment에 할당.
  - HEAP과 Stack은 초기 메모리 주소만 초기화됨.
  - PCB에 여러 정보가 기록되면 Ready Queue에서 CPU를 할당받기까지 대기한다.

</div>
</details>

<details>
<summary>프로세스와 쓰레드의 차이를 설명해보세요</summary>
<div markdown="1">
  
프로세스는 실행되는 프로그램 자체와 프로그램이 실행되는 주변 환경을 포함하는 개념이다. 실행되는 주변 환경이란 사용중인 파일, 데이터, 메모리 영역 주소 공간등을 뜻한다.

쓰레드는 프로세스 내부에서 프로세스의 자원을 공유하거나 공유하지 않고 실행되는 작업의 단위이다.

</div>
</details>

<details>
<summary>프로세스와 쓰레드의 차이를 설명해보세요</summary>
<div markdown="1">
  
크롬은 탭마다 PID를 가지고 있으니 Process이며 각 Tab마다 랜더링 정보나 기타 데이터를 따로 관리한다고 한다. 그로인해 메모리를 많이 잡아먹기도 하지만 하나의 Tab에 오류가 생겼다고 모든 Tab에 영향을 끼치진 않는다.

</div>
</details>


