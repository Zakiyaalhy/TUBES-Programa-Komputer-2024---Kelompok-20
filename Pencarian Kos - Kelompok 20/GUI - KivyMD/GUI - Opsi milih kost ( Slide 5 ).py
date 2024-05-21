from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDLabel:
        text: "PILIH RANGE HARGA KOS"
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
                text: "Under 5 Juta/Bulan"
                halign: "center"

        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "250dp", "50dp"
            radius: [15, 15, 15, 15]
            elevation: 8
            MDLabel:
                text: "5-10 Juta/Bulan"
                halign: "center"

        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "250dp", "50dp"
            radius: [15, 15, 15, 15]
            elevation: 8
            MDLabel:
                text: "Lebih dari 10 Juta/Bulan"
                halign: "center"

'''

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"
        return Builder.load_string(KV)

Example().run()
