# Class

## 0. 클래스란?

-   파이썬에서 **클래스`(class)`** 는 객체 지향 프로그래밍(_Object-Oriented Programming, OOP_)의 **핵심 개념** 중 하나

-   클래스는 객체를 생성하기 위한 청사진 또는 **설계도**

-   클래스는 **속성`(Attributes)`** & **메서드`(Methods)`** 를 정의하여 특정한 데이터를 구조화하고 동작을 지정하는 데 사용

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

## 2. 주요 구성 요소

**1. 속성(Attributes)**

-   **클래스 속성**: 클래스 자체에 속한 변수로, 모든 인스턴스가 공유합

*   **인스턴스 속성**: 인스턴스(객체)마다 개별적으로 관리되는 변수로, 생성자에서 주로 정의

**2 메서드(Methods)**

-   **인스턴스 메서드**: 각 객체와 연관된 메서드, 첫 번째 매개변수로 항상 self를 받음.
-   **클래스 메서드**: 클래스 자체에 작용하는 메서드로, 첫 번째 매개변수로 cls를 받으며 @classmethod 데코레이터를 사용합니다.
-   **정적 메서드**: 클래스나 인스턴스와 <span style='text-decoration:underline; font-style:italic;'>관계없이 작동하는 메서드</span> 로, `@staticmethod` 데코레이터를 사용

## 3. 상속

-   클래스는 다른 클래스를 **상속**받아 기존 **기능을 확장**가능

<details>
<summary> 3. example $\textbf{(Click!)}$
</summary>

```python
class ParentClass:
    def parent_method(self):
        return "부모 클래스 메서드"

class ChildClass(ParentClass):
    def child_method(self):
        return "자식 클래스 메서드"

# 사용
child = ChildClass()
print(child.parent_method())  # 출력: 부모 클래스 메서드
print(child.child_method())   # 출력: 자식 클래스 메서드
```

</details>

## 4. 메서드 오버라이드

-   **자식 클래스**에서 **부모 클래스**의 `메서드`와 _동일한 이름으로_ `메서드를 정의`하면, <span style='text-decoration:underline;'>부모 클래스의 메서드를 재정의</span> 할 수 있다.

<details>
<summary> 4. example $\textbf{(Click!)}$
</summary>

```python
class Parent:
    def greet(self):
        return "안녕하세요! 저는 부모 클래스입니다."

class Child(Parent):
    def greet(self):
        return "안녕하세요! 저는 자식 클래스입니다."

# 사용
parent = Parent()
child = Child()

print(parent.greet())  # 출력: 안녕하세요! 저는 부모 클래스입니다.
print(child.greet())   # 출력: 안녕하세요! 저는 자식 클래스입니다.

```

[Child] 클래스의 `greet` 메서드는 부모 클래스의 `greet` 메서드를 **재정의(오버라이드)** 함

</details>

### 4-1. 부모 메서드 호출

-   <span style='text-decoration:underline;'>오버라이드된 메서드 내부에서</span> **부모 클래스의 메서드를 호출**가능

<details>
<summary> 4-1. example $\textbf{(Click!)}$
</summary>

```python
class Parent:
    def greet(self):
        return "안녕하세요! 저는 부모 클래스입니다."

class Child(Parent):
    def greet(self):
        parent_message = super().greet()  # 부모 클래스의 메서드 호출
        return f"{parent_message} 그리고 저는 자식 클래스입니다."

# 사용
child = Child()
print(child.greet())
# 출력:
# 안녕하세요! 저는 부모 클래스입니다. 그리고 저는 자식 클래스입니다.

```

`super().greet()`를 사용하여 부모 클래스의 `greet` 메서드를 호출한 뒤 자식 클래스의 메서드를 추가

-   `super().greet()` = **`{parent_message}`**: "안녕하세요! 저는 부모 클래스입니다."
-   `child.greet()`: f"**`{parent_message}`** 그리고 저는 자식 클래스입니다."

</details>

### 4-2. 속성 오버라이드

-   자식 클래스에서 부모 클래스와 동일한 이름의 속성을 정의하면 부모의 속성을 덮어씀

<details>
<summary> 4-2. example $\textbf{(Click!)}$
</summary>

```python
class Parent:
    message = "부모 클래스의 메시지"

class Child(Parent):
    message = "자식 클래스의 메시지"

# 사용
print(Parent.message)  # 출력: 부모 클래스의 메시지
print(Child.message)   # 출력: 자식 클래스의 메시지

```

</details>

### 4-3. 특수 메서드(연산자 오버라이드)

-   `__add__`, `__str__`, `__eq__` 같은 특수 메서드를 오버라이드하여 <span style='text-decoration:underline;'>연산자나 내장함수의 동작</span>도 **변경 가능**\
     ▶ **`연산자 오버로딩`**이라고 부름

<details>
<summary> 4-3. example $\textbf{(Click!)}$
</summary>

```python
class CustomNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

# 사용
num1 = CustomNumber(10)
num2 = CustomNumber(20)

print(num1 + num2)  # 출력: 30

```

`__add__` 메서드 오버라이드 => `+`연산자의 동작의 커스터마이징

</details>

### 정리

-   <span style='font-size:0.9em;'>**메서드 오버라이드**: 부모 클래스의 메서드를 재정의.</span>
-   <span style='font-size:0.9em;'>**부모 메서드 호출**: `super()`를 사용하여 부모 클래스의 메서드 기능을 호출.</span>
-   <span style='font-size:0.9em;'>**속성 오버라이드**: 자식 클래스에서 속성 이름을 **재정의하여 덮어**쓰기.</span>
-   <span style='font-size:0.9em;'>**특수 메서드 오버라이드**: [`__add__`, `__str__`] 등을 오버라이드하여 객체의 동작 커스터마이징.</span>
