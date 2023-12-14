from PyQt5 import QtWidgets, uic

class telas:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.telaInicial = uic.loadUi("../telaInicial.ui")
        self.tabuleiro = uic.loadUi("../tabuleiro.ui")
        self.telaInicial.show()
        self.telaInicial.play.clicked.connect(self.mudar_tela)

        app.exec()

    def mudar_tela(self):
        self.telaInicial.close()
        self.tabuleiro.show()

if __name__ == '__main__':
    c = telas()