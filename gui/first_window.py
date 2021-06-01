# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_JamboGui(object):
    def setupUi(self, JamboGui):
        if not JamboGui.objectName():
            JamboGui.setObjectName(u"JamboGui")
        JamboGui.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(JamboGui.sizePolicy().hasHeightForWidth())
        JamboGui.setSizePolicy(sizePolicy)
        JamboGui.setMinimumSize(QSize(800, 600))
        JamboGui.setMaximumSize(QSize(800, 600))
        self.myGrid2 = QGridLayout(JamboGui)
        self.myGrid2.setObjectName(u"myGrid2")
        self.myGrid2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(JamboGui)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(800, 600))
        self.frame.setMaximumSize(QSize(800, 600))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(63, 217, 93, 255), stop:1 rgba(137, 230, 65, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.projectLoader = QLabel(self.frame)
        self.projectLoader.setObjectName(u"projectLoader")
        self.projectLoader.setMinimumSize(QSize(50, 50))
        self.projectLoader.setMaximumSize(QSize(50, 50))
        self.projectLoader.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.projectLoader.setFrameShadow(QFrame.Plain)
        self.projectLoader.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.projectLoader, 3, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.selectTotalSites = QSpinBox(self.frame)
        self.selectTotalSites.setObjectName(u"selectTotalSites")
        self.selectTotalSites.setMaximumSize(QSize(50, 16777215))
        self.selectTotalSites.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"font: 12pt \"Courier\";\n"
"color: rgb(255, 255, 255);")
        self.selectTotalSites.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.selectTotalSites.setMinimum(1)
        self.selectTotalSites.setMaximum(10)

        self.horizontalLayout.addWidget(self.selectTotalSites)

        self.inputSearch = QLineEdit(self.frame)
        self.inputSearch.setObjectName(u"inputSearch")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputSearch.sizePolicy().hasHeightForWidth())
        self.inputSearch.setSizePolicy(sizePolicy1)
        self.inputSearch.setMinimumSize(QSize(500, 40))
        self.inputSearch.setMaximumSize(QSize(300, 40))
        self.inputSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";\n"
