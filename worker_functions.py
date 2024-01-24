import folium
from sql_classes import Worker
from SQL_db_params import *
from cords_functions import *


### PRACOWNICY ###

### DODAWANIE ###
def insert_worker():
    name = input('Podaj imię pracownika: ')
    lastname = input('Podaj nazwisko pracownika: ')
    city = input('Podaj miejscowość pracownika: ')
    function = input('Podaj funkcję pracownika: ')
    id_workplace = input('Podaj numer oddziału: ')

    add = Worker(name, lastname, city, function, id_workplace)
    session.add(add)
    session.commit()

### WYŚWIETLANIE WSZYSTKICH ###
def select_all_workers():
    workers_from_db = session.query(Worker).all()
    if workers_from_db == []:
        print('Brak danych')
    else:
        for id, worker in enumerate(workers_from_db):
            print(f"{id+1}. Pracownik {worker.name} {worker.lastname} - oddział nr {worker.id_workplace}")


### WYŚWIETLANIE WSZYSTKICH Z JEDNEGO ODDZIAŁU ###
def select_workers_oneplace():
    id_place = input('Podaj numer oddziału: ')
    workers_from_db = session.query(Worker).filter(Worker.id_workplace==id_place).all()
    if workers_from_db == []:
        print('Brak danych')
    else:
        for id, worker in enumerate(workers_from_db):
            print(f"{id + 1}. Pracownik {worker.name} {worker.lastname} - oddział nr {worker.id_workplace}")


### WYŚWIETLANIE WSZYSTKICH O JEDNEJ FUNKCJI ###
def select_workers_onetype():
    type = input('Podaj funkcję: ')
    workers_from_db = session.query(Worker).filter(Worker.function==type).all()
    if workers_from_db == []:
        print('Brak danych')
    else:
        for id, worker in enumerate(workers_from_db):
            print(f"{id + 1}. Pracownik {worker.name} {worker.lastname} - oddział nr {worker.id_workplace}")


### USUWANIE PRACOWNIKÓW ###
def delete_workers():
    todelete  = input('Podaj nawisko pracownika: ')
    workers_from_db = session.query(Worker).filter(Worker.lastname==todelete).all()

    temp_list = []

    for worker in workers_from_db:
        if worker.lastname == todelete:
            temp_list.append(worker)
    print('Znaleziono następujących pracowników: ')
    print('0 - Usuń wszystkich')

    for id, worker in enumerate(temp_list):
        print(f"{id+1} - Pracownik {worker.name} {worker.lastname} pełniący funkcję {worker.function}")
    number = int(input('Wybierz pracownika do usunięcia: '))

    if number == 0:
        for worker in temp_list:
            session.delete(worker)
    else:
        number2 = temp_list[number-1]
        session.delete(number2)

    session.commit()


### USUWANIE PRACOWNIKÓW Z JEDNEGO ODDZIAŁU ###
def delete_workers_oneplace():
    todelete = input('Podaj numer oddziału: ')
    workers_from_db = session.query(Worker).filter(Worker.id_workplace==todelete)

    temp_list = []

    for worker in workers_from_db:
        temp_list.append(worker)
    print('Znaleziono następujących pracowników z tego oddziału: ')
    print('0 - Usuń wszystkich')

    for id, worker in enumerate(temp_list):
        print(f"{id+1} - Pracownik {worker.name} {worker.lastname} pełniący funkcję {worker.function}")
    number = int(input('Wybierz pracownika do usunięcia: '))

    if number == 0:
        for worker in temp_list:
            session.delete(worker)
    else:
        number2 = temp_list[number-1]
        session.delete(number2)

    session.commit()


### USUWANIE PRACOWNIKÓW O DANEJ FUNKCJI ###
def delete_workers_onetype():
    todelete = input('Podaj funkcję pracowników: ')
    workers_from_db = session.query(Worker).filter(Worker.function == todelete)

    temp_list = []

    for worker in workers_from_db:
        temp_list.append(worker)
    print('Znaleziono następujących pracowników o tej funkcji: ')
    print('0 - Usuń wszystkich')

    for id, worker in enumerate(temp_list):
        print(f"{id + 1} - Pracownik {worker.name} {worker.lastname} z oddziału nr {worker.id_workplace}")
    number = int(input('Wybierz pracownika do usunięcia: '))

    if number == 0:
        for worker in temp_list:
            session.delete(worker)
    else:
        number2 = temp_list[number - 1]
        session.delete(number2)

    session.commit()


