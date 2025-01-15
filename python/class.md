# Class

## 1. 클래스 정의하기

### python vs javascript

#### ${\textsf{\color{gray}{==결과==}}}$

```
브랜드=현대, 컬러=white
현대 white
자동차가 달립니다.
자동차를 정지합니다.

브랜드=BMW, 컬러=black
BMW black
자동차가 달립니다.
자동차를 정지합니다.
```

<details>
<summary> $\sf{\color{green}{1. python}}$
</summary>

```python
class Car:
    # 생성자: 객체를 생성할 때 실행되는 메소드(속성을 초기화 할 때 주로 사용)
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # 메소드(기능): 클래스 안에 정의하는 함수
    def stop(self):
        print('자동차를 정지합니다.')

    def run(self):
        print('자동차가 달립니다.')

    # 객체 정보 출력용 메소드
    def __str__(self):
        return f'브랜드={self.brand}, 컬러={self.color}'

# 자동차 객체 생성
car1 = Car("현대", "white") # 생성자는 객체가 실행될때 실행된다.
car2 = Car("BMW", "black")

# 자동차 메소드 실행
print(car1)
print(car1.brand, car1.color)
car1.run()
car1.stop()

print()

print(car2)
print(car2.brand, car2.color)
car2.run()
car2.stop()
```

</details>

<details>
<summary> $\sf{\color{red}{2. javascript}}$
</summary>

```javascript
// Car 클래스 정의
class Car {
    // 생성자: 객체를 초기화
    constructor(brand, color) {
        this.brand = brand // 브랜드
        this.color = color // 색상
    }

    // 메서드: 자동차 정지
    stop() {
        console.log('자동차를 정지합니다.')
    }

    // 메서드: 자동차 달리기
    run() {
        console.log('자동차가 달립니다.')
    }

    // 객체 정보 출력용 메서드
    toString() {
        return `브랜드=${this.brand}, 컬러=${this.color}`
    }
}

// 자동차 객체 생성
const car1 = new Car('현대', 'white')
const car2 = new Car('BMW', 'black')

// 자동차 메서드 실행
console.log(car1.toString())
console.log(car1.brand, car1.color)
car1.run()
car1.stop()

console.log()

console.log(car2.toString())
console.log(car2.brand, car2.color)
car2.run()
car2.stop()
```

</details>
