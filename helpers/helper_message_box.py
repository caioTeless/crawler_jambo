import os
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
from core.const_widgets import *


path = os.path.join(os.getcwd(), 'pesquisa.png')


def helper_msg_load():
    msg = QMessageBox()
    msg.setWindowTitle(c_title_msg_loader)
    msg.setText(c_content_msg_loader)
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setWindowIcon(QIcon(path))
    msg.exec_()


def helper_msg_load2():
    msg = QMessageBox()
    msg.setWindowTitle(c_title_msg_loader)
    msg.setText(c_content_msg_null)
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setWindowIcon(QIcon(path))
    msg.exec_()


def helper_clear_all_1():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(c_title_msg_clear)
    msg.setText(c_content_msg_clear)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setWindowIcon(QIcon(path))
    result_dialog = msg.exec_()
    if result_dialog == msg.Ok:
        return True


def helper_clear_all_2():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(c_title_msg_clear)
    msg.setText(c_content_msg_clear2)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setWindowIcon(QIcon(path))
    msg.exec_()


def helper_save_list_pdf():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(c_title_msg_save_pdf)
    msg.setText(c_content_msg_save_pdf)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setWindowIcon(QIcon(path))
    msg.exec_()


def helper_search_browser():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(c_title_msg_search_browser)
    msg.setText(c_content_msg_search_browser)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setWindowIcon(QIcon(path))
    msg.exec_()


def helper_search_browser2():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(c_title_msg_search_browser)
    msg.setText(c_content_msg_search_browser2)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setWindowIcon(QIcon(path))
    msg.exec_()


def helper_request_search():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(c_title_msg_request_search)
    msg.setText(c_content_msg_request_search)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setWindowIcon(QIcon(path))
    msg.exec_()


