import os


class Triangulo():

    def _init_(self):
        self.v1 = 0.0
        self.v2 = 0.0
        self.v3 = 0.0

    def iniciar(self):
        self.v1 = 0.0
        self.v2 = 0.0
        self.v3 = 0.0
        os.system('cls')

    def obternums(self):
        print('Digite tres valores para formar ou não um triangulo!')
        print('digite os valores em ordem decrescente (do maior para o menor)')
        self.v1 = float(input('digite o primeiro valor'))
        self.v1 = float(input('digite o segundo valor'))
        self.v1 = float(input('digite o terceiro valor'))

    def tipotri(self):
        if self.v1 == self.v2 != self.v3
            print('é um triangulo isosceles')
                else:
            self.v1 == self.v2 == self.v3
            print('é um triangulo equillátero')
            
                    else:
                        self.v1 != self.v2 != self.v3
                        print('é um triangulo escaleno!')

                            else:
                                self.v1 = (self.v2 ** 2 ) + (self.v2 ** 2)
                                print('é um triangulo retângulo')

    def naotri(self):
        x = True
            if self.v1 > (self.v2 - self.v3) and self.v1 < (self.v2 + self.v3)
            x = False
            return obternums()

    def fim(self):
        print('agradeço!!!')

