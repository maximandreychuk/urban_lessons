"""
Задание "Свой YouTube":

Университет Urban подумывает о создании своей платформы, 
где будут размещаться дополнительные полезные ролики на тему IT 
(юмористические, интервью и т.д.). 
Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.

Именно вам выпала возможность продемонстрировать их, 
написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:

Реализовать классы для взаимодействия с платоформой, 
каждый из которых будет содержать методы добавления видео, 
авторизации и регистрации пользователя и т.д.
"""


import time


class User():
    def __init__(self, nickname: str, password: int, age: int) -> None:
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return self.nickname


class Video():
    def __init__(self, title: str,
                 duration: int,
                 time_now: int = 0,
                 adult_mode: bool = False) -> None:
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube():
    def __init__(self,
                 users: list[User] = [],
                 videos: list[Video] = [],
                 current_user: User = None) -> None:
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def register(self, nickname, password, age):
        for obj in self.users:
            if obj.nickname == nickname:
                return print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Регистрация пользователя {new_user.nickname} пройдена")

    def log_in(self, login, password):
        for obj in self.users:
            if obj.nickname == login and obj.password == password:
                self.cur = User(login, password)
                return print(f"Поздравляю, {self.cur}, вы зашли на платформу Urtube")
            else:
                return print("Для начала пройдите регистрацию")

    def log_out(self):
        self.current_user = None

    def add(self, *args: Video):
        for obj in args:
            if obj.title not in self.videos:
                self.videos.append(obj)
            else:
                pass

    def get_videos(self, search_word):
        found = []
        for obj in self.videos:
            if search_word.upper() in obj.title.upper():
                found.append(obj.title)
        return found

    def watch_video(self, title):
        if not self.current_user:
            return print("Войдите в аккаунт чтобы смотреть видео")
        else:
            for movie in self.videos:
                if movie.title == title:
                    if self.current_user.age < 18 and movie.adult_mode == True:
                        return print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        while movie.time_now <= movie.duration:
                            print(
                                f"Фильм '{title}' идет на {movie.time_now} секунде"
                            )

                            time.sleep(4)
                            movie.time_now += 4
                        movie.time_now = 0
                        print("Конец видео")
            for movie in self.videos:
                if movie.title != title:
                    return print("Видео не существует")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года!', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень?', 111, adult_mode=True)
v4 = Video('Для чего девушкам девушка?', 8)


# - - - - - - - - - - - - - - - - -  Тесты  - - - - - - - - - - - - - - - - - -
# Добавление видео
ur.add(v1, v2, v3, v4)

# Проверка поиска
print("- - - - -Проверка поиска - - - - -")
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
print("- - - - - Проверка на вход пользователя и возрастное ограничение - - - - -")
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
print("- - - - - Проверка входа в другой аккаунт - - - - -")
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
print("- - - - - Попытка воспроизведения несуществующего видео - - - - -")
ur.watch_video('Для кого?')
