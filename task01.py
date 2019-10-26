import requests


def book_exist(url: str, query: dict, sid: int = None) -> bool:
    """
    Проверяю есть ли книга с заданым именем и автором на странице url
    Если указан ID книги, то он тоже участвует в поиске
    """
    if sid is None:
        get = requests.get(url)
        for i in get.json():
            if i["title"] == query["title"] and i["author"] == query["author"]:
                return True
    else:
        get = requests.get(url + str(sid))
        if get.status_code == 200 and get.json()["title"] == query["title"] and get.json()["author"] == query["author"]:
            return True
    return False


def role_exist(url: str, query: dict, sid: int = None) -> bool:
    """
    Проверяю есть ли роль с заданными параметрами на странице url
    Если указан ID роли, то он тоже участвует в поиске
    """
    if sid is None:
        get = requests.get(url)
        for i in get.json():
            if i["name"] == query["name"] and i["type"] == query["type"]\
                    and i["level"] == query["level"] and i["book"] == query["book"]:
                return True
    else:
        get = requests.get(url + str(sid))
        if get.status_code == 200 and get.json()["name"] == query["name"] and get.json()["type"] == query["type"]\
                and get.json()["level"] == query["level"] and get.json()["book"] == query["book"]:
            return True
    return False


burl = 'http://pulse-rest-testing.herokuapp.com/books/'
bpush = {"title": "Bubology", "author": "Great Me"}

# Создаём книгу POST /books/, и запоминаем его id.

res = requests.post(burl, bpush)
bid = res.json()['id']

# Проверяем, что она создалась и доступна по ссылке GET/books/[id]

if book_exist(burl, bpush, bid):
    print("Искомая книга " + str(bpush) + " найдена " + burl + str(bid))

# Проверяю, что книга есть в списке книг по запросу GET /books/

if book_exist(burl, bpush):
    print("Искомая книга " + str(bpush) + " найдена на странице " + burl)

# Изменяю данные этой книги методом PUT /books/[id]/

new_bpush = {"title": "Bubology 2", "author": "Great Me"}

if book_exist(burl, bpush, bid):
    requests.put(burl + str(bid), new_bpush)

# Проверяю, что она изменилась и доступна по ссылке /books/[id]

if book_exist(burl, new_bpush, bid):
    print("Новая книга " + str(new_bpush) + " найдена " + burl + str(bid))

# Проверяю, что она есть в списке книг по GET /books/ с новыми данными.

if book_exist(burl, new_bpush):
    print("Новая книга " + str(new_bpush) + " найдена на странице " + burl)

# Создаю роль POST roles, вы запоминаю её id.

rurl = "http://pulse-rest-testing.herokuapp.com/roles/"
rpush = {"name": "Bubolog Hero", "type": "Junior topotun", "level": 3, "book": burl + str(bid)}

if book_exist(burl, new_bpush, bid):
    res = requests.post(rurl, rpush)
    rid = res.json()['id']

# Проверяю, что роль создалась и доступна по ссылке GET/roles/[id]

if role_exist(rurl, rpush, rid):
    print("Искомая роль " + str(rpush) + " найдена " + rurl + str(rid))

# Проверяю, что она есть в списке ролей по запросу GET /roles/

if role_exist(rurl, rpush):
    print("Искомая роль " + str(rpush) + " найдена на странице " + rurl)

# Изменяю данные этой роли методом PUT /roles/[id]/

new_rpush = {"name": "New Bubolog Hero", "type": "God of topotun", "level": 800, "book": burl + str(bid)}

if role_exist(rurl, rpush, rid):
    requests.put(rurl + str(rid), new_rpush)

# Проверяю, что роль изменилась и доступна по ссылке /roles/[id]

if role_exist(rurl, new_rpush, rid):
    print("Обновленная роль " + str(new_rpush) + " найдена " + rurl + str(rid))

# Проверяю, что обновленная роль есть в списке ролей по GET /roles/ с новыми данными.

if role_exist(rurl, new_rpush):
    print("Обновленная роль " + str(new_rpush) + " найдена на странице " + rurl)

# Удаляю роль методом DELETE /role/[id].

if role_exist(rurl, new_rpush, rid):
    requests.delete(rurl + str(rid))
    print(rurl + str(rid) + " deleted")

# Удаляю книгу методом DELETE /books/[id].

if book_exist(burl, new_bpush, bid):
    requests.delete(burl + str(bid))
    print(burl + str(bid) + " deleted")