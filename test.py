import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from geopy.geocoders import Nominatim


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("InterSpecialists System")
        self.geometry("800x600")

        # Tworzenie zakładek
        tab_control = ttk.Notebook(self)

        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)

        tab_control.add(tab1, text='Workers')
        tab_control.add(tab2, text='Workplaces')

        tab_control.pack(expand=1, fill="both")

        # Inicjalizacja bazy danych (można dostosować do swojego środowiska)
        self.db_init()

        # Workers Tab
        self.create_workers_widgets(tab1)

        # Workplaces Tab
        self.create_workplaces_widgets(tab2)

    def db_init(self):
        # Tutaj możesz dodać kod inicjalizujący bazę danych lub połączenie z bazą danych
        # W tym przykładzie, połączenie do bazy danych zostało umieszczone w metodzie
        # W rzeczywistym projekcie, możesz użyć SQLAlchemy do lepszej obsługi bazy danych

        self.workers_data = [
            {"name": "John", "lastname": "Doe", "city": "New York", "function": "Manager", "id_workplace": 1},
            {"name": "Alice", "lastname": "Smith", "city": "Los Angeles", "function": "Developer", "id_workplace": 2}
        ]

        self.workplaces_data = [
            {"name": "Headquarters", "city": "New York", "country": "USA", "id_workplace": 1},
            {"name": "Branch Office", "city": "Los Angeles", "country": "USA", "id_workplace": 2}
        ]

    def create_workers_widgets(self, tab):
        label = tk.Label(tab, text="Workers", font=("Helvetica", 16))
        label.pack(pady=10)

        # Wyświetlanie pracowników
        btn_show_workers = tk.Button(tab, text="Show Workers", command=self.show_workers)
        btn_show_workers.pack(pady=5)

        # Dodawanie pracownika
        btn_add_worker = tk.Button(tab, text="Add Worker", command=self.add_worker)
        btn_add_worker.pack(pady=5)

    def create_workplaces_widgets(self, tab):
        label = tk.Label(tab, text="Workplaces", font=("Helvetica", 16))
        label.pack(pady=10)

        # Wyświetlanie oddziałów
        btn_show_workplaces = tk.Button(tab, text="Show Workplaces", command=self.show_workplaces)
        btn_show_workplaces.pack(pady=5)

        # Dodawanie oddziału
        btn_add_workplace = tk.Button(tab, text="Add Workplace", command=self.add_workplace)
        btn_add_workplace.pack(pady=5)

    def show_workers(self):
        workers_text = "\n".join(
            [f"{worker['name']} {worker['lastname']} - {worker['function']}" for worker in self.workers_data])
        messagebox.showinfo("Workers List", workers_text)

    def add_worker(self):
        # Przykładowa funkcja dodająca pracownika
        name = tk.simpledialog.askstring("Add Worker", "Enter name:")
        lastname = tk.simpledialog.askstring("Add Worker", "Enter lastname:")
        city = tk.simpledialog.askstring("Add Worker", "Enter city:")
        function = tk.simpledialog.askstring("Add Worker", "Enter function:")
        id_workplace = tk.simpledialog.askinteger("Add Worker", "Enter id_workplace:")

        # Tutaj można dodać kod dodający pracownika do bazy danych
        self.workers_data.append(
            {"name": name, "lastname": lastname, "city": city, "function": function, "id_workplace": id_workplace})
        messagebox.showinfo("Add Worker", "Worker added successfully!")

    def show_workplaces(self):
        workplaces_text = "\n".join(
            [f"{workplace['name']} - {workplace['city']}, {workplace['country']}" for workplace in
             self.workplaces_data])
        messagebox.showinfo("Workplaces List", workplaces_text)

    def add_workplace(self):
        # Przykładowa funkcja dodająca oddział
        name = tk.simpledialog.askstring("Add Workplace", "Enter name:")
        city = tk.simpledialog.askstring("Add Workplace", "Enter city:")
        country = tk.simpledialog.askstring("Add Workplace", "Enter country:")
        id_workplace = tk.simpledialog.askinteger("Add Workplace", "Enter id_workplace:")

        # Tutaj można dodać kod dodający oddział do bazy danych
        self.workplaces_data.append({"name": name, "city": city, "country": country, "id_workplace": id_workplace})
        messagebox.showinfo("Add Workplace", "Workplace added successfully!")


if __name__ == "__main__":
    app = Application()
    app.mainloop()