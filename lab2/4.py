
def fun():
    #raise Exception('er')
    print('wow')



if __name__ == '__main__':

    try:
        fun()
    except Exception as e:
        print(e)
    finally:
        print("Выполнится в любом случае")
    
