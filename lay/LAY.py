from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox, QApplication, QLineEdit, QLabel, QComboBox, QDialog, QWidget, QListWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt, QUrl
from escpos.printer import Usb
import sys

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome to Your Favorite Fast Food Hub!")

        
        self.set_background("MENU.jpg")

        self.button = QPushButton("ВЫЙТИ", self)
        self.button.setGeometry(1100, 650, 200, 50)
        self.button.clicked.connect(self.Close_window)

        self.btn_mc = QPushButton("MCdonalds", self)
        self.btn_mc.setGeometry(475, 150, 400, 100)
        self.btn_mc.clicked.connect(self.mc_pushed)

        self.setStyleSheet("""
        QPushButton{
                background-color: orange; 
                color: black;            
                border-radius: 10px;
                font-size: 20px;
                border: 2px solid black; 
        }       
        QPushButton:hover{  
                background-color: lightgreen; 
        }
        QPushButton:pressed{
                background-color: orange; 
        }
        """)

        self.btn_kfc = QPushButton("KFC", self)
        self.btn_kfc.setGeometry(475, 300, 400, 100)
        self.btn_kfc.clicked.connect(self.kfc_pushed)

        self.btn_bk = QPushButton("Burger King", self)
        self.btn_bk.setGeometry(475, 450, 400, 100)
        self.btn_bk.clicked.connect(self.bk_pushed)

        self.btn_cart = QPushButton("Корзина", self)
        self.btn_cart.setGeometry(475, 600, 400, 100)
        self.btn_cart.clicked.connect(self.cart_pushed)



        self.cart = []

    def mc_pushed(self):
        self.window_mc = Window_mc(self.cart)
        self.window_mc.showFullScreen()

    def kfc_pushed(self):
        self.window_kfc = Window_kfc(self.cart)
        self.window_kfc.showFullScreen()

    def bk_pushed(self):
        self.window_bk = Window_bk(self.cart)
        self.window_bk.showFullScreen()

    def cart_pushed(self):
        self.window_cart = CartWindow(self.cart)
        self.window_cart.show()

    def set_background(self, image_path):
        oImage = QPixmap(image_path)
        sImage = oImage.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def resizeEvent(self, event):
        self.set_background("MENU.jpg")
        super().resizeEvent(event)

    

    def toggle_recording(self):
        if self.recording:
            self.stop_recording()
        else:
            self.start_recording()

    def start_recording(self):
        self.mediaRecorder.setOutputLocation(QUrl.fromLocalFile('output.mp4'))
        self.mediaRecorder.record()
        self.recording = True
        self.btn_record.setText("Stop Recording")

    def stop_recording(self):
        self.mediaRecorder.stop()
        self.recording = False
        self.btn_record.setText("Record Video")

    def Close_window(self):
        self.close()
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Window_mc(QWidget):
    def __init__(self, cart):
        super().__init__()
        self.cart = cart

        self.setWindowTitle("Меню Макдональдс")
        self.setGeometry(150, 20, 1000, 800)
        
        self.set_background("food.jpg")

        self.button = QPushButton("ЗАКРЫТЬ ЭТО ОКНО", self)
        self.button.setGeometry(1100, 650, 200, 50)
        self.button.clicked.connect(self.Close_window)

        self.setStyleSheet("""
            QPushButton{
                background-color: lightblue;
                color: black;
                border-radius: 10px;
                font-size: 40 px;
            }
            QPushButton:pressed{
                background: white;
            }
            QPushButton:hover{
                background:grey;
            }
            QComboBox {
                background-color: lightblue;
                color: black;
                border-radius: 25px;
            }
        """)

        

        # Макбургер
        self.label_name = QLabel("<h2 style= 'color:black;'>Макбургер</h2>", self)
        self.label_name.move(200, 175)
        label = QLabel("<h3 style='color:black;'>169 Рублей</h3>", self)
        label.move(200, 295)
        self.lbl_ham = QLabel(self)
        pixmap_ham = QPixmap('ham.png')
        scaled_pixmap_ham = pixmap_ham.scaled(200, 180, aspectRatioMode=Qt.KeepAspectRatio)
        self.lbl_ham.setPixmap(scaled_pixmap_ham)
        self.lbl_ham.move(160, 144)
        
        self.button_ham = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_ham.setGeometry(170, 325, 150, 25)
        self.button_ham.clicked.connect(lambda: self.add_to_cart("Макбургер", 169))
        self.button_ham.setFixedHeight(25)
    
        # Чизбургер
        self.label_name = QLabel("<h2 style= 'color:black;'>Чизбургер</h2>", self)
        self.label_name.move(370, 175)

        label_cheese = QLabel("<h3 style='color:black;'>199 Рублей</h3>", self)
        label_cheese.move(385, 295)
        self.lbl_cheese = QLabel(self)
        pixmap_cheese = QPixmap('ham_cheese.png')
        scaled_pixmap_cheese = pixmap_cheese.scaled(200, 180, aspectRatioMode=Qt.KeepAspectRatio)
        self.lbl_cheese.setPixmap(scaled_pixmap_cheese)
        self.lbl_cheese.move(335, 160)
        
        
        self.button_ham_cheese = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_ham_cheese.setGeometry(350, 325, 150, 25)
        self.button_ham_cheese.clicked.connect(lambda: self.add_to_cart("Чизбургер", 199))
        self.button_ham_cheese.setFixedHeight(25)
        

        # Картошка фри
        self.label_name = QLabel("<h2 style= 'color:black;'>Картошка фри</h2>", self)
        self.label_name.move(520, 175)

        self.lbl_fries_price = QLabel("<h3 style='color:black;'>99 Рублей (Маленькая)</h3>", self)
        self.lbl_fries_price.move(520, 295)
        self.lbl_fries = QLabel(self)
        pixmap_fries = QPixmap('fries.png')
        scaled_pixmap_fries = pixmap_fries.scaled(300, 200, aspectRatioMode=Qt.KeepAspectRatio)
        self.lbl_fries.setPixmap(scaled_pixmap_fries)
        self.lbl_fries.move(500, 160)
        
        
        self.button_fries = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_fries.setGeometry(530, 325, 150, 25)
        self.button_fries.clicked.connect(lambda: self.add_to_cart("Картошка фри", self.get_fries_price()))
        self.button_fries.setFixedHeight(25)
        

        self.combo_fries = QComboBox(self)
        self.combo_fries.setGeometry(530, 355, 150, 25)
        self.combo_fries.addItems(["Маленькая - 99 Рублей", "Средняя - 129 Рублей", "Большая - 149 Рублей"])
        self.combo_fries.currentIndexChanged.connect(self.update_fries_price)
       

        # МакФлури
        self.label_name = QLabel("<h2 style= 'color:black'>МакФлури</h2>", self)
        self.label_name.move(725, 175)
        self.lbl_furry = QLabel(self)
        furry_pixmap = QPixmap('mcflurry.png')
        scaled_furry_pixmap = furry_pixmap.scaled(200, 100, aspectRatioMode= Qt.KeepAspectRatio)
        self.lbl_furry.setPixmap(scaled_furry_pixmap)
        self.lbl_furry.move(730, 195)
        self.label_price = QLabel("<h3 style='color:black;'>119 Рублей</h3>", self)
        self.label_price.move(745, 295)
        
        
        self.btn_mcflury = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.btn_mcflury.setGeometry(710, 325, 150, 25)
        self.btn_mcflury.clicked.connect(lambda: self.add_to_cart("МакФлури", 119))
        self.btn_mcflury.setFixedHeight(25)

        #МАК КОМБООООО
        self.label = QLabel("<h2 style= 'color:black;'>МакКомбо</h2>", self)
        self.label.move(930, 175)
        self.lbl_mc = QLabel(self)
        mc_pixmap = QPixmap('mc_combo.png')
        scaled_mc_pixmap = mc_pixmap.scaled(200, 100, aspectRatioMode= Qt.KeepAspectRatio)
        self.lbl_mc.setPixmap(scaled_mc_pixmap)
        self.lbl_mc.move(910, 195)

        self.lale = QLabel("<h3 style='color:black;'>139 Рублей</h3>", self)
        self.lale.move(910, 295)
        
        
        self.btn_mccombo = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.btn_mccombo.setGeometry(890, 325, 150, 25)
        self.btn_mccombo.clicked.connect(lambda: self.add_to_cart("МакКомбо", 139))
        self.btn_mccombo.setFixedHeight(25)

        #КОКА КОЛААААААААА
        self.label_cola = QLabel("<h2 style= 'color:black'>Кока кола классика</h2>", self)
        self.label_cola.move(180, 400)
        self.lbl_cola = QLabel(self)
        cola_pixmap = QPixmap('mc_cola.png')
        scaled_cola_pixmap = cola_pixmap.scaled(250, 150, aspectRatioMode= Qt.KeepAspectRatio)
        self.lbl_cola.setPixmap(scaled_cola_pixmap)
        self.lbl_cola.move(180, 430)

        self.cola_price = QLabel("<h3 style= 'color:black'>69 Рублей</h3>", self)
        self.cola_price.move(220, 570)

        self.button_cola = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_cola.setGeometry(190, 600, 150, 25)
        self.button_cola.clicked.connect(lambda: self.add_to_cart("Кока Кола", 69))
        
        

    def add_to_cart(self, item, price):
        self.cart.append((item, price))
        QMessageBox.information(self, "Добавлено в корзину", f"{item} за {price} рублей добавлен в корзину")

    def get_fries_price(self):
        prices = {
            0: 99,
            1: 129,
            2: 149
        }
        selected_index = self.combo_fries.currentIndex()
        return prices[selected_index]

    def update_fries_price(self):
        prices = {
            0: "<h3 style='color:black;'>99 Рублей (Маленькая)</h3>",
            1: "<h3 style='color:black;'>129 Рублей (Средняя)</h3>",
            2: "<h3 style='color:black;'>149 Рублей (Большая)</h3>"
        }
        selected_index = self.combo_fries.currentIndex()
        self.lbl_fries_price.setText(prices[selected_index])

    def set_background(self, image_path):
        oImage = QPixmap(image_path)
        sImage = oImage.scaled(self.size(), Qt.KeepAspectRatioByExpanding)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def resizeEvent(self, event):
        self.set_background("food.jpg")
        super().resizeEvent(event)

    def Close_window(self):
        self.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Window_kfc(QWidget):
    def __init__(self, cart):
        super().__init__()
        self.cart = cart

        self.setWindowTitle("Меню КФС")
        self.setGeometry(150, 20, 1000, 800)

        self.set_background("food.jpg")

        self.button = QPushButton("ЗАКРЫТЬ ЭТО ОКНО", self)
        self.button.setGeometry(1100, 650, 200, 50)
        self.button.clicked.connect(self.Close_window)

        self.setStyleSheet("""
            QPushButton{
                background-color: lightblue;
                color: black;
                border-radius: 10px;
            }
            QPushButton:pressed{
                background: white;
            }
            QPushButton:hover{
                background:grey;
            }
            QComboBox{
                background-color: lightblue;
                color: black;
                border-radius: 25px;
            }
        """)

        
        #ЛОНГЕЕР
        self.label_longer_name = QLabel("<h2 style= 'color:black;'>Лонгер</h2>", self)
        self.label_longer_name.move(680, 175)

        self.longer_price = QLabel("<h3 style= 'color:black'>99 Рублей</h3", self)
        self.longer_price.move(680, 315)


        self.lbl_pixmap = QLabel(self)
        longer_pixmap = QPixmap('longer.png')
        scaled_longer_pixmap = longer_pixmap.scaled(250, 150, aspectRatioMode= Qt. KeepAspectRatio)
        self.lbl_pixmap.setPixmap(scaled_longer_pixmap)
        self.lbl_pixmap.move(655, 175)
        
        self.button_nuggets = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_nuggets.setGeometry(650, 335, 150, 25)
        self.button_nuggets.clicked.connect(lambda: self.add_to_cart("Лонгер", 99))
        

        #КАРТОШКА ФРИИИИ
        self.label_name = QLabel("<h2 style= 'color:black;'>Картошка фри</h2>", self)
        self.label_name.move(490, 175)

        self.label_frie = QLabel("<h3 style = 'color:black'>99 рублей (Маленькая)</h3>", self)
        self.label_frie.move(470, 315)
        


        self.lbl_kfc = QLabel(self)
        kfc_pixmap = QPixmap('kfc.png')
        scaled_kfc_pixmap = kfc_pixmap.scaled(200, 100, aspectRatioMode= Qt.KeepAspectRatio)
        self.lbl_kfc.setPixmap(scaled_kfc_pixmap)
        self.lbl_kfc.move(470, 215)
        
        self.button_chicken = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_chicken.setGeometry(470, 335, 150, 25)
        self.button_chicken.clicked.connect(lambda: self.add_to_cart("Картошка фри", self.get_chicken_price()))
        

        self.combo_chicken = QComboBox(self)
        self.combo_chicken.setGeometry(470, 365, 150, 25)
        self.combo_chicken.addItems(["Маленький - 99 Рублей", "Средний - 129 Рублей", "Большой - 149 Рублей"])
        self.combo_chicken.currentIndexChanged.connect(self.update_chicken_price)
        
        #ЧИКЕНБУРГЕР
        self.label_name = QLabel("<h2 style= 'color:black;'>Чикенбургер</h2>", self)
        self.label_name.move(320, 175)

        
        self.lbl_chicken = QLabel(self)
        chick_pixmap = QPixmap("chicken_burg.png")
        scaled_chick_pixmap = chick_pixmap.scaled(280, 200, aspectRatioMode=Qt.KeepAspectRatio)
        self.lbl_chicken.setPixmap(scaled_chick_pixmap)
        self.lbl_chicken.move(275, 175)

        self.label_chick = QLabel("<h3 style = 'color:black;'>59 Рублей</h3>", self)
        self.label_chick.move(320, 315)
        
        self.button_burger = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_burger.setGeometry(290, 335, 150, 25)
        self.button_burger.clicked.connect(lambda: self.add_to_cart("Чикенбургер", 159))
        
        #КУРИНЫЕ КРЫЛЫШКИ
        self.label_name = QLabel("<h2 style= 'color:black;'>Крылышки</h2>", self)
        self.label_name.move(140, 175)

        self.label = QLabel("<h3 style = 'color:black;'>159 Рублей</h3>", self)
        self.label.move(140, 315)
        
        self.lbl_wing = QLabel(self)
        wing = QPixmap('wings.png')
        scaled_wing = wing.scaled(300, 280, aspectRatioMode=Qt.KeepAspectRatio)
        self.lbl_wing.setPixmap(scaled_wing)
        self.lbl_wing.move(65, 125)
        
        self.button_wings = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_wings.setGeometry(110, 335, 150, 25)
        self.button_wings.clicked.connect(lambda: self.add_to_cart("Куриные крылышки", 159))
        
    def add_to_cart(self, item, price):
        self.cart.append((item, price))
        QMessageBox.information(self, "Добавлено в корзину", f"{item} за {price} рублей добавлен в корзину")

    def get_nuggets_price(self):
        prices = {
            0: 79,
            1: 149,
            2: 199
        }
        selected_index = self.combo_nuggets.currentIndex()
        return prices[selected_index]

    def update_nuggets_price(self):
        prices = {
            0: "<h3 style='color:black;'>Маленький - 99 Рублей</h3>",
            1: "<h3 style='color:black;'>Средний - 129 Рублей</h3>",
            2: "<h3 style='color:black;'>Большой - 149 Рублей</h3>"
        }
        selected_index = self.combo_nuggets.currentIndex()
        self.lbl_nuggets_price.setText(prices[selected_index])

    def get_chicken_price(self):
        prices = {
            0: 99,
            1: 129,
            2: 149
        }
        selected_index = self.combo_chicken.currentIndex()
        return prices[selected_index]

    def update_chicken_price(self):
        prices = {
            0: "<h3 style='color:black;'>99 Рублей - Маленький</h3>",
            1: "<h3 style='color:black;'>129 Рублей - Средний</h3>",
            2: "<h3 style='color:black;'>149 Рублей - Большой</h3>"
        }
        selected_index = self.combo_chicken.currentIndex()
        self.label_frie.setText(prices[selected_index])

    def get_wings_price(self):
        prices = {
            0: 129,
            1: 249,
            2: 369
        }
        selected_index = self.combo_wings.currentIndex()
        return prices[selected_index]

    def update_wings_price(self):
        prices = {
            0: "<h3 style='color:black;'>129 Рублей (3 шт.)</h3>",
            1: "<h3 style='color:black;'>249 Рублей (6 шт.)</h3>",
            2: "<h3 style='color:black;'>369 Рублей (9 шт.)</h3>"
        }
        selected_index = self.combo_wings.currentIndex()
        self.lbl_wings_price.setText(prices[selected_index])

    def set_background(self, image_path):
        oImage = QPixmap(image_path)
        sImage = oImage.scaled(self.size(), Qt.KeepAspectRatioByExpanding)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def resizeEvent(self, event):
        self.set_background("food.jpg")
        super().resizeEvent(event)


    def Close_window(self):
        self.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Window_bk(QWidget):
    def __init__(self, cart):
        super().__init__()
        self.cart = cart

        self.setWindowTitle("Меню Бургер Кинг")
        self.setGeometry(150, 20, 1000, 800)

        self.set_background("food.jpg")

        self.button = QPushButton("ЗАКРЫТЬ ЭТО ОКНО", self)
        self.button.setGeometry(1100, 650, 200, 50)
        self.button.clicked.connect(self.Close_window)

        self.setStyleSheet("""
            QPushButton{
                background-color: lightblue;
                color: black;
                border-radius: 10px;
            }
            QPushButton:pressed{
                background: white;
            }
            QPushButton:hover{
                background:grey;
            }
            QComboBox{
                background-color: lightblue;
                color: black;
                border-radius: 25px;
            }
        """)

        
        #ВОППЕР
        self.label_name = QLabel("<h2 style= 'color:black;'>Воппер</h2>", self)
        self.label_name.move(150, 175)

        self.label_woper = QLabel(self)
        woper_pixmap = QPixmap("woper.png")
        scaled_woper_pixmap = woper_pixmap.scaled(150, 150, aspectRatioMode=Qt.KeepAspectRatio)
        self.label_woper.setPixmap(scaled_woper_pixmap)
        self.label_woper.move(130, 185)
        
        self.label_woper_price = QLabel("<h3 style='color:black;'>199 Рублей</h3>", self)
        self.label_woper_price.move(140, 315)
       
        self.button_whopper = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_whopper.setGeometry(110, 335, 150, 25)
        self.button_whopper.clicked.connect(lambda: self.add_to_cart("Воппер", 299))
       

        #ЛУКОВЫЕ КОЛЬЦА
        self.label_name = QLabel("<h2 style= 'color:black;'>Луковые кольца</h2>", self)
        self.label_name.move(290, 175)

        self.label_onion_rings = QLabel(self)
        onion_rings_pixmap = QPixmap("onion_rings.png")
        scaled_onion_rings_pixmap = onion_rings_pixmap.scaled(280, 200, aspectRatioMode=Qt.KeepAspectRatio)
        self.label_onion_rings.setPixmap(scaled_onion_rings_pixmap)
        self.label_onion_rings.move(240, 130)
        
        self.label_nuggets_price = QLabel("<h3 style='color:black;'>Маленькая - 69 Рублей</h3>", self)
        self.label_nuggets_price.move(295, 315)
    
       
        self.button_king_fries = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_king_fries.setGeometry(290, 335, 150, 25)
        self.button_king_fries.clicked.connect(lambda: self.add_to_cart("Луковые кольца", 69))
        
        
        #РОЛЛ
        self.label_name = QLabel("<h2 style= 'color:black;'>Ролл</h2>", self)
        self.label_name.move(690, 175)
        
        self.lbl_long_chicken = QLabel(self)
        pixmap_long_chicken = QPixmap('roll.png')
        scaled_pixmap_long_chicken = pixmap_long_chicken.scaled(200, 150, aspectRatioMode=Qt.KeepAspectRatio)
        self.lbl_long_chicken.setPixmap(scaled_pixmap_long_chicken)
        self.lbl_long_chicken.move(640, 200)
        
        self.lbl_long_chicken_price = QLabel("<h3 style='color:black;'>199 Рублей</h3>", self)
        self.lbl_long_chicken_price.move(680, 315)
        
        self.button_long_chicken = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_long_chicken.setGeometry(650, 335, 150, 25)
        self.button_long_chicken.clicked.connect(lambda: self.add_to_cart("Ролл", 199))
        
        #КАРТОШКА ФРИ
        self.label_name = QLabel("<h2 style= 'color:black;'>Картошка фри</h2>", self)
        self.label_name.move(490, 175)

        self.label_fries = QLabel(self)
        fries_pixmap = QPixmap("fries_bk.png")
        scaled_fries_pixmap = fries_pixmap.scaled(280, 200, aspectRatioMode=Qt.KeepAspectRatio)
        self.label_fries.setPixmap(scaled_fries_pixmap)
        self.label_fries.move(435, 140)
        
        self.label_fries_price = QLabel("<h3 style='color:black;'>89 Рублей (Маленькая)</h3>", self)
        self.label_fries_price.move(470, 315)
        
        self.button_chicken_fries = QPushButton("ДОБАВИТЬ В КОРЗИНУ", self)
        self.button_chicken_fries.setGeometry(470, 335, 150, 25)
        self.button_chicken_fries.clicked.connect(lambda: self.add_to_cart("Картошка Фри", self.get_chicken_fries_price()))
        

        self.combo_chicken_fries = QComboBox(self)
        self.combo_chicken_fries.setGeometry(470, 365, 150, 25)
        self.combo_chicken_fries.addItems(["Маленький - 89 Рублей", "Средний - 129 Рублей", "Большой - 169 Рублей"])
        self.combo_chicken_fries.currentIndexChanged.connect(self.update_chicken_fries_price)

    def add_to_cart(self, item, price):
        self.cart.append((item, price))
        QMessageBox.information(self, "Добавлено в корзину", f"{item} за {price} рублей добавлен в корзину")

    def get_king_fries_price(self):
        prices = {
            0: 69,
            1: 99,
            2: 129
        }
        selected_index = self.button_king_fries.currentIndex()
        return prices[selected_index]

    def get_chicken_fries_price(self):
        prices = {
            0: 89,
            1: 129,
            2: 169
        }
        selected_index = self.combo_chicken_fries.currentIndex()
        return prices[selected_index]

    def update_chicken_fries_price(self):
        prices = {
            0: "<h3 style='color:black;'>89 Рублей (Маленький)</h3>",
            1: "<h3 style='color:black;'>129 Рублей (Средний)</h3>",
            2: "<h3 style='color:black;'>169 Рублей (Большой)</h3>"
        }
        selected_index = self.combo_chicken_fries.currentIndex()
        self.label_fries_price.setText(prices[selected_index])

    def set_background(self, image_path):
        oImage = QPixmap(image_path)
        sImage = oImage.scaled(self.size(), Qt.KeepAspectRatioByExpanding)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def resizeEvent(self, event):
        self.set_background("food.jpg")
        super().resizeEvent(event)

    def Close_window(self):
        self.close()


