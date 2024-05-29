from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import (
MDDialog,
MDDialogIcon,
MDDialogHeadlineText,
MDDialogSupportingText,
MDDialogButtonContainer,
MDDialogContentContainer,
)

from kivymd.uix.screen import MDScreen
import csv
import pandas as pd


nyoba = '''
# PUTRI_UNDER_1
MDScreen:
    name: "putri_under_1"
    FitImage:
        source: "halaman login (2).png"
        
    MDCard:
        style: "elevated"
        orientation: "vertical"
        pos_hint: {"center_x": 0.3, "center_y": 0.47}
        size_hint: None, None
        size: "400dp", "400dp"
        radius: [15, 15, 15, 15]
        elevation: 8

        FitImage:
            source: "L_1.jpg"
            radius: [15, 15, 15, 15]

    MDCard:
        style: "elevated"
        orientation: "vertical"
        pos_hint: {"center_x": 0.66, "center_y": 0.675}
        size_hint: None, None
        size: "500dp", "70dp"
        radius: [15, 15, 15, 15]
        elevation: 8

        MDLabel:
            text: "Nama Kos"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            bold: True

    MDCard:
        style: "elevated"
        orientation: "vertical"
        pos_hint: {"center_x": 0.66, "center_y": 0.4685}
        size_hint: None, None
        size: "500dp", "230dp"
        radius: [15, 15, 15, 15]
        elevation: 8
        

        MDLabel:
            text: "Detail Kos"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            bold: True

        
    MDCard:
        style: "elevated"
        orientation: "vertical"
        pos_hint: {"center_x": 0.66, "center_y": 0.262}
        size_hint: None, None
        size: "500dp", "70dp"
        radius: [15, 15, 15, 15]
        elevation: 8

    FloatLayout:
        MDTextField:
            id  : jumlah
            mode: "outlined"
            pos_hint: {"center_x": 0.66, "center_y": 0.26}
            bold: True
            size_hint: None, None
            size: "490dp", "0dp"
            radius: [15, 15, 15, 15]

            MDTextFieldHintText:
                text: "Jumlah Kamar"

            MDTextFieldHelperText:
                mode: "persistent"            
'''

class Homepage(MDApp):
    def build(self) :
        return Builder.load_string(nyoba)
Homepage().run()


    


