# shopmax-api_studyLog

## 1. routes: order.js

-   `items`가 배열인 이유: 장바구니로 주문할 경우 여러가지 주문목록을 Promise.all과 map(async () => await) 구조로 병렬로 빠르게 처리하기 위해서

### $\textsf{\color{navy}{α. Promise.all과 map(async ( ) => { await })}}$

'''javascript

const orderItemsData = await Promise.all(
items.map(async (item) => {
// 1. 상품 재고 확인
const product = await Item.findByPk(item.itemId, { transaction })

        // 2. 재고 차감

        // 3. 재고 차감후 [item 테이블] 새로 저장
    })

)

for(const item of items) {
const product = await Item.findByPk(item.itemId, { transaction })
}

'''

## JWT 토큰 (Json Web Token)

**JWT(_json web token_)** 은 JSON 형식의 데이터를 이용 => 사용자 인증 및 정보를 **안전하게 전달**하기 위한 개방형 표준(_RFC 7519_)

### ${\textsf{\color{navy}{1. JWT의 구조}}}$

1. $\textsf{\color{blue}{ 헤더(Header)}}$

    - 토큰의 유형(JWT)과 서명 알고리즘(ex: HMAC, RSA)을 포함

    <details>
    <summary> ${\textsf{\color{hotpink}{example - Header}}}$ </summary>

    ```json
    {
        "alg": "HS256",
        "typ": "JWT"
    }
    ```

    </details>

2. $\textsf{\color{blue}{ Payload(페이로드)}}$

    - **클레임(claim)** 을 포함
    - 클레임(claim): 토큰에 담길 데이터로 **크게 3가지로 분류**
        - **등록된 클레임 (Registered Claims)**: 사전에 정의된 표준 클레임 (ex: `iss`, `exp`, `sub` 등)
        - **공개 클레임 (Public Claims)**: 사용자 정의 데이터
        - **비공개 클레임 (Private Claims)**: 특정 애플리케이션 간에만 사용되는 데이터

    <details>
    <summary> $\textsf{\color{hotpink}{example - Payload}}$ </summary>

    ```json
    {
        "sub": "1234567890",
        "name": "John Doe",
        "admin": true
    }
    ```

    </details>

## Socket

-   네트워크 통신을 위한 소프트웨어 인터페이스
-   컴퓨터 간 데이터 교환을 가능하게 함
-   클라이언트와 서버 간의 데이터 통신을 효율적으로 처리하기 위해 사용
-   다양한 네트워크 프로토콜과 함께 동작

#### 소켓이란...

-   네트워크 연결을 생성하고 관리하기 위한 엔드포인트
-   애플리케이션 레벨에서 데이터를 송수신 가능
-   프로세스 간 또는 컴퓨터 간 통신을 처리

#### 작동방식

-   보통 **두 가지 주요 통신 주체** 간 연결을 기반으로 작동
    -   **클라이언트**: 요청을 보내는 **주체**
    -   **서버**: 요청을 받아 처리하고 응답하는 **주체**
- 기본 동작 과정
    1. **서버 소켓 생성 및 바인딩**: 서버는 특정 IP와 포트에 소켓을 바인딩하고 연결을 대기
    2. **클라이언트 요청**: 클라이언트 => 서버의 IP와 포트에 연결 요청
    3. **연결 수락**: 서버측에서 클라이언트의 **연결 요청을 수락** => **데이터 전송이 가능**