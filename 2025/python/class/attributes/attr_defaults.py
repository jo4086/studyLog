class Character:
    DEFAULTS = {
        "NAME": "Unnamed",
        "HP": 100,
        "MP": 50,
        "DF": 10,
        "m_DF": 10,
        "ATK": 15,
        "m_ATK": 15,
        "SPEED": 5,
    }

    def __init__(self, **kwargs):
        for key, default_value in self.DEFAULTS.items():
            setattr(self, key, kwargs.get(key, default_value))

    def status(self):
        return "\n".join(f"{attr}: {value}" for attr, value in self.__dict__.items())

# 사용 예제
hero = Character(NAME="Hero", HP=120, ATK=18, m_ATK=10, DF=16, m_DF=12, SPEED=7)
mage = Character(NAME="Mage", m_ATK=20, DF=8)
normal = Character(NAME="Normal")

print(hero.status(), "\n")
print(mage.status(), "\n")
print(normal.status(), "\n")
