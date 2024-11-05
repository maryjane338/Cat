from PIL import Image
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import os
import sys


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cat')
        self.resize(380, 260)

        self.label = QLabel()

        open_btn = QPushButton('Открыть файл')
        btn_rotate_clockwise = QPushButton('По часовой стрелке')
        btn_rotate_counter_clockwise = QPushButton('Против часовой стрелки')
        btn_red = QPushButton('R')
        btn_green = QPushButton('G')
        btn_blue = QPushButton('B')
        btn_all = QPushButton('ALL')
        open_btn.clicked.connect(self.open)
        btn_rotate_clockwise.clicked.connect(self.rotate_clockwise)
        btn_rotate_counter_clockwise.clicked.connect(self.rotate_counter_clockwise)
        btn_red.clicked.connect(self.red_colored)
        btn_green.clicked.connect(self.green_colored)
        btn_blue.clicked.connect(self.blue_colored)
        btn_all.clicked.connect(self.all_colored)

        self.slider = QSlider()
        self.slider.setMinimum(0)
        self.slider.setMaximum(256)
        self.slider.setValue(256)
        self.slider.valueChanged.connect(self.make_transparent)

        self.transform = QTransform()
        self.rotate = 0
        self.transform.rotate(self.rotate)

        self.pixmap_empty = QPixmap()

        main_l = QHBoxLayout()
        v_l1 = QVBoxLayout()
        v_l2 = QVBoxLayout()
        v_l3 = QVBoxLayout()
        v_l1.addWidget(btn_red)
        v_l1.addWidget(btn_green)
        v_l1.addWidget(btn_blue)
        v_l1.addWidget(btn_all)
        v_l1.addStretch()
        v_l2.addWidget(self.label)
        v_l2.addStretch()
        v_l3.addWidget(self.slider)
        v_l2.addWidget(btn_rotate_counter_clockwise)
        v_l1.addWidget(open_btn)
        v_l1.addWidget(btn_rotate_clockwise)
        main_l.addLayout(v_l1)
        main_l.addLayout(v_l2)
        main_l.addLayout(v_l3)
        self.setLayout(main_l)

    def open(self):
        file = QFileDialog.getOpenFileName(self, 'Выберите файл')[0]
        if file:
            img = Image.open(file)
            img.save('image/cat.jpg')
            red, green, blue = img.split()
            zeroed_band = red.point(lambda _: 0)
            red_merge = Image.merge('RGB', (red, zeroed_band, zeroed_band))
            red_merge.save('image/cat_red_merge.jpg')
            green_merge = Image.merge('RGB', (zeroed_band, green, zeroed_band))
            green_merge.save('image/cat_green_merge.jpg')
            blue_merge = Image.merge('RGB', (zeroed_band, zeroed_band, blue))
            blue_merge.save('image/cat_blue_merge.jpg')

            self.pixmap_empty.load('image/cat.jpg')
            self.pixmap = self.pixmap_empty.scaled(200, 200)
            self.label.setPixmap(self.pixmap)

            self.transparent = Image.open('image/cat.jpg')
        else:
            message = QMessageBox()
            message.setWindowTitle('Инфо')
            message.setText('Файл не выбран')
            message.exec()

    def rotate_clockwise(self):
        clockwise_rotation = self.rotate
        if self.rotate == clockwise_rotation:
            self.rotate = 90
            clockwise_rotation = self.rotate
            self.transform.rotate(clockwise_rotation)
        transformed_pixmap = self.pixmap.transformed(self.transform)
        self.label.setPixmap(transformed_pixmap)

    def rotate_counter_clockwise(self):
        counter_clockwise_rotation = self.rotate
        if self.rotate == counter_clockwise_rotation:
            self.rotate = -90
            counter_clockwise_rotation = self.rotate
            self.transform.rotate(counter_clockwise_rotation)
        transformed_pixmap = self.pixmap.transformed(self.transform)
        self.label.setPixmap(transformed_pixmap)

    def red_colored(self):
        pixmap_red = QPixmap()
        pixmap_red.load("image/cat_red_merge.jpg")
        self.transparent = Image.open("image/cat_red_merge.jpg")
        self.slider.setValue(256)
        pixmap_red_scaled = pixmap_red.scaled(200, 200)
        self.pixmap.swap(pixmap_red_scaled)
        self.label.setPixmap(self.pixmap)
        red_rotation = self.rotate
        if self.rotate == red_rotation:
            self.rotate = 0
            red_rotation = self.rotate
            self.transform.rotate(red_rotation)
        transformed_pixmap = self.pixmap.transformed(self.transform)
        self.label.setPixmap(transformed_pixmap)

    def green_colored(self):
        pixmap_green = QPixmap()
        pixmap_green.load("image/cat_green_merge.jpg")
        self.transparent = Image.open("image/cat_green_merge.jpg")
        self.slider.setValue(256)
        pixmap_green_scaled = pixmap_green.scaled(200, 200)
        self.pixmap.swap(pixmap_green_scaled)
        self.label.setPixmap(self.pixmap)
        green_rotation = self.rotate
        if self.rotate == green_rotation:
            self.rotate = 0
            green_rotation = self.rotate
            self.transform.rotate(green_rotation)
        transformed_pixmap = self.pixmap.transformed(self.transform)
        self.label.setPixmap(transformed_pixmap)

    def blue_colored(self):
        pixmap_blue = QPixmap()
        pixmap_blue.load("image/cat_blue_merge.jpg")
        self.transparent = Image.open("image/cat_blue_merge.jpg")
        self.slider.setValue(256)
        pixmap_blue_scaled = pixmap_blue.scaled(200, 200)
        self.pixmap.swap(pixmap_blue_scaled)
        self.label.setPixmap(self.pixmap)
        blue_rotation = self.rotate
        if self.rotate == blue_rotation:
            self.rotate = 0
            blue_rotation = self.rotate
            self.transform.rotate(blue_rotation)
        transformed_pixmap = self.pixmap.transformed(self.transform)
        self.label.setPixmap(transformed_pixmap)

    def all_colored(self):
        pixmap_og = QPixmap()
        pixmap_og.load("image/cat.jpg")
        self.transparent = Image.open("image/cat.jpg")
        self.slider.setValue(256)
        pixmap_og_scaled = pixmap_og.scaled(200, 200)
        self.pixmap.swap(pixmap_og_scaled)
        self.label.setPixmap(self.pixmap)
        all_rotation = self.rotate
        if self.rotate == all_rotation:
            self.rotate = 0
            all_rotation = self.rotate
            self.transform.rotate(all_rotation)
        transformed_pixmap = self.pixmap.transformed(self.transform)
        self.label.setPixmap(transformed_pixmap)

    def make_transparent(self):
        size = self.slider.value()
        self.transparent.putalpha(size)
        self.transparent.save('image/cat_transparent.png')
        pixmap_transparent = QPixmap()
        pixmap_transparent.load('image/cat_transparent.png')
        pixmap_transparent_scaled = pixmap_transparent.scaled(200, 200)
        self.pixmap.swap(pixmap_transparent_scaled)
        self.label.setPixmap(self.pixmap)
        transparent_rotation = self.rotate
        if self.rotate == transparent_rotation:
            self.rotate = 0
            transparent_rotation = self.rotate
            self.transform.rotate(transparent_rotation)
        transformed_pixmap = self.pixmap.transformed(self.transform)
        self.label.setPixmap(transformed_pixmap)

def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
