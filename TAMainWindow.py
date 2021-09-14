# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TAMainWindow_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 649)
        MainWindow.setStyleSheet("*{\n"
" border: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slide_menu_container = QtWidgets.QFrame(self.centralwidget)
        self.slide_menu_container.setEnabled(True)
        self.slide_menu_container.setMaximumSize(QtCore.QSize(0, 16777215))
        self.slide_menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu_container.setObjectName("slide_menu_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.slide_menu_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.slide_menu = QtWidgets.QFrame(self.slide_menu_container)
        self.slide_menu.setMinimumSize(QtCore.QSize(198, 0))
        self.slide_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu.setObjectName("slide_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.slide_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.slide_menu)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Title_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Title_label.setFont(font)
        self.Title_label.setObjectName("Title_label")
        self.horizontalLayout_5.addWidget(self.Title_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.frame_4, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_5 = QtWidgets.QFrame(self.slide_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.toolBox = QtWidgets.QToolBox(self.frame_5)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 162, 493))
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.page)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.New_button = QtWidgets.QPushButton(self.frame_6)
        self.New_button.setObjectName("New_button")
        self.verticalLayout_6.addWidget(self.New_button)
        self.Load_button = QtWidgets.QPushButton(self.frame_6)
        self.Load_button.setObjectName("Load_button")
        self.verticalLayout_6.addWidget(self.Load_button)
        self.SaveAs_button = QtWidgets.QPushButton(self.frame_6)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/save-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveAs_button.setIcon(icon)
        self.SaveAs_button.setObjectName("SaveAs_button")
        self.verticalLayout_6.addWidget(self.SaveAs_button)
        self.verticalLayout_5.addWidget(self.frame_6, 0, QtCore.Qt.AlignTop)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/document-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 162, 493))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.page_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Edit_button = QtWidgets.QPushButton(self.frame_7)
        self.Edit_button.setObjectName("Edit_button")
        self.verticalLayout_8.addWidget(self.Edit_button)
        self.Rotate_button = QtWidgets.QPushButton(self.frame_7)
        self.Rotate_button.setObjectName("Rotate_button")
        self.verticalLayout_8.addWidget(self.Rotate_button)
        self.Combin_button = QtWidgets.QPushButton(self.frame_7)
        self.Combin_button.setObjectName("Combin_button")
        self.verticalLayout_8.addWidget(self.Combin_button)
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 164, 493))
        self.page_3.setObjectName("page_3")
        self.toolBox.addItem(self.page_3, "")
        self.verticalLayout_4.addWidget(self.toolBox)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.slide_menu)
        self.horizontalLayout.addWidget(self.slide_menu_container)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.main_body)
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.header)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Menu_button = QtWidgets.QPushButton(self.frame_2)
        self.Menu_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-align-justified.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Menu_button.setIcon(icon2)
        self.Menu_button.setIconSize(QtCore.QSize(32, 32))
        self.Menu_button.setObjectName("Menu_button")
        self.horizontalLayout_4.addWidget(self.Menu_button)
        self.horizontalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.First_button = QtWidgets.QPushButton(self.frame)
        self.First_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-player-skip-back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.First_button.setIcon(icon3)
        self.First_button.setObjectName("First_button")
        self.horizontalLayout_6.addWidget(self.First_button)
        self.Prev_button = QtWidgets.QPushButton(self.frame)
        self.Prev_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-player-track-prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Prev_button.setIcon(icon4)
        self.Prev_button.setObjectName("Prev_button")
        self.horizontalLayout_6.addWidget(self.Prev_button)
        self.Play_button = QtWidgets.QPushButton(self.frame)
        self.Play_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-player-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play_button.setIcon(icon5)
        self.Play_button.setObjectName("Play_button")
        self.horizontalLayout_6.addWidget(self.Play_button)
        self.Next_button = QtWidgets.QPushButton(self.frame)
        self.Next_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-player-track-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next_button.setIcon(icon6)
        self.Next_button.setObjectName("Next_button")
        self.horizontalLayout_6.addWidget(self.Next_button)
        self.Last_button = QtWidgets.QPushButton(self.frame)
        self.Last_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-player-skip-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Last_button.setIcon(icon7)
        self.Last_button.setObjectName("Last_button")
        self.horizontalLayout_6.addWidget(self.Last_button)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minimize_button = QtWidgets.QPushButton(self.frame_3)
        self.minimize_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/Programming-Minimize-Window-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_button.setIcon(icon8)
        self.minimize_button.setIconSize(QtCore.QSize(16, 16))
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_3.addWidget(self.minimize_button)
        self.maximize_button = QtWidgets.QPushButton(self.frame_3)
        self.maximize_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/Programming-Maximize-Window-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximize_button.setIcon(icon9)
        self.maximize_button.setIconSize(QtCore.QSize(16, 16))
        self.maximize_button.setObjectName("maximize_button")
        self.horizontalLayout_3.addWidget(self.maximize_button)
        self.close_button = QtWidgets.QPushButton(self.frame_3)
        self.close_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/Actions-file-close-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon10)
        self.close_button.setIconSize(QtCore.QSize(24, 24))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_3.addWidget(self.close_button)
        self.horizontalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.main_body_contents = QtWidgets.QFrame(self.main_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_contents.setObjectName("main_body_contents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.main_body_contents)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.main_body_contents)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.verticalLayout.addWidget(self.main_body_contents)
        self.horizontalLayout.addWidget(self.main_body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title_label.setText(_translate("MainWindow", "TA Simulator"))
        self.New_button.setText(_translate("MainWindow", "New"))
        self.Load_button.setText(_translate("MainWindow", "Load"))
        self.SaveAs_button.setText(_translate("MainWindow", "Save As ..."))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "File"))
        self.Edit_button.setText(_translate("MainWindow", "Edit"))
        self.Rotate_button.setText(_translate("MainWindow", "Rotate"))
        self.Combin_button.setText(_translate("MainWindow", "Combine"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Tools"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Papers"))
