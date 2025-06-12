# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import resources.icons.images

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1548, 962)
        icon = QIcon()
        icon.addFile(u":/viniq/viniq.webp", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 8, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setMinimumSize(QSize(200, 100))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.pushButton_quality = QPushButton(self.page)
        self.pushButton_quality.setObjectName(u"pushButton_quality")
        sizePolicy1.setHeightForWidth(self.pushButton_quality.sizePolicy().hasHeightForWidth())
        self.pushButton_quality.setSizePolicy(sizePolicy1)
        self.pushButton_quality.setMinimumSize(QSize(200, 100))
        self.pushButton_quality.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_quality, 7, 0, 1, 1)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(200, 100))
        self.pushButton.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton, 3, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setMinimumSize(QSize(200, 100))
        self.pushButton_5.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_5, 9, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(200, 100))
        self.pushButton_2.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_2, 5, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 10, 0, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(100, 100))
        self.label_2.setMaximumSize(QSize(300, 300))
        self.label_2.setPixmap(QPixmap(u":/portada/logo.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 97, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 0, 0, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(1200, 0))
        font1 = QFont()
        font1.setFamilies([u"Algerian"])
        font1.setPointSize(150)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 1, 11, 1)

        self.verticalSpacer_7 = QSpacerItem(97, 766, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 1, 2, 10, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_16 = QLabel(self.page_2)
        self.label_16.setObjectName(u"label_16")
        font2 = QFont()
        font2.setFamilies([u"Cascadia Code"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_16.setFont(font2)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.fixed_acidity = QLineEdit(self.page_2)
        self.fixed_acidity.setObjectName(u"fixed_acidity")
        self.fixed_acidity.setMinimumSize(QSize(0, 30))
        self.fixed_acidity.setMaximumSize(QSize(150, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Cascadia Code"])
        font3.setPointSize(20)
        self.fixed_acidity.setFont(font3)
        self.fixed_acidity.setStyleSheet(u"")
        self.fixed_acidity.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.fixed_acidity)

        self.label_17 = QLabel(self.page_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_17)

        self.volatile_acidity = QLineEdit(self.page_2)
        self.volatile_acidity.setObjectName(u"volatile_acidity")
        self.volatile_acidity.setMinimumSize(QSize(0, 30))
        self.volatile_acidity.setMaximumSize(QSize(150, 16777215))
        self.volatile_acidity.setFont(font3)
        self.volatile_acidity.setStyleSheet(u"")
        self.volatile_acidity.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.volatile_acidity)

        self.label_18 = QLabel(self.page_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_18)

        self.citric_acid = QLineEdit(self.page_2)
        self.citric_acid.setObjectName(u"citric_acid")
        self.citric_acid.setMinimumSize(QSize(0, 30))
        self.citric_acid.setMaximumSize(QSize(150, 16777215))
        self.citric_acid.setFont(font3)
        self.citric_acid.setStyleSheet(u"")
        self.citric_acid.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.citric_acid)

        self.label_19 = QLabel(self.page_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_19)

        self.residual_sugar = QLineEdit(self.page_2)
        self.residual_sugar.setObjectName(u"residual_sugar")
        self.residual_sugar.setMinimumSize(QSize(0, 30))
        self.residual_sugar.setMaximumSize(QSize(150, 16777215))
        self.residual_sugar.setFont(font3)
        self.residual_sugar.setStyleSheet(u"")
        self.residual_sugar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.residual_sugar)

        self.label_20 = QLabel(self.page_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_20)

        self.chlorides = QLineEdit(self.page_2)
        self.chlorides.setObjectName(u"chlorides")
        self.chlorides.setMinimumSize(QSize(0, 30))
        self.chlorides.setMaximumSize(QSize(150, 16777215))
        self.chlorides.setFont(font3)
        self.chlorides.setStyleSheet(u"")
        self.chlorides.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.chlorides)

        self.label_21 = QLabel(self.page_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.label_21)

        self.free_sulfur_dioxide = QLineEdit(self.page_2)
        self.free_sulfur_dioxide.setObjectName(u"free_sulfur_dioxide")
        self.free_sulfur_dioxide.setMinimumSize(QSize(0, 30))
        self.free_sulfur_dioxide.setMaximumSize(QSize(150, 16777215))
        self.free_sulfur_dioxide.setFont(font3)
        self.free_sulfur_dioxide.setStyleSheet(u"")
        self.free_sulfur_dioxide.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.free_sulfur_dioxide)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_3.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer_24)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_3.setItem(3, QFormLayout.SpanningRole, self.verticalSpacer_25)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_3.setItem(5, QFormLayout.SpanningRole, self.verticalSpacer_26)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_3.setItem(7, QFormLayout.SpanningRole, self.verticalSpacer_27)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_3.setItem(9, QFormLayout.SpanningRole, self.verticalSpacer_28)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_3.setItem(11, QFormLayout.SpanningRole, self.verticalSpacer_29)


        self.gridLayout_3.addLayout(self.formLayout_3, 1, 2, 1, 1)

        self.label_28 = QLabel(self.page_2)
        self.label_28.setObjectName(u"label_28")
        sizePolicy2.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy2)
        self.label_28.setMinimumSize(QSize(100, 100))
        self.label_28.setMaximumSize(QSize(300, 300))
        self.label_28.setPixmap(QPixmap(u":/viniq/viniq.webp"))
        self.label_28.setScaledContents(True)
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_28, 0, 6, 1, 1)

        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamilies([u"Colonna MT"])
        font4.setPointSize(72)
        font4.setBold(False)
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 5, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.total_sulfur_dioxide = QLineEdit(self.page_2)
        self.total_sulfur_dioxide.setObjectName(u"total_sulfur_dioxide")
        self.total_sulfur_dioxide.setMinimumSize(QSize(0, 30))
        self.total_sulfur_dioxide.setMaximumSize(QSize(150, 16777215))
        self.total_sulfur_dioxide.setFont(font3)
        self.total_sulfur_dioxide.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.total_sulfur_dioxide)

        self.label_23 = QLabel(self.page_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_23)

        self.density = QLineEdit(self.page_2)
        self.density.setObjectName(u"density")
        self.density.setMinimumSize(QSize(0, 30))
        self.density.setMaximumSize(QSize(150, 16777215))
        self.density.setFont(font3)
        self.density.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.density)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_4.setItem(4, QFormLayout.SpanningRole, self.verticalSpacer_31)

        self.label_24 = QLabel(self.page_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_24)

        self.ph = QLineEdit(self.page_2)
        self.ph.setObjectName(u"ph")
        self.ph.setMinimumSize(QSize(0, 30))
        self.ph.setMaximumSize(QSize(150, 16777215))
        self.ph.setFont(font3)
        self.ph.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.ph)

        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_4.setItem(6, QFormLayout.SpanningRole, self.verticalSpacer_32)

        self.label_25 = QLabel(self.page_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.label_25)

        self.sulphates = QLineEdit(self.page_2)
        self.sulphates.setObjectName(u"sulphates")
        self.sulphates.setMinimumSize(QSize(0, 30))
        self.sulphates.setMaximumSize(QSize(150, 16777215))
        self.sulphates.setFont(font3)
        self.sulphates.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.sulphates)

        self.verticalSpacer_33 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_4.setItem(8, QFormLayout.SpanningRole, self.verticalSpacer_33)

        self.label_26 = QLabel(self.page_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.formLayout_4.setWidget(9, QFormLayout.LabelRole, self.label_26)

        self.alcohol = QLineEdit(self.page_2)
        self.alcohol.setObjectName(u"alcohol")
        self.alcohol.setMinimumSize(QSize(0, 30))
        self.alcohol.setMaximumSize(QSize(150, 16777215))
        self.alcohol.setFont(font3)
        self.alcohol.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_4.setWidget(9, QFormLayout.FieldRole, self.alcohol)

        self.verticalSpacer_34 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_4.setItem(10, QFormLayout.SpanningRole, self.verticalSpacer_34)

        self.calculate_quality = QPushButton(self.page_2)
        self.calculate_quality.setObjectName(u"calculate_quality")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.calculate_quality.sizePolicy().hasHeightForWidth())
        self.calculate_quality.setSizePolicy(sizePolicy4)
        self.calculate_quality.setFont(font2)

        self.formLayout_4.setWidget(11, QFormLayout.SpanningRole, self.calculate_quality)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_4.setItem(12, QFormLayout.SpanningRole, self.verticalSpacer_35)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_4.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer_30)

        self.label_22 = QLabel(self.page_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_22)


        self.gridLayout_3.addLayout(self.formLayout_4, 1, 4, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_27 = QLabel(self.page_2)
        self.label_27.setObjectName(u"label_27")
        font5 = QFont()
        font5.setFamilies([u"Arial Black"])
        font5.setPointSize(28)
        font5.setBold(True)
        self.label_27.setFont(font5)
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_27)

        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_36)

        self.quality = QLineEdit(self.page_2)
        self.quality.setObjectName(u"quality")
        self.quality.setMinimumSize(QSize(0, 30))
        self.quality.setMaximumSize(QSize(150, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Cascadia Code"])
        font6.setPointSize(28)
        font6.setBold(True)
        self.quality.setFont(font6)
        self.quality.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.quality.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.quality, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_37 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_37)

        self.save = QPushButton(self.page_2)
        self.save.setObjectName(u"save")
        self.save.setFont(font2)

        self.verticalLayout_2.addWidget(self.save)

        self.verticalSpacer_38 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_38)

        self.clear = QPushButton(self.page_2)
        self.clear.setObjectName(u"clear")
        self.clear.setFont(font2)

        self.verticalLayout_2.addWidget(self.clear)

        self.verticalSpacer_39 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_39)

        self.back = QPushButton(self.page_2)
        self.back.setObjectName(u"back")
        self.back.setFont(font2)

        self.verticalLayout_2.addWidget(self.back)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.edit = QPushButton(self.page_2)
        self.edit.setObjectName(u"edit")
        self.edit.setFont(font2)

        self.verticalLayout_2.addWidget(self.edit)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 6, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1548, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VinIQ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.pushButton_quality.setText(QCoreApplication.translate("MainWindow", u"CLASIFICADOR\n"
"DE CALIDAD", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"VENTAS", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"EMPLEADOS", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"VI\u00d1ERIA\n"
"SAN JUAN", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Acidez Fija", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Acidez Vol\u00e1til", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u00c1cido C\u00edtrico", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Az\u00facar Residual", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Cloruros", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Di\u00f3x. de Azufre libre", None))
        self.label_28.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CALIDAD DEL VINO", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Densidad", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"PH", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Sulfatos", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Alcohol", None))
        self.calculate_quality.setText(QCoreApplication.translate("MainWindow", u"Calcular calidad", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Di\u00f3x. de Azufre Total", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Calidad", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.back.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.edit.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
    # retranslateUi

