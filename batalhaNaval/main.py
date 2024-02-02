from PyQt5 import QtWidgets, uic, QtCore
import random
import sys

class telas:
    def __init__(self):

        self.app = QtWidgets.QApplication([])

        self.telaInicial = uic.loadUi("telaInicial.ui")
        self.tabuleiro = uic.loadUi("tabuleiro.ui")
        self.telaGameOver = uic.loadUi("telaGameOver.ui")
        self.telaWinner = uic.loadUi("telaWinner.ui")
        self.telaInicial.show()
        self.telaInicial.play.clicked.connect(self.mudar_telaInicial)
        self.telaGameOver.btnExit.clicked.connect(self.Exit)
        self.telaGameOver.btnAgain.clicked.connect(self.Again)
        # self.vidas = 20
        self.tentativas_max = 20
        self.tentativas = 0

        coordenadasLetras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        coordenadasNumeros = ["1","2","3","4","5","6","7","8","9","10"]
        sorteio = []

        sorteio1 = random.sample(coordenadasLetras, 4)

        while True:
            sorteio2 = random.sample(coordenadasNumeros, 4)
            if int(sorteio2[1]) > 8:
                continue
            if int(sorteio2[2]) > 7:
                continue
            if int(sorteio2[3]) > 6:
                continue
            else:
                break


        for i in range(len(sorteio1)):
            sorteio.append(f"{sorteio1[i]}{sorteio2[i]}")

        print(sorteio)


        self.barcos = []

        # laço para separar os caracteres letras de numeros de cada coordenada
        for a in range(len(sorteio)):
            if a == 0:
                for i in range(len(sorteio)):
                    self.barcos.append(sorteio[i])

            if a == 1:
                print("\nCOMEÇA O 2")
                separado = list(sorteio[a])
                print(separado)
                self.barcos.append(f"{separado[0]}{int(separado[1])+1}")
                print(self.barcos)
                
            
            if a == 2:
                for i in range(2):
                    print("\nCOMEÇA O 3")
                    separado = list(sorteio[a])
                    print(separado)
                    self.barcos.append(f"{separado[0]}{int(separado[1])+(i + 1)}")
                    print(self.barcos)

            if a == 3:
                    for i in range(3):
                        print("\nCOMEÇA O 4")
                        separado = list(sorteio[a])
                        print(separado)
                        self.barcos.append(f"{separado[0]}{int(separado[1])+(i+1)}")
                        print(self.barcos)

        # comando para executar sempre que o botões da tela forem clicados
        for button in self.tabuleiro.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.selecionarBotao)
            
        self.app.exec() # executar o pyqt
        sys.exit(self.app.exec_()) # acessa o sistema operacional e 'mata' o loop do pyqt

    def restart(self):
        QtCore.QCoreApplication.quit() #permite sair da aplicação
        QtCore.QProcess.startDetached(sys.executable, sys.argv) # permite que o programa incie novamente antes de sair por completo da aplicação

    def mudar_telaInicial(self):
        self.telaInicial.close()
        self.tabuleiro.show()

    def Exit (self):
        self.telaGameOver.close()   

    def Again (self):
        self.restart()
    
    def selecionarBotao(self):
        sender = self.telaInicial.sender()
        senderCoordenada = sender.objectName()
    
        # if senderCoordenada in self.barcos:
        #     sender.setStyleSheet("background-image: url('img/bomba_estourou.png'); border: none")
        #     self.barcos.remove(senderCoordenada)
        #     self.vidas += 1

        #     if len(self.barcos) == 0:
        #         self.tabuleiro.close()
        #         self.telaWinner.show()

        # else:
        #     sender.setStyleSheet("background-image: url('img/bomba.png'); border: none")
        #     self.vidas -= 1

        #     if self.vidas == 0:
        #         self.tabuleiro.close()
        #         self.telaGameOver.show()

        if self.tentativas < self.tentativas_max:
           
            if senderCoordenada in self.barcos:
                sender.setStyleSheet("background-image: url('img/bomba_estourou.png'); border: none")
                self.barcos.remove(senderCoordenada)
                sender.setEnabled(False)
               
                if len(self.barcos) == 0:
                    self.tabuleiro.close()
                    self.telaWinner.show()
                   
                   
            else:
                sender.setStyleSheet("background-image: url('img/bomba.png'); border: none")
                self.tentativas += 1
                print(self.tentativas)
 
        else:
            self.tabuleiro.close()
            self.telaGameOver.show()
            sender.setEnabled(False)

if __name__ == '__main__':
    c = telas()