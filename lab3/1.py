
path_to_files = "lab3/text_documents"

with open(f"{path_to_files}/F1.txt","w+",encoding='utf-8') as f:
    while True:
        line = input('Введите строчку или Enter: ')
        if not line:
            break

        print(line,file=f)

with open(f"{path_to_files}/F1.txt","r",encoding='utf-8') as f:
    lines = f.readlines();

with open(f"{path_to_files}/F2.txt","w",encoding='utf-8') as f:
    f.writelines( [line for line in lines if len(set(line.split())) < len(line.split())]  )

print('Программа завершена')