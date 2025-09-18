dictionary = dict()

with open("lab3/text_documents/F4.txt",encoding='utf-8') as file:


    for line in file:

        subject,_,lessons = line.partition(':')

        lessons = lessons.strip()

        total = 0

        for part in lessons.split():
            # Берем только число до скобки
            num = ''.join(ch for ch in part if ch.isdigit())
            if num:
                total += int(num)

        dictionary[subject] = total

for item in dictionary.items():
    print(item)