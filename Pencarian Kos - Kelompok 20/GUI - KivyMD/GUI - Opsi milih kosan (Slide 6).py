from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDLabel:
        text: "KOST PUTRA"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        font_style: "Display"
        bold: True

    MDLabel:
        text: "Daftar Kost dengan Harga Under 5 Juta Per Bulan"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        role: "large"
        bold: True

    GridLayout:
        cols: 3
        rows: 2
        padding: "20dp"
        spacing: "20dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        size_hint: None, None
        width: self.minimum_width
        height: self.minimum_height

        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "150dp", "100dp"
            radius: [15, 15, 15, 15]
            elevation: 8
            MDLabel:
                text: "Nama Kost 1"
                halign: "center"

        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "150dp", "100dp"
            radius: [15, 15, 15, 15]
            elevation: 8
            MDLabel:
                text: "Nama Kost 2"
                halign: "center"

        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "150dp", "100dp"
            radius: [15, 15, 15, 15]
            elevation: 8
            MDLabel:
                text: "Nama Kost 3"
                halign: "center"

        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "150dp", "100dp"
            radius: [15, 15, 15, 15]
            elevation: 8
            MDLabel:
                text: "Nama Kost 4"
                halign: "center"

        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "150dp", "100dp"
            radius: [15, 15, 15, 15]
            elevation: 8
            MDLabel:
                text: "Nama Kost 5"
                halign: "center"

        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "150dp", "100dp"
            radius: [15, 15, 15, 15]
            elevation: 8
            MDLabel:
                text: "Nama Kost 6"
                halign: "center"
'''

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"
        return Builder.load_string(KV)

Example().run()