class CartWindow(QWidget):
    def __init__(self, cart):
        super().__init__()
        self.cart = cart

        self.setWindowTitle("Корзина")
        self.setGeometry(300, 150, 600, 600)

        layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Введите ваше имя")
        layout.addWidget(self.name_input)

        self.cart_list = QListWidget(self)
        layout.addWidget(self.cart_list)

        for item, price in self.cart:
            self.cart_list.addItem(f"{item} - {price} Рублей")

        self.total_price_label = QLabel(self)
        layout.addWidget(self.total_price_label)
        self.update_total_price()

        self.remove_button = QPushButton("Удалить выбранный предмет", self)
        self.remove_button.setStyleSheet("background:red; color:black; font-size: 17px;")
        self.remove_button.clicked.connect(self.remove_selected_item)
        layout.addWidget(self.remove_button)

        self.receipt_button = QPushButton("Показать чек", self)
        self.receipt_button.clicked.connect(self.show_receipt)
        self.receipt_button.setStyleSheet("background:green; color:black; font-size: 17px;")
        layout.addWidget(self.receipt_button)

        self.setLayout(layout)

    def update_total_price(self):
        global total_price
        global dur
        total_price = sum(price for item, price in self.cart)
        dur = total_price * 0.15
        self.total_price_label.setText(f"Цена за обслуживание: 15% от общей суммы \nИтог: {total_price + dur} Рублей (цена за обслуживание включено) ")

    def remove_selected_item(self):
        selected_items = self.cart_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Ошибка", "Выберите предмет для удаления")
            return
        for item in selected_items:
            row = self.cart_list.row(item)
            self.cart_list.takeItem(row)
            self.cart.pop(row)
        self.update_total_price()

    def show_receipt(self):
        name = self.name_input.text()
        if not name:
            QMessageBox.warning(self, "Ошибка", "Введите ваше имя")
            return

        receipt_dialog = ReceiptDialog(self.cart, name)
        receipt_dialog.exec_()


