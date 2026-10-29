"""Демонстрационный модуль для задания 1556 (Git + PEP 8)."""


def greet(name):
    """Возвращает приветствие для указанного имени."""
    return "Привет, " + name + "!"

def calc_sum( x,y ):
        result=x+y
        return result

if __name__ == "__main__":
    print(greet("мир"))
    print( calc_sum(1,2) )
