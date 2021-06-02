import os.path
from PySide2.QtCore import Signal, QThread, QSize, SIGNAL, QObject, Qt, QTimer, QCoreApplication
from PySide2.QtGui import QMovie, QPixmap
import sys
from core import site_tips
from first_window import Ui_JamboGui
from helpers.helper_buttons import helper_clean_list_button, \
    helper_search_input_button, helper_save_list_button, helper_open_browser_button
from aux_classes import internet_search
from gui import miniBrowser
import jambo_pdf
from helpers.helper_message_box import *


class Window(QWidget):
    pass


class Worker(QThread):
    progress = Signal(str)

    def __init__(self, parent=None, input_query='', tot_query=0):
        super(Worker, self).__init__()
        self.input_query = input_query
        self.tot_query = tot_query

    def run(self):
        internet_test = internet_search.InternetSearch(self.input_query, self.tot_query)
        if not internet_test.get_pages_wikipedia():
            helper_request_search()
        else:
            internet_test.get_pages_wikipedia()
            self.progress.emit(str)


class JamboGui(QWidget, Ui_JamboGui):
    def __init__(self):
        super(JamboGui, self).__init__()
        self.setupUi(self)
        self.cleanListButton.setStyleSheet(helper_clean_list_button())
        self.searchInputButton.setStyleSheet(helper_search_input_button())
        self.saveListButton.setStyleSheet(helper_save_list_button())
        self.openMiniBrowser.setStyleSheet(helper_open_browser_button())
        self.mini_browser = miniBrowser.MiniBrowser()
        image = os.path.join(os.getcwd(), 'loader_new.gif')
        self.movie = QMovie(image)
        self.movie.setScaledSize(QSize(50, 50))
        self.thread = None
        self.internet_search = internet_search.InternetSearch()
        self.setWindowTitle('Jambo')
        self.setWindowIcon(QIcon(os.path.join(os.getcwd(), 'pesquisa.png')))
        self.add_items()
        QObject.connect(self.listSitesArticles, SIGNAL("itemClicked(QListWidgetItem *)"), self.item_click)
        self.cleanListButton.setText('')
        self.cleanListButton.setIcon(QIcon(os.path.join(os.getcwd(), 'clean_icon.png')))
        self.saveListButton.setText('')
        self.saveListButton.setIcon(QIcon(os.path.join(os.getcwd(), 'save_icon.png')))

    def add_items(self):
        self.listSitesArticles.setWordWrap(True)
        self.listSitesArticles.setSpacing(4)
        for key, value in site_tips.articles.items():
            item = QListWidgetItem(key)
            self.listSitesArticles.addItem(item)

    def item_click(self, item):
        self.show_browser()
        for key, value in site_tips.articles.items():
            if item.text() == key:
                self.mini_browser.lineEdit.setText(value)

    def show_browser(self):
        self.mini_browser.show()

    def load_gif(self):
        if self.thread is not None:
            return
        if self.inputSearch.text() == '':
            helper_msg_load()
        elif len(self.inputSearch.text()) <= 1:
            helper_msg_load2()
        else:
            self.projectLoader.setMovie(self.movie)
            self.movie.start()
            self.thread = Worker(None, self.inputSearch.text(), self.selectTotalSites.value())
            self.thread.progress.connect(self.seed_list_widget)
            try:
                self.thread.start()
            except:
                QCoreApplication.quit()

    def seed_list_widget(self):
        self.listResult.clear()
        self.listResult.setSpacing(5)
        self.listResult.setWordWrap(True)
        if len(self.internet_search.site_tips) > 0:
            self.listResult.addItem(c_interesting_links)
            self.listResult.addItems(self.internet_search.site_tips)
        if len(self.internet_search.site_caught) > 0:
            self.listResult.addItem(c_content_base)
            self.listResult.addItems(self.internet_search.site_caught)
            for items in self.internet_search.read_pages():
                self.listResult.addItem(items)
        self.movie.stop()
        self.projectLoader.clear()
        self.thread.progress.disconnect()
        self.thread = None
        self.internet_search.site_caught.clear()
        self.internet_search.site_tips.clear()

    def clear_all(self):
        if self.listResult.count() > 0:
            if helper_clear_all_1():
                self.listResult.clear()
                self.inputSearch.clear()
        else:
            helper_clear_all_2()

    def save_list_widget(self):
        if self.listResult.count() > 0:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '',
                                                       '*.pdf', options=options)
            if file_name:
                jb = jambo_pdf.JamboPDF('data.txt', file_name)
                jb.build_pdf()
            else:
                jb = jambo_pdf.JamboPDF('data.txt', file_name + '_jambo')
                jb.build_pdf()
        else:
            helper_save_list_pdf()

    def show_list_sites(self):
        self.article_sites.show()

    def start_operations(self):
        self.saveListButton.clicked.connect(self.save_list_widget)
        self.searchInputButton.clicked.connect(self.load_gif)
        self.openMiniBrowser.clicked.connect(self.show_browser)
        self.cleanListButton.clicked.connect(self.clear_all)


if __name__ == "__main__":
    app = QApplication([])
    ui = JamboGui()
    ui.start_operations()
    # pixmap = QPixmap(os.path.join(os.getcwd(), 'SplashScreen_Jambo.png'))
    # splash = QSplashScreen()
    # splash.setPixmap(pixmap)
    # QTimer.singleShot(4999, splash.close)
    # QTimer.singleShot(5000, ui.show)
    # splash.show()
    ui.show()
    sys.exit(app.exec_())
