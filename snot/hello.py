import os
import sys



class HELLO:

    name = 'me'

    @classmethod
    def run(cls):
        print(cls.name)



if __name__ == '__main__':
    HELLO.run()
