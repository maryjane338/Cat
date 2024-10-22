from PIL import Image
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(280, 300)

        img = Image.open("image/cat.jpg")
        red, green, blue = img.split()
        zeroed_band = red.point(lambda _: 0)
        red_merge = Image.merge('RGB', (red, zeroed_band, zeroed_band))
        red_merge.save('image/cat_red_merge.jpg')
        green_merge = Image.merge('RGB', (zeroed_band, green, zeroed_band))
        green_merge.save('image/cat_green_merge.jpg')
        blue_merge = Image.merge('RGB', (zeroed_band, zeroed_band, blue))
        blue_merge.save('image/cat_blue_merge.jpg')

        self.label = QLabel()
        self.label2 = QLabel('ЭЭЭЭЭЭЭЭЭ')
        btn_rotate_clockwise = QPushButton('Повернуть по часовой стрелке')
        btn_rotate_counter_clockwise = QPushButton('Повернуть против часовой стрелке')
        btn_red = QPushButton('R')
        btn_green = QPushButton('G')
        btn_blue = QPushButton('B')
        btn_all = QPushButton('ALL')
        self.slider = QSlider()
        self.slider.setMinimum(0)
        self.slider.setMaximum(20)
        self.slider.setValue(10)
        btn_rotate_clockwise.clicked.connect(self.rotate_clockwise)
        btn_rotate_counter_clockwise.clicked.connect(self.rotate_counter_clockwise)
        btn_red.clicked.connect(self.red_colored)
        btn_green.clicked.connect(self.green_colored)
        btn_blue.clicked.connect(self.blue_colored)
        btn_all.clicked.connect(self.all_colored)
        self.slider.valueChanged.connect(self.valuechange)

        self.transform = QTransform()
        self.rotate = 0
        self.transform.rotate(self.rotate)

        self.pixmap_empty = QPixmap()
        self.pixmap_empty.load("image/cat.jpg")
        data = img.getdata()
        new_data = []
        for i in data:
            new_data.append((i[0], i[1], i[2], int(i[3] * 0.5)))
        img.putdata(new_data)
        img.save("transparent_cat.jpg")
        self.pixmap_empty.load("transparent_cat.jpg")
        self.pixmap = self.pixmap_empty.scaled(500, 500)
        self.label.setPixmap(self.pixmap)

        self.main_l = QHBoxLayout()
        self.main_l.addWidget(self.label2)
        self.main_l.addWidget(self.label)
        self.main_l.addWidget(btn_red)
        self.main_l.addWidget(btn_green)
        self.main_l.addWidget(btn_blue)
        self.main_l.addWidget(btn_all)
        self.main_l.addWidget(self.slider)
        self.main_l.addWidget(btn_rotate_clockwise)
        self.main_l.addWidget(btn_rotate_counter_clockwise)
        self.setLayout(self.main_l)

    def valuechange(self):
        size = self.slider.value()
        self.label2.setFont(QFont('Arial', size))

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
        pixmap_red_scaled = pixmap_red.scaled(500, 500)
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
        pixmap_green_scaled = pixmap_green.scaled(500, 500)
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
        pixmap_blue_scaled = pixmap_blue.scaled(500, 500)
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
        pixmap_og_scaled = pixmap_og.scaled(500, 500)
        self.pixmap.swap(pixmap_og_scaled)
        self.label.setPixmap(self.pixmap)
        all_rotation = self.rotate
        if self.rotate == all_rotation:
            self.rotate = 0
            all_rotation = self.rotate
            self.transform.rotate(all_rotation)
        transformed_pixmap = self.pixmap.transformed(self.transform)
        self.label.setPixmap(transformed_pixmap)

def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()