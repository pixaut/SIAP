text = input()


pairs_sum = sum( 1 for i in range(len(text)-1) 
           if (text[i].islower() and text[i+1].islower() ) or (text[i].isupper() and text[i+1].isupper())  
)

print(f'Пар чисел одинакового регистра: {pairs_sum}')


vowel_letters = ['а','у','е','о','ы','я','и','ю','ё','э']

number_of_vowels = sum(1 for letter in text if letter.lower() in vowel_letters)

print(f'Количество гласных: {number_of_vowels}')
