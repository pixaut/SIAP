
def isDigitPrime(digit:int) -> bool:
    n = 2
    while n*n <= digit:
        if (digit%n == 0):
            return False
        n += 1
    return True

def sortDict(dictionary):
    items = dict( sorted(dictionary.items(),reverse=True) )
    dictionary.clear()
    dictionary.update(items)
    #Если не поменяется добавить ретурн

def number_of_words(line:str) -> int:
    return len(line.split())

def getLongestWord(line:str)->str:
    words = line.split()
    return max(words, key=len)

def getGeaometricAverage(numbers:list)->float:
    p = 1
    [p := p * number for number in numbers]
    return p ** (1/len(numbers))
 
def some_function(object):

    print(object,' : ',end='')

    match object:
        case int():
            print("число простое" if isDigitPrime(object) else "число составное") 
        case dict():
            sortDict(object)
            print(f"Просортированный словарь: {object}")
        case str():
            n = number_of_words(object)
            word = getLongestWord(object)
            print(f"Количество слов: {n}, Самое длинное слово: {word}")
        case list():
            n = getGeaometricAverage(object)
            print(f"Среднее геометрическое списка: {n}")
        case _:
            print(f"Функция не расчитана на тип: {type(object)}")

if __name__ == '__main__':

    #Уберите комментарий с нужного типа
    some_var = {1:'ods',-1:'asd',10:'oo'}
    #some_var = 10
    #some_var = 'asdad ieieiedd'
    #some_var = {1,2,3,4}
    #some_var = [1,2,3,4]
    some_function(some_var) 