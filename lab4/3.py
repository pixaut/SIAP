import time

class TrafficLight:

    color:str

    def running(self):

        order = {'red':7,'yellow':2,'green':3}

        while True:
            for i in order.items():
                self.color = i[0]
                print(self.color)

                for t in range(i[1], -1 ,-1):
                    print(f'Осталось: {t} секунд')
                    time.sleep(1)


if __name__ == '__main__':

    tf = TrafficLight()

    tf.running()