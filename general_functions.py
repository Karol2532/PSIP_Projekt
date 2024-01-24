from worker_functions import *
from workplace_functions import *

    ### FUNKCJE ###


### LOGOWANIE ###
def login_to_sys():
    while True:
        login = input('Podaj login: ')
        password = input('Podaj hasło: ')
        if ((login == 'geoinformatyka')
        and (password == 'rzadzi')):
            GUI()
            break
        else:
            print('Logowanie się nie powiodło')
            print('Spróbuj ponownie')


### INTERFEJS ###
def GUI():
    while True:
        print('\nWitaj w systemie firmy InterSpecialists\n'
              f'0 - Wyłącz system\n'
              f'1 - Wyświetl wszystkich pracowników\n'
              f'2 - Wyświetl pracowników z wybranego oddziału\n'
              f'3 - Wyświetl pracowników o danej funkcji\n'
              f'4 - Wyświetl wszystkie oddziały\n'
              f'5 - Dodaj nowego pracownika\n'
              f'6 - Dodaj nowy oddział\n'
              f'7 - Usuń pracownika\n'
              f'8 - Usuń pracownika z wybranego oddziału\n'
              f'9 - Usuń pracownika o danej funkcji\n'
              f'10 - Usuń oddział\n'
              f'11 - Aktualizuj dane pracownika\n'
              f'12 - Aktualizuj dane pracownika z wybranego oddziału\n'
              f'13 - Aktualizuj dane pracownika o danej funkcji\n'
              f'14 - Aktualizuj dane oddziału\n'
              f'15 - Wygeneruj mapę wszystkich pracowników\n'
              f'16 - Wygeneruj mapę pracowników z danego oddziału\n'
              f'17 - Wygeneruj mapę pracowników o danej funkcji\n'
              f'18 - Wygeneruj mapę wszystkich oddziałów\n')

        option = int(input('Wybierz funkcję do wykonania: '))
        print(f'Wybrano funkcję {option}\n')

        match option:
            case 0:
                print('Wyłączam system')
                session.flush()
                engine.dispose()
                break
            case 1:
                print('Wyświetlam listę wszystkich pracowników')
                select_all_workers()
            case 2:
                print('Wyświetlam listę pracowników z danego oddziału')
                select_workers_oneplace()
            case 3:
                print('Wyświetlam listę pracowników o danej funkcji')
                select_workers_onetype()
            case 4:
                print('Wyświetlam wszystkie oddziały')
                select_all_workplaces()
            case 5:
                print('Dodaje nowego użytkownika')
                insert_worker()
            case 6:
                print('Dodaje nowy oddział')
                insert_workplace()
            case 7:
                print('Usuwam pracownika')
                delete_workers()
            case 8:
                print('Usuwam pracownika z danego oddziału')
                delete_workers_oneplace()
            case 9:
                print('Usuwam pracownika o danej funkcji')
                delete_workers_onetype()
            case 10:
                print('Usuwam oddział')
                delete_workplaces()
            case 11:
                print('Aktualizuje dane pracownika')
                update_workers()
            case 12:
                print('Aktualizuje dane pracownika z danego oddziału')
                update_workers_oneplace()
            case 13:
                print('Aktualizuje dane pracownika o danej funkcji')
                update_workers_onetype()
            case 14:
                print('Aktualizuje dane oddziału')
                update_workplaces()
            case 15:
                print('Generuję mapę wszystkich pracowników')
                map_all_workers()
            case 16:
                print('Generuję mapę pracowników z danego oddziału')
                map_oneplace_workers()
            case 17:
                print('Generuję mapę pracowników o danej funkcji')
                map_onetype_workers()
            case 18:
                print('Generuję mapę wszystkich oddziałów')
                map_all_workplaces()