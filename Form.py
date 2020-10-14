import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QWidget()
    form.setGeometry(80,80,800,300)
    form.setWindowTitle("Belajar Pyqt Form")

#Menampilkan teks label
    label = QLabel(form)
    label.setText("Input Biodata")
    label.setStyleSheet("background-color: grey; color: red; font: bold 30px; ")

    lineEdit1 = QLineEdit()
    lineEdit2 = QLineEdit()
    lineEdit3 = QLineEdit()

    layout = QFormLayout()
    layout.addRow(label)
    layout.addRow("Name", lineEdit1)
    layout.addRow("Adress", lineEdit2)
    layout.addWidget(lineEdit3)

#Menampilkan pilihan klik persegi
    check1 = QCheckBox("Makan")
    check2 = QCheckBox("Tidur")
    check3 = QCheckBox("Main")
    layout.addRow("Hobby", check1)
    layout.addWidget(check2)
    layout.addWidget(check3)

#Menampilkan pilihan klik lingkaran
    rad1 = QRadioButton("Pelajar")
    rad2 = QRadioButton("Pegawai")
    rad3 = QRadioButton("Wirasawasta")
    layout.addRow("Status", rad1)
    layout.addWidget(rad2)
    layout.addWidget(rad3)




    form.setLayout(layout)
    form.show()
    app.exec_()