### AKTUALIZACJA DANYCH PRACOWNIKÓW ###
def update_workers():
    edit = input('Podaj nazwisko pracownika: ')
    workers_from_db = session.query(Worker).all()
    for worker in workers_from_db:
        if worker.lastname == edit:
            worker.name = input('Podaj nowe imię pracownika: ')
            worker.lastname = input('Podaj nowe nazwisko pracownika: ')
            worker.city = input('Podaj nową miejscowość pracownika: ')
            worker.function = input('Podaj nową funkcję pracownika: ')
            worker.id_workplace = input('Podaj nowy numer oddziału: ')
            worker.location = f"POINT({get_cordinates(worker.city)[1]} {get_cordinates(worker.city)[0]}"
    session.commit()


### AKTUALIZACJA DANYCH PRACOWNIKÓW Z JEDNEGO ODDZIAŁU ###
def update_workers_oneplace():
    edit = input('Podaj numer oddziału: ')
    workers_from_db = session.query(Worker).filter(Worker.id_workplace == edit)

    temp_list = []

    for worker in workers_from_db:
        if worker.id_workplace == edit:
            temp_list.append(worker)
    print('Znaleziono następujących pracowników z tego oddziału: ')

    for id, worker in enumerate(temp_list):
        print(f"{id + 1} - Pracownik {worker.name} {worker.lastname} pełniący funkcję {worker.function}")
    number = int(input('Wybierz pracownika do edycji: '))

    temp1_list = []

    for worker in temp_list:
        number2 = temp_list[number-1]
        temp1_list.append(number2)

    for worker in temp1_list:
        worker.name = input('Podaj nowe imię pracownika: ')
        worker.lastname = input('Podaj nowe nazwisko pracownika: ')
        worker.city = input('Podaj nową miejscowość pracownika: ')
        worker.function = input('Podaj nową funkcję pracownika: ')
        worker.id_workplace = input('Podaj nowy numer oddziału: ')
        worker.location = f"POINT({get_cordinates(worker.city)[1]} {get_cordinates(worker.city)[0]}"
    session.commit()


### AKTUALIZACJA DANYCH PRACOWNIKÓW O DANEJ FUNKCJI ###
def update_workers_onetype():
    edit = input('Podaj funkcję pracowników: ')
    workers_from_db = session.query(Worker).filter(Worker.function == edit)

    temp_list = []

    for worker in workers_from_db:
        if worker.id_workplace == edit:
            temp_list.append(worker)
    print('Znaleziono następujących pracowników z tego oddziału: ')

    for id, worker in enumerate(temp_list):
        print(f"{id + 1} - Pracownik {worker.name} {worker.lastname} pełniący funkcję {worker.function}")
    number = int(input('Wybierz pracownika do edycji: '))

    temp1_list = []

    for worker in temp_list:
        number2 = temp_list[number - 1]
        temp1_list.append(number2)

    for worker in temp1_list:
        worker.name = input('Podaj nowe imię pracownika: ')
        worker.lastname = input('Podaj nowe nazwisko pracownika: ')
        worker.city = input('Podaj nową miejscowość pracownika: ')
        worker.function = input('Podaj nową funkcję pracownika: ')
        worker.id_workplace = input('Podaj nowy numer oddziału: ')
        worker.location = f"POINT({get_cordinates(worker.city)[1]} {get_cordinates(worker.city)[0]}"
    session.commit()


### MAPA PRACOWNIKÓW ###
def map_all_workers():
    map = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)
    workers_from_db = session.query(Worker).all()
    for worker in workers_from_db:
        cordy = get_cordinates(worker.city)
        folium.Marker(location=cordy, popup=f"Tu mieszka {worker.name} {worker.lastname}").add_to(map)
    print('\n Wygenerowano mapę')
    map.save(f'mapa_wszystkich_pracownikow.html')


### MAPA PRACOWNIKÓW Z JEDNEGO ODDZIAŁU ###
def map_oneplace_workers():
    map = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)

    mapselect = input('Podaj numer oddziału: ')
    workers_from_db = session.query(Worker).filter(Worker.id_workplace == mapselect)

    for worker in workers_from_db:
        cordy = get_cordinates(worker.city)
        folium.Marker(location=cordy, popup=f"Tu mieszka {worker.name} {worker.lastname}").add_to(map)
        print('\n Wygenerowano mapę')
        map.save(f'mapa pracowników z oddziału {worker.id_workplace}.html')


### MAPA PRACOWNIKÓW O DANEJ FUNKCJI ###
def map_onetype_workers():
    map = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)

    mapselect = input('Podaj nazwę funkcji pracowników: ')
    workers_from_db = session.query(Worker).filter(Worker.function == mapselect)

    for worker in workers_from_db:
        cordy = get_cordinates(worker.city)
        folium.Marker(location=cordy, popup=f"Tu mieszka {worker.name} {worker.lastname}").add_to(map)
        print('\n Wygenerowano mapę')
        map.save(f'mapa pracowników o funkcji {worker.function}.html')


