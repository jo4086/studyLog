# Attribute Automation (속성 자동화)

### $\textsf{\color{navy}{α. Attribute란?}}$

-   **Attribute**는 클래스나 객체가 가지는 **데이터(변수)**를 의미합니다.
-   Python에서는 `self.attribute_name` 형식으로 클래스 내부에서 정의됩니다.

### $\textsf{\color{navy}{β. Attribute Automation이란?}}$

-   **Attribute Automation**은 클래스 내에서 `self.attribute = value`와 같은 작업을 **자동화**하여 반복성을 줄이고, 코드를 간결하게 만드는 기법입니다.
-   Python에서는 `setattr()` 또는 `locals()`와 같은 동적 속성 관리 메커니즘을 사용하여 구현할 수 있습니다.

---

### $\textsf{\color{blue}{1. Attribute 정의와 수동 초기화}}$

-   일반적으로, 클래스의 속성은 `__init__` 메서드에서 **수동으로 정의**됩니다.

<details>
<summary> $\sf{\small{\color{hotpink}{example}}}$ </summary>

```python
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# 사용 예시
person = Person("Alice", 25, "Seoul")
print(person.name, person.age, person.city)
# 출력: Alice 25 Seoul
```

### $\textsf{\color{blue}{2. Attribute Automation의 구현}}$

-   Python에서는 \*\*kwargs와 setattr()를 사용해 속성 설정을 자동화할 수 있습니다.
-   kwargs는 키-값 쌍을 받아 처리하며, setattr()로 속성을 동적으로 추가합니다.
<details> <summary> $\sf{\small{\color{hotpink}{example}}}$ </summary>

```python
class Person:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

# 사용 예시
person = Person(name="Alice", age=25, city="Seoul")
print(person.name, person.age, person.city)
# 출력: Alice 25 Seoul
```

</details>

### $\textsf{\color{blue}{3. Attribute Automation의 응용}}$

-   속성 초기화 자동화는 속성의 동적 추가 외에도, 데이터 유효성 검사 및 기본값 설정에 응용될 수 있습니다.
<details> <summary> $\sf{\small{\color{hotpink}{example: 기본값 설정}}}$ </summary>

```python
class Person:
    DEFAULTS = {"name": "Unknown", "age": 0, "city": "Unknown"}

    def __init__(self, **kwargs):
        for key, default_value in self.DEFAULTS.items():
            setattr(self, key, kwargs.get(key, default_value))

# 사용 예시
person = Person(name="Alice", city="Seoul")
print(person.name, person.age, person.city)
# 출력: Alice 0 Seoul
```

</details>

### $\textsf{\color{blue}{4. Attribute Automation의 장점}}$

1. 코드 간소화:
    - 반복적인 self.attribute = value 작업을 제거하여 코드가 간결해짐.
2. 유연성:
    - kwargs를 활용하면 속성 추가를 동적으로 처리할 수 있음.
3. 확장성:
    - 새로운 속성을 쉽게 추가하거나 수정 가능.

### $\textsf{\color{blue}{5. 참고}}$

-   setattr(): 객체의 속성을 동적으로 설정.
-   locals(): 현재 지역 변수 정보를 반환.
-   Python 공식 문서: Data Model - init
