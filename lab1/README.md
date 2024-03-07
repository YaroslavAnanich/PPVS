# Классы Assistant, TicketSeller и Judge

Данные классы представляют собой ассистента, продавца билетов и судью соревнований.

## Класс Assistant

### Атрибуты Assistant

- `name`: имя ассистента

### Методы Assistant

- `__init__(self, name)`: конструктор класса, инициализирует объект ассистента с заданным именем.
- `get_assistant_name(self) -> str`: возвращает имя ассистента.

## Класс TicketSeller

### Наследование TicketSeller

- `Assistant`: наследует класс `Assistant`

### Атрибуты TicketSeller

- `tickets`: список объектов билета
- `ticket_price`: стоимость билета

### Методы TicketSeller

- `__init__(self, name)`: конструктор класса, инициализирует объект продавца билетов с заданным именем.
- `sell_ticket(self, tickets, ticket_price)`: продает билет из списка билетов и выводит информацию о продаже.

## Класс Judge

### Наследование Judge

- `Assistant`: наследует класс `Assistant`

### Атрибуты Judge

- `participants`: список участников соревнований
- `track`: объект трассы

### Методы Judge

- `__init__(self, name)`: конструктор класса, инициализирует объект судьи с заданным именем.
- `is_have_horse(self, participants)`: проверяет, имеет ли каждый участник лошадь.
- `is_have_track(self, track)`: проверяет, имеется ли информация о трассе.
- `set_places(self, places, participants, name, track)`: определяет места участников в соревнованиях и выводит информацию о результатах.

## Пример использования

```python
# Создание объектов
assistant = Assistant("Assistant")
ticket_seller = TicketSeller("TicketSeller")
judge = Judge("Judge")

# Создание билетов
tickets = [Ticket(1, "John"), Ticket(2, "Jane")]

# Продажа билета
ticket_seller.sell_ticket(tickets, 10)

# Создание участников и трассы
participants = [Participant(1, "John", Horse("Horse1", 10)), Participant(2, "Jane", Horse("Horse2", 9))]
track = Track("Track1", 200)

# Определение мест
judge.set_places(places, participants, "Race", track)
```
# Класс Track

Данный класс представляет собой объект трассы.

## Атрибуты
- `name`: название трассы
- `track_length`: длина трассы

## Методы
- `__init__(self, name=None, track_length=None)`: конструктор класса, инициализирует объект трассы с заданным названием и длиной.
- `get_name(self) -> str`: возвращает название трассы.
- `get_length(self) -> int`: возвращает длину трассы.

## Пример использования
```python
# Создание объекта трассы
track = Track("Track1", 200)

# Получение информации о трассе
track_name = track.get_name()
track_length = track.get_length()
````
# Класс Ticket

Данный класс представляет собой объект билета.

## Атрибуты
- `number`: номер билета
- `name`: имя владельца билета

## Методы
- `__init__(self, number, name)`: конструктор класса, инициализирует объект билета с заданным номером и именем.
- `get_ticket_number(self) -> int`: возвращает номер билета.
- `get_ticket_name(self) -> str`: возвращает имя владельца билета.

## Пример использования
```python
# Создание объекта билета
ticket = Ticket(12345, "John Doe")

# Получение информации о билете
ticket_number = ticket.get_ticket_number()
ticket_name = ticket.get_ticket_name()

# Класс Participant

### Атрибуты Participant

- `name`: имя участника
- `horse`: объект лошади

### Методы Participant

- `__init__(self, name, horse)`: конструктор класса, инициализирует объект участника с заданным именем и лошадью.
- `get_participant_name(self) -> str`: возвращает имя участника.
- `get_participant_horse(self) -> Horse`: возвращает объект лошади участника.
```
# Класс Horse

### Атрибуты Horse

- `name`: имя лошади
- `speed`: скорость лошади

### Методы Horse

- `__init__(self, name=None, speed=None)`: конструктор класса, инициализирует объект лошади с заданным именем и скоростью.
- `get_horse_name(self) -> str`: возвращает имя лошади.
- `get_horse_speed(self) -> int`: возвращает скорость лошади.

# Класс Tournament

### Атрибуты Tournament

- `name`: название турнира
- `ticket_price`: цена билета (целое число)
- `participants`: список участников
- `judge`: объект судьи
- `track`: объект трассы
- `tickets`: список билетов
- `ticket_seller`: объект продавца билетов
- `places`: словарь для хранения результатов мест участников

### Методы Tournament

- `__init__(self, name, ticket_price)`: конструктор класса, инициализирует объект турнира с заданным названием и ценой билета.
- `register_participant(self, name, horse=None, speed=None)`: регистрирует участника с указанным именем, лошадью и скоростью.
- `register_ticket_seller(self, name)`: регистрирует продавца билетов с указанным именем.
- `register_judge(self, name)`: регистрирует судью с указанным именем.
- `register_ticket(self, number, name)`: регистрирует билет с указанным номером и именем.
- `register_track(self, name=None, track_length=None)`: регистрирует трассу с указанным названием и длиной.
- `sell_ticket(self)`: продает билеты через зарегистрированного продавца билетов.
- `set_places(self)`: определяет места участников в турнире через зарегистрированного судью.

**Примечание:** В случае отсутствия зарегистрированного продавца билетов или судьи, будет выведено соответствующее сообщение об ошибке.
