# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Show_Hide_TradeLog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TradeLog_ShowHide(object):
    def setupUi(self, TradeLog_ShowHide):
        TradeLog_ShowHide.setObjectName("TradeLog_ShowHide")
        TradeLog_ShowHide.setEnabled(True)
        TradeLog_ShowHide.resize(254, 769)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        TradeLog_ShowHide.setFont(font)
        TradeLog_ShowHide.setFocusPolicy(QtCore.Qt.StrongFocus)
        TradeLog_ShowHide.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        # TradeLog_ShowHide.setStyleSheet("url:/Resources/Combinear.qss")
        TradeLog_ShowHide.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(TradeLog_ShowHide)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_colId = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_colId.sizePolicy().hasHeightForWidth())
        self.btn_colId.setSizePolicy(sizePolicy)
        self.btn_colId.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_colId.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_colId.setFont(font)
        self.btn_colId.setToolTip("")
        self.btn_colId.setToolTipDuration(2)
        self.btn_colId.setWhatsThis("")
        self.btn_colId.setAccessibleDescription("")
        self.btn_colId.setAutoFillBackground(False)
        self.btn_colId.setStyleSheet("background-color: green;")
        self.btn_colId.setCheckable(True)
        self.btn_colId.setAutoDefault(False)
        self.btn_colId.setObjectName("btn_colId")
        self.verticalLayout_2.addWidget(self.btn_colId)
        self.btn_BtId = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_BtId.sizePolicy().hasHeightForWidth())
        self.btn_BtId.setSizePolicy(sizePolicy)
        self.btn_BtId.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_BtId.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_BtId.setFont(font)
        self.btn_BtId.setToolTip("")
        self.btn_BtId.setToolTipDuration(2)
        self.btn_BtId.setWhatsThis("")
        self.btn_BtId.setAccessibleDescription("")
        self.btn_BtId.setAutoFillBackground(False)
        self.btn_BtId.setStyleSheet("background-color: green;")
        self.btn_BtId.setCheckable(True)
        self.btn_BtId.setAutoDefault(False)
        self.btn_BtId.setObjectName("btn_BtId")
        self.verticalLayout_2.addWidget(self.btn_BtId)
        self.btn_Time = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Time.sizePolicy().hasHeightForWidth())
        self.btn_Time.setSizePolicy(sizePolicy)
        self.btn_Time.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_Time.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Time.setFont(font)
        self.btn_Time.setToolTip("")
        self.btn_Time.setToolTipDuration(2)
        self.btn_Time.setWhatsThis("")
        self.btn_Time.setAccessibleDescription("")
        self.btn_Time.setAutoFillBackground(False)
        self.btn_Time.setStyleSheet("background-color: green;")
        self.btn_Time.setCheckable(True)
        self.btn_Time.setAutoDefault(False)
        self.btn_Time.setObjectName("btn_Time")
        self.verticalLayout_2.addWidget(self.btn_Time)
        self.btn_Synbol = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Synbol.sizePolicy().hasHeightForWidth())
        self.btn_Synbol.setSizePolicy(sizePolicy)
        self.btn_Synbol.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_Synbol.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Synbol.setFont(font)
        self.btn_Synbol.setToolTip("")
        self.btn_Synbol.setToolTipDuration(2)
        self.btn_Synbol.setWhatsThis("")
        self.btn_Synbol.setAccessibleDescription("")
        self.btn_Synbol.setAutoFillBackground(False)
        self.btn_Synbol.setStyleSheet("background-color: green;")
        self.btn_Synbol.setCheckable(True)
        self.btn_Synbol.setAutoDefault(False)
        self.btn_Synbol.setObjectName("btn_Synbol")
        self.verticalLayout_2.addWidget(self.btn_Synbol)
        self.btn_Type = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Type.sizePolicy().hasHeightForWidth())
        self.btn_Type.setSizePolicy(sizePolicy)
        self.btn_Type.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_Type.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Type.setFont(font)
        self.btn_Type.setToolTip("")
        self.btn_Type.setToolTipDuration(2)
        self.btn_Type.setWhatsThis("")
        self.btn_Type.setAccessibleDescription("")
        self.btn_Type.setAutoFillBackground(False)
        self.btn_Type.setStyleSheet("background-color: green;")
        self.btn_Type.setCheckable(True)
        self.btn_Type.setAutoDefault(False)
        self.btn_Type.setObjectName("btn_Type")
        self.verticalLayout_2.addWidget(self.btn_Type)
        self.btn_Action = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Action.sizePolicy().hasHeightForWidth())
        self.btn_Action.setSizePolicy(sizePolicy)
        self.btn_Action.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_Action.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Action.setFont(font)
        self.btn_Action.setToolTip("")
        self.btn_Action.setToolTipDuration(2)
        self.btn_Action.setWhatsThis("")
        self.btn_Action.setAccessibleDescription("")
        self.btn_Action.setAutoFillBackground(False)
        self.btn_Action.setStyleSheet("background-color: green;")
        self.btn_Action.setCheckable(True)
        self.btn_Action.setAutoDefault(False)
        self.btn_Action.setObjectName("btn_Action")
        self.verticalLayout_2.addWidget(self.btn_Action)
        self.btn_Comment = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Comment.sizePolicy().hasHeightForWidth())
        self.btn_Comment.setSizePolicy(sizePolicy)
        self.btn_Comment.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_Comment.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Comment.setFont(font)
        self.btn_Comment.setToolTip("")
        self.btn_Comment.setToolTipDuration(2)
        self.btn_Comment.setWhatsThis("")
        self.btn_Comment.setAccessibleDescription("")
        self.btn_Comment.setAutoFillBackground(False)
        self.btn_Comment.setStyleSheet("background-color: green;")
        self.btn_Comment.setCheckable(True)
        self.btn_Comment.setAutoDefault(False)
        self.btn_Comment.setObjectName("btn_Comment")
        self.verticalLayout_2.addWidget(self.btn_Comment)
        self.btn_BaseAmt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_BaseAmt.sizePolicy().hasHeightForWidth())
        self.btn_BaseAmt.setSizePolicy(sizePolicy)
        self.btn_BaseAmt.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_BaseAmt.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_BaseAmt.setFont(font)
        self.btn_BaseAmt.setToolTip("")
        self.btn_BaseAmt.setToolTipDuration(2)
        self.btn_BaseAmt.setWhatsThis("")
        self.btn_BaseAmt.setAccessibleDescription("")
        self.btn_BaseAmt.setAutoFillBackground(False)
        self.btn_BaseAmt.setStyleSheet("background-color: green;")
        self.btn_BaseAmt.setCheckable(True)
        self.btn_BaseAmt.setAutoDefault(False)
        self.btn_BaseAmt.setObjectName("btn_BaseAmt")
        self.verticalLayout_2.addWidget(self.btn_BaseAmt)
        self.btn_QuoteAmt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_QuoteAmt.sizePolicy().hasHeightForWidth())
        self.btn_QuoteAmt.setSizePolicy(sizePolicy)
        self.btn_QuoteAmt.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_QuoteAmt.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_QuoteAmt.setFont(font)
        self.btn_QuoteAmt.setToolTip("")
        self.btn_QuoteAmt.setToolTipDuration(2)
        self.btn_QuoteAmt.setWhatsThis("")
        self.btn_QuoteAmt.setAccessibleDescription("")
        self.btn_QuoteAmt.setAutoFillBackground(False)
        self.btn_QuoteAmt.setStyleSheet("background-color: green;")
        self.btn_QuoteAmt.setCheckable(True)
        self.btn_QuoteAmt.setAutoDefault(False)
        self.btn_QuoteAmt.setObjectName("btn_QuoteAmt")
        self.verticalLayout_2.addWidget(self.btn_QuoteAmt)
        self.btn_EntryPrice = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_EntryPrice.sizePolicy().hasHeightForWidth())
        self.btn_EntryPrice.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_EntryPrice.setFont(font)
        self.btn_EntryPrice.setStyleSheet("background-color: green;")
        self.btn_EntryPrice.setCheckable(True)
        self.btn_EntryPrice.setObjectName("btn_EntryPrice")
        self.verticalLayout_2.addWidget(self.btn_EntryPrice)
        self.btn_TargPrice = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_TargPrice.sizePolicy().hasHeightForWidth())
        self.btn_TargPrice.setSizePolicy(sizePolicy)
        self.btn_TargPrice.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_TargPrice.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_TargPrice.setFont(font)
        self.btn_TargPrice.setToolTip("")
        self.btn_TargPrice.setToolTipDuration(2)
        self.btn_TargPrice.setWhatsThis("")
        self.btn_TargPrice.setAccessibleDescription("")
        self.btn_TargPrice.setAutoFillBackground(False)
        self.btn_TargPrice.setStyleSheet("background-color: green;")
        self.btn_TargPrice.setCheckable(True)
        self.btn_TargPrice.setAutoDefault(False)
        self.btn_TargPrice.setObjectName("btn_TargPrice")
        self.verticalLayout_2.addWidget(self.btn_TargPrice)
        self.btn_CurPrice = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_CurPrice.sizePolicy().hasHeightForWidth())
        self.btn_CurPrice.setSizePolicy(sizePolicy)
        self.btn_CurPrice.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_CurPrice.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_CurPrice.setFont(font)
        self.btn_CurPrice.setToolTip("")
        self.btn_CurPrice.setToolTipDuration(2)
        self.btn_CurPrice.setWhatsThis("")
        self.btn_CurPrice.setAccessibleDescription("")
        self.btn_CurPrice.setAutoFillBackground(False)
        self.btn_CurPrice.setStyleSheet("background-color: green;")
        self.btn_CurPrice.setCheckable(True)
        self.btn_CurPrice.setAutoDefault(False)
        self.btn_CurPrice.setObjectName("btn_CurPrice")
        self.verticalLayout_2.addWidget(self.btn_CurPrice)
        self.btn_TSL = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_TSL.sizePolicy().hasHeightForWidth())
        self.btn_TSL.setSizePolicy(sizePolicy)
        self.btn_TSL.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_TSL.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_TSL.setFont(font)
        self.btn_TSL.setToolTip("")
        self.btn_TSL.setToolTipDuration(2)
        self.btn_TSL.setWhatsThis("")
        self.btn_TSL.setAccessibleDescription("")
        self.btn_TSL.setAutoFillBackground(False)
        self.btn_TSL.setStyleSheet("background-color: green;")
        self.btn_TSL.setCheckable(True)
        self.btn_TSL.setAutoDefault(False)
        self.btn_TSL.setObjectName("btn_TSL")
        self.verticalLayout_2.addWidget(self.btn_TSL)
        self.btn_PL = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_PL.sizePolicy().hasHeightForWidth())
        self.btn_PL.setSizePolicy(sizePolicy)
        self.btn_PL.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_PL.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_PL.setFont(font)
        self.btn_PL.setToolTip("")
        self.btn_PL.setToolTipDuration(2)
        self.btn_PL.setWhatsThis("")
        self.btn_PL.setAccessibleDescription("")
        self.btn_PL.setAutoFillBackground(False)
        self.btn_PL.setStyleSheet("background-color: green;")
        self.btn_PL.setCheckable(True)
        self.btn_PL.setAutoDefault(False)
        self.btn_PL.setObjectName("btn_PL")
        self.verticalLayout_2.addWidget(self.btn_PL)
        self.btn_PLpercent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_PLpercent.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_PLpercent.sizePolicy().hasHeightForWidth())
        self.btn_PLpercent.setSizePolicy(sizePolicy)
        self.btn_PLpercent.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_PLpercent.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_PLpercent.setFont(font)
        self.btn_PLpercent.setToolTip("")
        self.btn_PLpercent.setToolTipDuration(2)
        self.btn_PLpercent.setWhatsThis("")
        self.btn_PLpercent.setAccessibleDescription("")
        self.btn_PLpercent.setAutoFillBackground(False)
        self.btn_PLpercent.setStyleSheet("background-color: green;")
        self.btn_PLpercent.setCheckable(True)
        self.btn_PLpercent.setAutoDefault(False)
        self.btn_PLpercent.setObjectName("btn_PLpercent")
        self.verticalLayout_2.addWidget(self.btn_PLpercent)
        self.btn_Fees = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Fees.sizePolicy().hasHeightForWidth())
        self.btn_Fees.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Fees.setFont(font)
        self.btn_Fees.setStyleSheet("background-color: green;")
        self.btn_Fees.setCheckable(True)
        self.btn_Fees.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.btn_Fees)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        TradeLog_ShowHide.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TradeLog_ShowHide)
        self.statusbar.setObjectName("statusbar")
        TradeLog_ShowHide.setStatusBar(self.statusbar)

        self.retranslateUi(TradeLog_ShowHide)
        QtCore.QMetaObject.connectSlotsByName(TradeLog_ShowHide)
        TradeLog_ShowHide.setTabOrder(self.btn_colId, self.btn_BtId)
        TradeLog_ShowHide.setTabOrder(self.btn_BtId, self.btn_Time)
        TradeLog_ShowHide.setTabOrder(self.btn_Time, self.btn_Type)
        TradeLog_ShowHide.setTabOrder(self.btn_Type, self.btn_Action)
        TradeLog_ShowHide.setTabOrder(self.btn_Action, self.btn_Comment)
        TradeLog_ShowHide.setTabOrder(self.btn_Comment, self.btn_CurPrice)
        TradeLog_ShowHide.setTabOrder(self.btn_CurPrice, self.btn_TSL)
        TradeLog_ShowHide.setTabOrder(self.btn_TSL, self.btn_PL)
        TradeLog_ShowHide.setTabOrder(self.btn_PL, self.btn_PLpercent)

    def retranslateUi(self, TradeLog_ShowHide):
        _translate = QtCore.QCoreApplication.translate
        TradeLog_ShowHide.setWindowTitle(_translate("TradeLog_ShowHide", "Show/Hide Columns"))
        # TradeLog_ShowHide.setWindowFilePath(_translate("TradeLog_ShowHide", "url:/Resources/Combinear.qss"))
        self.btn_colId.setText(_translate("TradeLog_ShowHide", "Id"))
        self.btn_BtId.setText(_translate("TradeLog_ShowHide", "BtId"))
        self.btn_Time.setText(_translate("TradeLog_ShowHide", "Time"))
        self.btn_Synbol.setText(_translate("TradeLog_ShowHide", "Symbol"))
        self.btn_Type.setText(_translate("TradeLog_ShowHide", "Type"))
        self.btn_Action.setText(_translate("TradeLog_ShowHide", "Action"))
        self.btn_Comment.setText(_translate("TradeLog_ShowHide", "Comment"))
        self.btn_BaseAmt.setText(_translate("TradeLog_ShowHide", "Base Amount"))
        self.btn_QuoteAmt.setText(_translate("TradeLog_ShowHide", "Quote Amount"))
        self.btn_EntryPrice.setText(_translate("TradeLog_ShowHide", "Entry Price"))
        self.btn_TargPrice.setText(_translate("TradeLog_ShowHide", "Target Price"))
        self.btn_CurPrice.setText(_translate("TradeLog_ShowHide", "Current Price"))
        self.btn_TSL.setText(_translate("TradeLog_ShowHide", "TSL"))
        self.btn_PL.setText(_translate("TradeLog_ShowHide", "PL"))
        self.btn_PLpercent.setText(_translate("TradeLog_ShowHide", "PL%"))
        self.btn_Fees.setText(_translate("TradeLog_ShowHide", "Fees"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TradeLog_ShowHide = QtWidgets.QMainWindow()
    ui = Ui_TradeLog_ShowHide()
    ui.setupUi(TradeLog_ShowHide)
    TradeLog_ShowHide.show()
    sys.exit(app.exec_())
