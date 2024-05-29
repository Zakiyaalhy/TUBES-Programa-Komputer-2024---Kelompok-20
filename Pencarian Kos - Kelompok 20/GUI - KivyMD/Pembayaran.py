
from kivy.lang import Builder

from kivymd.app import MDApp
import csv
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
import pandas as pd
from kivymd.uix.dialog import (
MDDialog,
MDDialogIcon,
MDDialogHeadlineText,
MDDialogSupportingText,
MDDialogButtonContainer,
MDDialogContentContainer,
)



homepage = '''

# OPSI_UNDER_PUTRI
MDScreen:
    name: "opsi_bayar"
    md_bg_color:"white"

    # FitImage:
    #     source: "gambar\BG_SU_1.png"

    MDLabel:
        text: "Pilih Metode Pembayaran!"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        role: "large"
        bold: True

    MDButton:
        pos_hint: {"center_x": .5, "center_y": .65}
        y: "36dp"

        MDButtonText:
            text: "BANK MANDIRI" 
            theme_font_name: "Custom"
          #  font_name: "Font/HammersmithOne-Regular.ttf"
            theme_text_color: "Custom"
            text_color: "#3B3939"  

    MDButton:
        pos_hint: {"center_x": .5, "center_y": .55}
        y: "36dp"

        MDButtonText:
            text: "BANK BRI" 
            theme_font_name: "Custom"
          #  font_name: "Font/HammersmithOne-Regular.ttf"
            theme_text_color: "Custom"
            text_color: "#3B3939"  
    MDButton:
        pos_hint: {"center_x": .5, "center_y": .45}
        y: "36dp"

        MDButtonText:
            text: "BANK BCA" 
            theme_font_name: "Custom"
          #  font_name: "Font/HammersmithOne-Regular.ttf"
            theme_text_color: "Custom"
            text_color: "#3B3939"  

    MDButton:
        pos_hint: {"center_x": .5, "center_y": .35}
        y: "36dp"

        MDButtonText:
            text: "OVO" 
            theme_font_name: "Custom"
          #  font_name: "Font/HammersmithOne-Regular.ttf"
            theme_text_color: "Custom"
            text_color: "#3B3939"  

'''

class KosanKu(MDApp):
    def build(self):
        return Builder.load_string(homepage)

   
       
KosanKu().run()


