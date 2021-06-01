import os.path
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from gui.main_window import Ui_MainWindow
from helpers import helper_buttons, helper_message_box
import sys


class MiniBrowser(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MiniBrowser, self).__init__()
        self.setupUi(self)
        self.pushButton.setText('Pesquisar')
        self.setWindowTitle('Jambo browser')
        self.setWindowIcon(QIcon(os.path.join(os.getcwd(), 'pesquisa.png')))
        self.setStyleSheet(helper_buttons.helper_background_mini_browser())
        self.lineEdit.setStyleSheet(helper_buttons.helper_input_mini_browser())
        self.pushButton.setStyleSheet(helper_buttons.helper_search_mini_browser())
        self.pushButton.setMinimumSize(QSize(150, 50))
        self.pushButton.setMaximumSize(QSize(50, 50))
        self.pushButton.clicked.connect(self.return_page)

    def return_page(self):
        if self.lineEdit.text() == '' or len(self.lineEdit.text()) <= 5:
            helper_message_box.helper_search_browser()
        elif '://' not in self.lineEdit.text():
            helper_message_box.helper_search_browser2()
        else:
            url = QUrl(self.lineEdit.text())
            self.webEngineView.setUrl(url)

    def load_finished(self):
        url = self.webEngineView.url().toString()
        self.lineEdit.setText(url)


if __name__ == '__main__':
    app = QApplication([])
    ui = MiniBrowser()
    ui.show()
    sys.exit(app.exec_())
