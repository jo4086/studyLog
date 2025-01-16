# Argument

### $\textsf{\color{navy}{α. Argument란?}}$

-   함수 실행시 파라미터(**parameter**)에 전달되는 실제 값
-   `위치`, `키워드`, `기본값`, `가변길이`, `가변키워드` 등 다양한 방식으로 전달

<details>
<summary> $\sf{\small{\color{hotpink}{example}}}$ </summary>

```python
def add(a, b):   # [a, b]: Parameter
    return a + b

print(add(2, 3)) # [2, 3]: Argument
```

<details>
<summary> $\sf{\color{red}{result}}$ </summary>

```diff
! result
5
```

</details>
</details>

---

### $\textsf{\color{navy}{β. 함수의 5가지 입력 방식}}$

<details>
<summary> $\textbf{\color{blue}{1. Positional Arguments{\textsf{(위치 인수)}}}}$ </summary>

-   아규먼트가 **순서**에 따라 파라미터에 매핑
-   단점: `parameter`가 많을 경우 가독성 저하

  <details>
  <summary> $\sf{\small{\color{hotpink}{example}}}$ </summary>

  ```python
  def greet(name, age):
      print(f"{name} is {age} years old.")

  greet("Alice", 25)  # 출력: Alice is 25 years old.
  ```

  </details>
</details>

<details>
<summary> $\textbf{\color{blue}{2. Keyword Arguments{\textsf{(키워드 인수)}}}}$ </summary>

-   순서와 관계없이 특정 파라미터에 값을 할당할 수 있음.
-   아규먼트 이름을 명시적으로 지정하여 전달.
-   단점: 호출 시 `parameter`명을 모두 명시하므로 코드가 난잡해짐

  <details>
  <summary> $\sf{\small{\color{hotpink}{example}}}$ </summary>

  ```python
  def greet(name, age):
      print(f"{name} is {age} years old.")

  greet(age=25, name="Alice")  # 출력: Alice is 25 years old.
  ```

  </details>
</details>

<details>
<summary> $\textbf{\color{blue}{3. Default Arguments{\textsf{(기본값 인수)}}}}$ </summary>

-   함수 정의 시 기본값을 지정하면, 호출 시 해당 값을 생략 가능.

  <details>
  <summary> $\sf{\small{\color{hotpink}{example}}}$ </summary>

  ```python
  def greet(name="Guest"):
      return f"Hello, {name}!"

  print(greet())           # 출력: Hello, Guest!
  print(greet("Alice"))    # 출력: Hello, Alice!
  ```

  </details>
</details>

<details>
<summary> $\textbf{\color{blue}{4. Variable-Positional Arguments{\textsf{(가변 위치 인수)}}}}$ </summary>

-   전달되는 아규먼트의 개수가 정해지지 않았을 때 사용.
-   `*args`: 가변 위치 인수, 튜플 형태로 전달.

  <details>
  <summary> $\sf{\small{\color{hotpink}{example}}}$ </summary>

  ```python
  def add_all(*args):
      return sum(args)

  print(add_all(1, 2, 3, 4))  # 출력: 10
  print(add_all(5))           # 출력: 5
  ```

  </details>
</details>

<details>
<summary> $\textbf{\color{blue}{5. Variable-Keyword Arguments{\textsf{(가변 키워드 인수)}}}}$ </summary>

-   전달되는 아규먼트의 개수가 정해지지 않았을 때 사용.
-   `**kwargs`: 가변 키워드 인수, 딕셔너리 형태로 전달.

  <details>
  <summary> $\sf{\small{\color{hotpink}{example}}}$ </summary>

  ```python
  def describe_person(**kwargs):
      for key, value in kwargs.items():
          print(f"{key}: {value}")
  describe_person(name="Alice", age=25, hobby="reading")
  # 출력:
  # name: Alice
  # age: 25
  # hobby: reading
  ```

  </details>
</details>