class ReceiptDialog(QDialog):
    def __init__(self, cart, name):
        super().__init__()
        self.cart = cart
        self.name = name
        self.setWindowTitle("Чек")
        self.setGeometry(500, 100, 400, 400)
        
        layout = QVBoxLayout()

        lbl_scan = QLabel(self)
        scan_pixmap = QPixmap("scan.jpg")
        scaled_scan_pixmap = scan_pixmap.scaled(400, 400, Qt.KeepAspectRatio)
        lbl_scan.setPixmap(scaled_scan_pixmap)
        layout.addWidget(lbl_scan)

        receipt_label = QLabel(self)
        receipt_text = "\n".join([f"{item} - {price} Рублей" for item, price in self.cart])
        receipt_label.setText(receipt_text)

        name_label = QLabel(self)
        name_label.setText(f"Имя: {self.name}")

        self.button_check = QPushButton("Распечатать", self)
        self.button_check.setStyleSheet("background:lightgreen; color:black; font-size: 17px;")
        self.button_check.clicked.connect(self.print_receipt)
        
        layout.addWidget(self.button_check)
        layout.addWidget(receipt_label)
        layout.addWidget(name_label)

        self.setLayout(layout)

        # Подключение к принтеру
        try:
            # Замените 'idVendor' и 'idProduct' на значения, соответствующие вашему принтеру
            self.printer = Usb(0x04b8, 0x0202)  # Примерные значения, необходимо уточнить
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось подключиться к принтеру: {str(e)}")

    def print_receipt(self):
        try:
            self.printer.text("Чек\n")
            for item, price in self.cart:
                self.printer.text(f"{item} - {price} Рублей\n")
            self.printer.text(f"Имя: {self.name}\n")
            self.printer.cut()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка печати", f"Не удалось напечатать: {str(e)}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Menu()
    mainWindow.showFullScreen()
    sys.exit(app.exec_())





        