"border-radius: 12px;\n"
"padding: 12px;")

        self.horizontalLayout.addWidget(self.inputSearch)

        self.searchInputButton = QPushButton(self.frame)
        self.searchInputButton.setObjectName(u"searchInputButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.searchInputButton.sizePolicy().hasHeightForWidth())
        self.searchInputButton.setSizePolicy(sizePolicy2)
        self.searchInputButton.setMinimumSize(QSize(150, 40))
        self.searchInputButton.setMaximumSize(QSize(50, 40))
        self.searchInputButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"font: 12pt \"Courier\";\n"
"color: rgb(255, 255, 255);")
        self.searchInputButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.searchInputButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.openMiniBrowser = QPushButton(self.frame)
        self.openMiniBrowser.setObjectName(u"openMiniBrowser")
        self.openMiniBrowser.setMinimumSize(QSize(150, 40))
        self.openMiniBrowser.setMaximumSize(QSize(60, 40))
        self.openMiniBrowser.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Courier\";")
        self.openMiniBrowser.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.openMiniBrowser)

        self.horizontalSpacer_3 = QSpacerItem(15, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tabJamboWidget = QTabWidget(self.frame)
        self.tabJamboWidget.setObjectName(u"tabJamboWidget")
        self.tabJamboWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border: 1px solid #000000;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"	\n"
"	color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	font: 10pt \"Courier\";\n"
"	min-width: 100px;\n"
"	min-height: 30px;\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"    color: rgb(255, 255, 255);\n"
"	background: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"")
        self.tabJamboWidget.setTabPosition(QTabWidget.North)
        self.tabJamboWidget.setTabShape(QTabWidget.Rounded)
        self.tabJamboWidget.setElideMode(Qt.ElideNone)
        self.tabJamboWidget.setDocumentMode(False)
        self.tabJamboWidget.setMovable(False)
        self.tabJamboWidget.setTabBarAutoHide(False)
        self.tabSearch = QWidget()
        self.tabSearch.setObjectName(u"tabSearch")
        self.tabSearch.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(63, 217, 93, 255), stop:1 rgba(137, 230, 65, 255));")
        self.formLayout = QFormLayout(self.tabSearch)
        self.formLayout.setObjectName(u"formLayout")
        self.cleanListButton = QPushButton(self.tabSearch)
        self.cleanListButton.setObjectName(u"cleanListButton")
        self.cleanListButton.setMinimumSize(QSize(50, 40))
        self.cleanListButton.setMaximumSize(QSize(50, 40))
        self.cleanListButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Courier\";")
        self.cleanListButton.setIconSize(QSize(30, 30))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cleanListButton)

        self.saveListButton = QPushButton(self.tabSearch)
        self.saveListButton.setObjectName(u"saveListButton")
        self.saveListButton.setMinimumSize(QSize(50, 40))
        self.saveListButton.setMaximumSize(QSize(50, 40))
        self.saveListButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Courier\";")
        self.saveListButton.setIconSize(QSize(40, 40))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.saveListButton)

        self.listResult = QListWidget(self.tabSearch)
        self.listResult.setObjectName(u"listResult")
        self.listResult.setMinimumSize(QSize(450, 0))
        self.listResult.setStyleSheet(u"font: 10pt \"Courier\";\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.listResult.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listResult.setAlternatingRowColors(True)
        self.listResult.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.listResult)

        self.tabJamboWidget.addTab(self.tabSearch, "")
        self.tabSites = QWidget()
        self.tabSites.setObjectName(u"tabSites")
        self.tabSites.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(63, 217, 93, 255), stop:1 rgba(137, 230, 65, 255));")
        self.verticalLayout_3 = QVBoxLayout(self.tabSites)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listSitesArticles = QListWidget(self.tabSites)
        self.listSitesArticles.setObjectName(u"listSitesArticles")
        self.listSitesArticles.setStyleSheet(u"font: 10pt \"Courier\";\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"QScrollArea::vertical{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.listSitesArticles.setFrameShape(QFrame.StyledPanel)
        self.listSitesArticles.setFrameShadow(QFrame.Sunken)
        self.listSitesArticles.setLineWidth(1)
        self.listSitesArticles.setMidLineWidth(0)
        self.listSitesArticles.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listSitesArticles.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listSitesArticles.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listSitesArticles.setAutoScroll(True)
        self.listSitesArticles.setTabKeyNavigation(False)
        self.listSitesArticles.setProperty("showDropIndicator", True)
        self.listSitesArticles.setAlternatingRowColors(True)
        self.listSitesArticles.setTextElideMode(Qt.ElideRight)
        self.listSitesArticles.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.listSitesArticles.setMovement(QListView.Static)

        self.verticalLayout_3.addWidget(self.listSitesArticles)

        self.tabJamboWidget.addTab(self.tabSites, "")

        self.verticalLayout.addWidget(self.tabJamboWidget)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 6)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 3, 3, 1, 1)


        self.myGrid2.addWidget(self.frame, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(JamboGui)

        self.tabJamboWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(JamboGui)
    # setupUi

    def retranslateUi(self, JamboGui):
        JamboGui.setWindowTitle(QCoreApplication.translate("JamboGui", u"JamboGui", None))
        self.projectLoader.setText("")
        self.searchInputButton.setText(QCoreApplication.translate("JamboGui", u"Pesquisar", None))
        self.openMiniBrowser.setText(QCoreApplication.translate("JamboGui", u"Browser", None))
        self.cleanListButton.setText(QCoreApplication.translate("JamboGui", u"L", None))
        self.saveListButton.setText(QCoreApplication.translate("JamboGui", u"S", None))
        self.tabJamboWidget.setTabText(self.tabJamboWidget.indexOf(self.tabSearch), QCoreApplication.translate("JamboGui", u"Pesquisas", None))
        self.tabJamboWidget.setTabText(self.tabJamboWidget.indexOf(self.tabSites), QCoreApplication.translate("JamboGui", u"Sites", None))
    # retranslateUi

