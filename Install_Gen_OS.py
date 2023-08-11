from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_Dialog(object):
    def downloadandrun(self):
        os.system("wget ftsetup.sh https://raw.githubusercontent.com/crazycheetah42/GenOS-Tools/main/ftsetup.sh")
        os.system("chmod +x ftsetup.sh")
        os.system('gnome-terminal -- bash -c "sudo ./ftsetup.sh"')
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(302, 472)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 251, 24))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 170, 150, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.downloadandrun)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 410, 301, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 430, 211, 18))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gen OS Installer"))
        self.label.setText(_translate("Dialog", "Welcome to Gen OS!"))
        self.label_2.setText(_translate("Dialog", "Click Begin Installation to install Gen OS."))
        self.pushButton.setText(_translate("Dialog", "Begin Installation"))
        self.label_3.setText(_translate("Dialog", "Note: Gen OS is not an ISO. Do not download"))
        self.label_4.setText(_translate("Dialog", "any ISOs that claim to be Gen OS."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
