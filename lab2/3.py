def getMatrix(n:int,m:int) -> list:
    
    list = [ ['&' if(i+j)%2 == 0 else '%' for j in range(m)] for i in range(n)]
    list[0][0] = '.'
    return list


if __name__ == '__main__':

    for row in getMatrix(5,6):
        print(' '.join(row))
