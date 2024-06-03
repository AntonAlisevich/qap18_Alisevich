# Тема проекта: приложение «Касса кинотеатра».
# Спроектировать ПО, предназначенное для автоматизации деятельности кассы
# кинотеатра. Функции, которые должны быть реализованы в приложении:
# добавление, удаление, редактирование и просмотр информации о сеансах,
# наличии билетов и свободных мест.

class Kassa:
    def __init__(self, seans: list):
        self.seans: list = seans

# Не могу понять как связать Кассу и Сеанс вместе так что бы реализовать функционал получения информации обо всех
# сеансах. Условно: я задал сеанс1 и сеанс2 с определенными параметрами и при вызовеве метода информации о сеансах
# я получаю список со всеми сеансами который хотя бы включает название сеанса.


class Seans:
    def __init__(self, title: str, place: int, tickets: int):
        self.place: int = place
        self.tickets: int = tickets
        self.title: str = title

    def number_of_places(self):
        print(self.place)

    def number_of_tickets(self):
        print(self.tickets)

    def getting_informatiom(self):
        if self.place > 0 and self.tickets > 0:
            availability = "Seans is Available"
        else:
            availability = "Seans is Not available. Tickets are SOLD OUT"
        print(f"{self.title}; {availability} Places:{self.place}, Tickets:{self.tickets}")

    def editing_information(self, new_title, new_place, new_tickets):
        self.title = new_title
        self.place = new_place
        self.tickets = new_tickets

    def buying_tickets(self, n_tickets: int):
        if n_tickets <= self.tickets:
            self.tickets -= n_tickets
            self.place = self.tickets
        else:
            print(f"{self.tickets} tickets available")

    def returning_tickets(self, n_tickets):
        self.tickets += n_tickets
        self.place = self.tickets


seans1 = Seans("Star Wars", 15, 15)
# Получил инфо о сеанс1
seans1.getting_informatiom()
# Отредактировал сеанс1
seans1.editing_information("Barbarian", 2, 2)
# Снова получил инфо о сеанс1
seans1.getting_informatiom()
# Создал сеанс2
seans2 = Seans("Animation", 115, 115)
# Получил инфо о сеанс2
seans2.getting_informatiom()
# Попытался купить больше билетов на сеанс1 чем доступно
seans1.buying_tickets(22)
# Сдали билетов на сеанс1
seans1.returning_tickets(25)
# Получил инфо о сеанс1
seans1.getting_informatiom()
# Купил все билеты на сеанс1
seans1.buying_tickets(27)
# Инфо на сеанс1 для которого все билеты проданы
seans1.getting_informatiom()
