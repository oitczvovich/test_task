import wikipediaapi
import string


ALPHABET = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л',
    'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш',
    'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
]
wiki = wikipediaapi.Wikipedia('ru')
page = wiki.page('Категория:Животные по алфавиту')


def animal_letter_count():
    """ Получаем список животных по русскому алфавиту.
    Подсчитываем количество животных на каждую букву.
    """
    animals_letters = [
        cat.title[0] for cat in page.categorymembers.values() if
        cat.title[:] not in string.ascii_uppercase and string.punctuation
    ]

    for letter in ALPHABET:
        print(letter, ':', animals_letters.count(letter))


if __name__ == '__main__':
    animal_letter_count()
