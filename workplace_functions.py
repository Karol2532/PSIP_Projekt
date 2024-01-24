import folium
from sql_classes import Workplace
from SQL_db_params import *
from cords_functions import *

### ODDZIAŁY ###

### DODAWANIE ODDZIAŁÓW ###
def insert_workplace():
    name = input('Podaj nazwę oddziału: ')
    city = input('Podaj nazwę miejscowości: ')
    country = input('Podaj nazwę kraju: ')
    id_workplace = input('Podaj numer oddziału: ')

    add = Workplace(name, city, country, id_workplace)
    session.add(add)
    session.commit()


### WYŚWIETLANIE ODDZIAŁÓW ###
def select_all_workplaces():
    workplaces_from_db = session.query(Workplace).all()
    if workplaces_from_db == []:
        print('Brak danych')
    else:
        for id, workplace in enumerate(workplaces_from_db):
            print(f"{id+1}. Oddział {workplace.name} nr {workplace.id_workplace} w miejscowości {workplace.city}")


### USUWANIE ODDZIAŁÓW ###
def delete_workplaces():
    todelete = input('Podaj nazwę oddziału: ')
    workplaces_from_db = session.query(Workplace).filter(Workplace.name==todelete)

    temp_list =[]

    for workplace in workplaces_from_db:
        if workplace.name == todelete:
            temp_list.append(workplace)
    print('Znaleziono następujące oddziały: ')
    print('0 - Usuń wszystkie')

    for id, workplace in enumerate(temp_list):
        print(f"{id+1} - Oddział {workplace.name} numer {workplace.id_workplace}")
    number = int(input('Wybierz oddział do usunięcia: '))

    if number == 0:
        for workplace in temp_list:
            session.delete(workplace)
    else:
        number2 = temp_list[number-1]
        session.delete(number2)

    session.commit()


### AKTUALIZACJA DANYCH ODDZIAŁÓW ###
def update_workplaces():
    edit = input('Podaj nazwę oddziału: ')
    workplaces_from_db = session.query(Workplace).all()
    for workplace in workplaces_from_db:
        if workplace.name == edit:
            workplace.name = input('Podaj nową nazwę oddziału: ')
            workplace.city = input('Podaj nową nazwę miejscowości: ')
            workplace.country = input('Podaj nową nazwę kraju: ')
            workplace.id_workplace = input('Podaj nowy numer oddziału: ')
            workplace.location = f"POINT({get_cordinates(workplace.city)[1]} {get_cordinates(workplace.city)[0]})"
    session.commit()


### MAPA ODDZIAŁÓW ###
def map_all_workplaces():
    map = folium.Map(location=[48.7, 18.9], tiles='OpenStreetMap', zoom_start=5)
    workplace_from_db = session.query(Workplace).all()
    for workplace in workplace_from_db:
        cordy = get_cordinates(workplace.city)
        folium.Marker(location=cordy, popup=f"{workplace.name}").add_to(map)
    print('\n Wygenerowano mapę')
    map.save(f'mapa_wszystkich_oddzialow.html')