import time


class User():
    def __init__(self, nickname: str, password: int, age: int) -> None:
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)


class Video():
    def __init__(self, title: str, duration: int) -> None:
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False


class Urtube():
    def __init__(self, users: list[User], videos: list[Video], current_user: User) -> None:
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, login, password):
        if (login, password) in self.users:
            self.current_user = User(login, password)

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        if not User(nickname=nickname) in self.users():
            self.users.append(User(nickname, password, age))
        else:
            print(f"Пользователь {nickname} уже существует")
            self.log_in(nickname, password)

    def add(self, *args: Video):
        if args.title not in self.videos:
            self.videos.append(args)

    def get_videos(self, search_word):
        for title in self.videos:
            if search_word.upper() in title.upper():
                return title

    def watch_video(self, title):
        for movie in self.videos:
            if movie.title == title:
                cur_dur = 0
                while cur_dur != movie.duration:
                    movie.duration = cur_dur
                    print(f"Видео идет на {cur_dur} секунде")
                    time.sleep(4)
