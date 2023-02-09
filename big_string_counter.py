"""
📌 В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10
самых частых. Не учитывать знаки препинания и регистр символов. За основу
возьмите любую статью из википедии или из документации к языку.
"""

big_string = 'Python was conceived in the late 1980s[42] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) ' \
             'in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,' \
             '[43] capable of exception handling and interfacing with the Amoeba operating system.[13] Its ' \
             'implementation began in December 1989.[44] Van Rossum shouldered sole responsibility for the project, ' \
             'as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his ' \
             'responsibilities as Python\'s "benevolent dictator for life", a title the Python community bestowed ' \
             'upon him to reflect his long-term commitment as the project\'s chief decision-maker.[45] In January ' \
             '2019, active Python core developers elected a five-member Steering Council to lead the project.'\
    .lower().split()

res = set()
for i in big_string:
    if i not in res:
        res.add((i, big_string.count(i)))

counter = 10
for i in sorted(res, key=lambda x: x[1], reverse=True):
    if counter != 0:
        print(i)
        counter -= 1
