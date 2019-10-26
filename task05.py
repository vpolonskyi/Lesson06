with open("empl.txt", "r") as f:
    list_db = []
    empl = {}
    head = f.readline()
    head = head.split()
    for line in f:
        line = line.split()
        empl = {head[i]: line[i] for i in range(len(head))}
        list_db.append(empl)

# Посчитайте сколько отделов на фирме

otd = []
for i in range(len(list_db)):
    if otd.count((list_db[i].get("Отдел"))) == 0:
        otd.append((list_db[i].get("Отдел")))

print("Отделов на фирме: ", len(otd))

# Определите максимальную зарплату

print("Максимальная зарплата", max(list(int(list_db[i].get("Зарплата")) for i in range(len(list_db)))))

# Определите максимальную зарплату в каждом отделе

max_pay = {}
for i in list_db:
    if max_pay.get(i.get("Отдел")) is None:
        max_pay.update({i.get("Отдел"): i.get("Зарплата")})
    elif int(max_pay.get(i.get("Отдел"))) < int(i.get("Зарплата")):
        max_pay.update({i.get("Отдел"): i.get("Зарплата")})

print("Максимальная зарплата в каждом отделе", max_pay)

# Выведите «Отдел Макс_Зарплата  Фамилия_человека_с_такой_зарплатой» в новый файл

max_workers = []
for i in list_db:
    for ii in max_pay:
        if i.get("Отдел") == ii and i.get("Зарплата") == max_pay.get(ii):
            max_workers.append([i.get("Отдел"), i.get("Зарплата"), i.get("Фамилия")])

out = ''
for i in max_workers:
    out = str(i) + "\n" + out

with open("max_workers.txt", "w") as f:
    f.write(out)
