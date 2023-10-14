"""Напишите класс MinMaxWordFinder. Класс должен уметь анализировать текст и находить в нём слова 
наименьшей и наибольшей длины. Текст состоит из предложений, которые добавляются в обработку 
методом add_sentence. Метод shortest_words возвращает список самых коротких на данный момент 
слов, метод longest_words — самых длинных. Слова, возвращаемые методами shortest_words и 
longest_words, должны быть отсортированы по алфавиту.

Если одно из самых коротких слов встретилось в исходных предложениях несколько раз, оно должно 
столько же раз повториться в списке самых коротких слов. Самые длинные слова наоборот должны 
входить в список без повторов."""


class MinMaxWordFinder:

    def __init__(self):
        self.list_obj = []

    def add_sentence(self, text: str):
        text_list = text.split()
        self.list_obj.extend(text_list)

    def shortest_words(self):
        lenght = len(self.list_obj[0])
        for i in range(1, len(self.list_obj)):
            if len(self.list_obj[i]) < lenght:
                lenght = len(self.list_obj[i])
        return sorted(filter(lambda x: len(x) == lenght, self.list_obj))

    def longest_words(self):
        lenght = len(self.list_obj[0])
        for i in range(1, len(self.list_obj)):
            if len(self.list_obj[i]) > lenght:
                lenght = len(self.list_obj[i])
        return sorted(set(filter(lambda x: len(x) == lenght, self.list_obj)))


x = MinMaxWordFinder()
x.add_sentence(
    "Константин Ольга Мария Елизавета Дмитрий Никита Анастасия Александра Николь Денис Константин Николай")
x.add_sentence(
    "Ярослав Александра Мария Валерия Марат Софья Даниил Константин Макар Мария Павел Ульяна Денис")

print(x.shortest_words())
print(x.longest_words())
print(x.list_obj)