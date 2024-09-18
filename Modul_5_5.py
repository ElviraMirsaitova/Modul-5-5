class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self, title, duration,time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = 0


    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user


    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        for i in self.users:
            if i.nickname == user.nickname:
                return print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(user)
            self.current_user = user

    def log_out(self):
        self.current_user = None
        return self.current_user

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)


    def get_videos(self, word):
        list1 = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                list1.append(video.title)
        return list1

    def watch_video(self, name):
        if self.current_user == 0:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if name == video.title:
                if video.adult_mode == True:
                    if self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        return

                from time import sleep
                while video.time_now < video.duration:
                    video.time_now = video.time_now + 1
                    sleep(1)
                    print(f'{video.time_now} ', end='')
                print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')












