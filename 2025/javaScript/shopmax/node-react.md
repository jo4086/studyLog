## $\textsf{\color{red}{1. Socket}}$

-   네트워크 통신을 위한 소프트웨어 인터페이스
-   컴퓨터 간 데이터 교환을 가능하게 함
-   클라이언트와 서버 간의 데이터 통신을 효율적으로 처리하기 위해 사용
-   다양한 네트워크 프로토콜과 함께 동작

### $\textsf{\color{navy}{1. 소켓이란}}$

-   네트워크 연결을 생성하고 관리하기 위한 엔드포인트
-   애플리케이션 레벨에서 데이터를 송수신 가능
-   프로세스 간 또는 컴퓨터 간 통신을 처리

### $\textsf{\color{navy}{2. 작동방식}}$

-   보통 **두 가지 주요 통신 주체** 간 연결을 기반으로 작동
    -   **클라이언트**: 요청을 보내는 **주체**
    -   **서버**: 요청을 받아 처리하고 응답하는 **주체**
-   기본 동작 과정
    1. **서버 소켓 생성 및 바인딩**: 서버는 특정 IP와 포트에 소켓을 바인딩하고 연결을 대기
    2. **클라이언트 요청**: 클라이언트 => 서버의 IP와 포트에 연결 요청
    3. **연결 수락**: 서버측에서 클라이언트의 **연결 요청을 수락** => **데이터 전송이 가능**
    4. **데이터 전송**: 양쪽에서 데이터를 송수신
    5. **연결 종료**: 데이터 통신이 끝난 후 연결을 종료

### $\textsf{\color{navy}{3. 소켓의 유형}}$

1). **스트림 소켓 (_Stream Socket_)**

-   **프로토콜**: TCP (_Transmission Control Protocol_)
-   **특징**
    -   신뢰성 있는 연결
    -   순차적 데이터 전달 및 무손실
-   **사용처**
    -   실시간 스트리밍
    -   파일 전송

2). **데이터그램 소켓 (_Datagram Socket_)**

-   **프로토콜**: UDP (_User Datagram Protocol_)
-   **특징**
    -   비 연결형 통신
    -   빠른 데이터 전송 **AND** 신뢰성은 중요하지 않은 경우
-   **사용처**
    -   온라인게임
    -   동영상 스트리밍

3). **로우 소켓 (_Raw Socket_)**

-   **특징**
    -   TCP/UDP와 같은 프로토콜 헤더를 사용하지 않음
    -   데이터 패킷을 직접 처리
-   **사용처**
    -   네트워크 패킷 분석
    -   방화벽 애플리케이션

## $\textsf{\color{red}{2. Socket.IO}}$

-   Node.js에서 사용되는 라이브러리
-   **실시간 양방향 통신**울 구현하는데 사용
-   기본적으로 **WebSocket 프로토콜** 위에서 동작 $\texttt{\color{red}{BUT}}$ <ins>브라우저와 네트워크 환경</ins>에 따라 자동으로 폴백(Fallback)하여 AJAX 폴링 등 다른 기술을 활용할 수 있음

### $\textsf{\color{navy}{1. Socket.IO의 특징}}$
#### (1). 양방향 실시간 통신:


### $\textsf{\color{navy}{5. 소켓의 준비}}$

-   React: `yarn add socket.io-client`
-   Node: `npm install socket.io`
