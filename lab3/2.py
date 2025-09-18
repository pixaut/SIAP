with open("lab3/text_documents/F3.txt", "r", encoding="utf-8") as f:
    average = 0
    count = 0
    for line in f:
        parts = line.split()
        text = parts[0]
        cost = int(parts[1])

        if 10 <= cost < 50:
            print(f'игрушка: {text}, стоимость: {cost}')

        average += cost
        count += 1

    if count > 0:
        average /= count
    else:
        average = 0

print(f'средняя цена: {average}')
