import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
            QPushButton, QWidget)

# Cria uma classe personalizada que herda de QMainWindow
class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Cria um widget central para a janela
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela bonita')

        # Cria botões personalizados usando um método
        self.botao1 = self.make_button('Texto do botão')
        self.botao1.clicked.connect(self.segunda_acao_marcada)  # type: ignore

        self.botao2 = self.make_button('Botão 2')

        self.botao3 = self.make_button('Terceiro')

        # Define um layout de grade para organizar os botões
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        # Adiciona os botões ao layout de grade
        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # Cria uma barra de status
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # Cria uma barra de menu
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')

        # Conecta o slot para exibir a mensagem na barra de status à ação do menu
        self.primeira_acao.triggered.connect(  # type:ignore
            self.muda_mensagem_da_status_bar)

        self.segunda_action = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_action.setCheckable(True)

        # Conecta o slot para lidar com a ação de alternância (marcar/desmarcar)
        self.segunda_action.toggled.connect(  # type:ignore
            self.segunda_acao_marcada)
        self.segunda_action.hovered.connect(  # type:ignore
            self.segunda_acao_marcada)

    @Slot()
    def muda_mensagem_da_status_bar(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado?', self.segunda_action.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 80px;')
        return btn

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()  # O loop da aplicação
