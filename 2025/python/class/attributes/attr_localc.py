class Character:
    def __init__(self, name, hp, mp, df, mdf, atk, matk, action_speed):
        # 현재 함수의 로컬 변수들 (name, hp, mp 등)을 가져와 self에 추가
        for key, value in locals().items():
            if key != "self":  # self는 제외
                setattr(self, key, value)

    def status(self):
        return "\n".join(f"{attr}: {value}" for attr, value in self.__dict__.items())

# 사용 예제
hero = Character(name="Hero", hp=100, mp=50, df=10, mdf=10, atk=15, matk=15, action_speed=5)
print(hero.status())

