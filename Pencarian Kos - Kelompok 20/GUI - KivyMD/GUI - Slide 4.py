from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    
    MDLabel:
        text: "PILIH JENIS KOS"
        halign: "center"
        pos_hint: {"center_x": .5, "center_y": 0.65}
        font_style: "Display"
        bold: True

    GridLayout:
        cols: 2
        rows: 1
        spacing: "50dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        size_hint: None, None
        width: self.minimum_width
        height: self.minimum_height

        MDButton:
            style: "elevated"
            pos_hint: {"x": .4, "y": .5} 
            MDButtonText:
                text: "Kos Putra"
            
        MDButton:
            style: "elevated"
            pos_hint: {"x": .4, "y": .5} 
            MDButtonText:
                text: "Kos Putri"     
'''

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"
        return Builder.load_string(KV)

Example().run()
