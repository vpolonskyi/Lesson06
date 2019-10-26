def song(l: int = 3, lines: int = 3, ex: int = 0) -> str:
    """
    Генерирую песенку по заданным параметрам
    :param l: количество слов в строке
    :param lines: количество строк
    :param ex: чем закончить песенку (./!)
    :return: результат в str
    """
    assert l >= 1 and lines >= 1 and 0 <= ex <= 1
    lin = 'la'
    for i in range(1, l * lines):
        if i % l:
            lin = lin + '-la'
        else:
            lin = lin + '\nla'
    if ex == 0:
        return lin + '.'
    return lin + '!'


f = open("out.txt", "w")
f.write(song())
f.close()

f = open("..\\Lesson06\\task01.py", "r", encoding="utf8")
print(f.read())
f.close()

f = open("..\\Lesson06\\task01.py", "r", encoding="utf8")
for line in f:
    print(line.rstrip() + "!")
f.close()

f = open("out.txt", "r")
f1 = open("out2.txt", "w")
line = []
i = 0
for lin in f:
    i += 1
    line.append(str(i) + ". " + lin)
f1.writelines(line)
f.close()
f1.close()

with open("out.txt", "w") as f:
    f.write(song(10, 10))
