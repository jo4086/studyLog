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

    - 토큰의 유형(JWT)과 서명 알고리즘(ex: HMAC, RSA)을 포함\

    <details>
    <summary> ${\textsf{\color{hotpink}{example - Header}}}$ </summary>

    ```json
    {
        "alg": "HS256",
        "typ": "JWT"
    }
    ```

    </details>
