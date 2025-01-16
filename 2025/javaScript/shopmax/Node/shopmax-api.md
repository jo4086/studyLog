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

