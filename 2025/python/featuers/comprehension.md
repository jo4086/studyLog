# 컴프리헨션(_Comprehension_)
## 컴프리헨션(_Comprehension_)이란?
파이썬(_python_)의 고유한 기능 중 하나로 **코드를 간결하게 작성**하게 도와주는 문법적 설탕(_Syntactic Sugar_)이다.

## 컴프리헨션의 종류
#### 1. 리스트 컴프리헨션
- **목적**: 기존 데이터를 기반으로 새로운 리스트를 생성 및 반환
- **특징**: 가장 많이 사용되며, 간단한 데이터 변환에 적합

<details>
<summary> 예시코드 </summary>

>```python
># 기존 코드 (일반 for 루프)    
>numbers = [1, 2, 3, 4, 5]
>squared_numbers = []
>for num in numbers:
>    squared_numbers.append(numm ** 2)
>print(squared_numbers)
>```
>```python
># 리스트 컴프리헨션
>numbers = [1, 2, 3, 4, 5]
>squared_numbers = [num ** 2 for num in numbers]
>print(squared_numbers)
>```
> **결과**:`[1, 4, 9, 16, 25]`


```python
squares = [x**2 for x in range(5)]
print(squares) # [0, 1, 4, 9, 16]
```

</details>

#### 2. 딕셔너리 컴프리헨션
#### 3. 집합 컴프리헨션
#### 4. 제너레이터 표현식

##### 5. ㅇㅇ
##### 6. ㅇㅇ