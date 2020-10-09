import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

#membuat fungsi utk menentukan layout window
def window_go():
   #inisialisasi pyqt
   app = QApplication(sys.argv)
   window = QWidget()

   #menyiapkan label, menempelkan label ke window
   #settext, dan posisi


   label2=[None]*10
   baris = 30
   for a in range(10):
      baris = baris + 15
      label2[a] = QLabel(window)
      label2[a].setText("Lagi " + str(a))
      label2[a].move(110,baris)


   #menentukan ukuran window, + title dan menampilkan
   window.setGeometry(50,50,320,200)
   window.setWindowTitle("PyQt5 Example")
   window.show()
   sys.exit(app.exec_())


if _name_ == '_main_':
   window_go()
