print('Привет! Это программа с объяснением современных словечек')

meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            'АГРИТЬСЯ': 'злиться',
            'ЧИНАЗЕС': 'Очень круто',
            'ТРЕНД': 'что-то модное',
            'ДЕДЛАЙН': 'Крайние сроки сдачи работы',
            'КОМФОРТИК': 'Милый человек',
            'ЧЕЧИК': 'Неопределенный парень, нейтральная окраска описывающая молодого человека'
            }
            
word = input("Введите непонятное слово (большими буквами!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('даже я такое не знаю..')
