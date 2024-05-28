from kivy.lang import Builder
from kivymd.app import MDApp

homepage= '''
MDScreen:
    md_bg_color: "blue"

    MDLabel:
        text: "Pilih Range Harga Kosanmu!"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        font_style: "Display"
        bold: True

    MDLabel:
        text: "Pilih Daftar Harga"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.70}
        role: "large"
        bold: True

    GridLayout:
        cols: 1
        rows: 3
        padding: "20dp"
        spacing: "20dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        size_hint: None, None
        width: self.minimum_width
        height: self.minimum_height

        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "250dp", "50dp"
            radius: [15, 15, 15, 15]
            elevation: 8
            MDLabel:
                text: "Under 5 Juta/Tahun"
                halign: "center"

        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "250dp", "50dp"
            radius: [15, 15, 15, 15]
            elevation: 8
            MDLabel:
                text: "5 - 10 Juta/Tahun"
                halign: "center"

        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "250dp", "50dp"
            radius: [15, 15, 15, 15]
            elevation: 8
            MDLabel:
                text: "Above 10 Juta/Tahun"
                halign: "center"

'''

class Harga(MDApp):
    def build(self):
        return Builder.load_string(homepage)

Harga().run()
