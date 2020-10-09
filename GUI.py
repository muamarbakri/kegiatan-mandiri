import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
#membuat fungsi utk menentukan layout window
def window_go():
   #inisialisasi pyqt
   app = QApplication(sys.argv)
   window = QWidget()

   #menyiapkan label, menempelkan label ke window
   #settext, dan posisi
   x = 0
   label = QLabel(window)
   label.setText("Kotak Angka")
   # style label untuk yang base nya warna hitam
   label.setStyleSheet("color: white")
   label.move(100,0)
   for i in range(5):
      #menginisiasi button nyas
       button = QPushButton(str(i+1),window)
       # mengubah style/tampilan nya
       button.setStyleSheet("color: blue; font-size: 12pt; font-weight: bold; background-color: green")
       # Mengubah Ukuran Button Nya
       button.resize(50,50)
       # memindahkan posisi button nya
       button.move(x,30)
       # variabel x bisa ditambah nilai nya jika tidak terlihat space nya
       x += 50
   #menentukan ukuran window, + title dan menampilkan
   window.setGeometry(100,100,500,500)
   window.setWindowTitle("PyQT Pertama")
   window.show()
   sys.exit(app.exec_())


if _name_ == '_main_':
   window_go()
