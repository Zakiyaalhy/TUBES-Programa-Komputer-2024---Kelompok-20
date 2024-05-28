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
MDScreenManager:

    # SIGN IN PAGE
    MDScreen:
        name: "sign_in"
        md_bg_color: "lightblue"

        MDLabel:
            text: "WELCOME!"
            halign: "center"
            valign: "center"
            bold: True
            font_style: "Display"
            pos_hint: {"center_x": .5, "center_y": 0.7}
            # pos_hint: {"center_x": -.5, "center_y": -.5}

        #TEMPAT BUTTON DAN TEKS INPUT
        MDCard:
            orientation: "vertical"
            padding: "36dp", "36dp", "36dp" , "80dp"
            size_hint: .8, .4
            style: "elevated"
            pos_hint: {"center_x": .5, "center_y": .4}
            spacing: dp(10)   

            #USERNAME
            MDTextField:
                id  : username_IN
                mode: "outlined"

                MDTextFieldHintText:
                    text: "Username"
                
                MDTextFieldHelperText:
                    mode: "persistent"

            #PASSWORD
            MDTextField:
                id  : password_IN
                mode: "outlined"
                password: True

                MDTextFieldHintText:
                    text: "Password"
                
                MDTextFieldHelperText:
                    mode: "persistent"

        MDButton:
            pos_hint: {"center_x": .5, "center_y": .14}
            y: "36dp"
            on_release: 
                app.sign_in()
                root.current = "opsi_jenis"

            MDButtonText:
                text: "Sign In"   

        MDButton:
            pos_hint: {"center_x": .5, "center_y": .05}
            y: "36dp"
            on_release:
                root.current = "sign_up"

            MDButtonText:
                text: "Belum punya akun?, Sign Up!"      
   

    # SIGN UP PAGE
    MDScreen:
        name: "sign_up"
        md_bg_color: "pink"

        MDLabel:
            text: "WELCOME!"
            halign: "center"
            valign: "center"
            bold: True
            font_style: "Display"
            pos_hint: {"center_x": .5, "center_y": 0.7}
            # pos_hint: {"center_x": -.5, "center_y": -.5}

        #TEMPAT BUTTON DAN TEKS INPUT
        MDCard:
            orientation: "vertical"
            padding: "36dp", "36dp", "36dp" , "80dp"
            size_hint: .8, .45
            style: "elevated"
            pos_hint: {"center_x": .5, "center_y": .4}
            spacing: dp(10)   

            #USERNAME
            MDTextField:
                id  : username_UP
                mode: "outlined"

                MDTextFieldHintText:
                    text: "Username"
                
                MDTextFieldHelperText:
                    mode: "persistent"

            #PASSWORD
            MDTextField:
                id  : password_UP
                mode: "outlined"
                password: True

                MDTextFieldHintText:
                    text: "Password"
                
                MDTextFieldHelperText:
                    mode: "persistent"

        MDButton:
            pos_hint: {"center_x": .5}
            y: "36dp"
            on_release:
                root.current = "sign_in"
                app.sign_up()

            MDButtonText:
                text: "Sign Up"   


    # OPSI_JENIS
    MDScreen:
        name: "opsi_jenis"
        md_bg_color: "pink"

        MDLabel:
            text: "Pilih Jenis Kosanmu!"
            halign: "center"
            valign: "center"
            bold: True
            font_style: "Display"
            pos_hint: {"center_x": .5, "center_y": 0.5}


        #TEMPAT BUTTON  
        GridLayout:
            cols: 2
            rows: 1
            spacing: "50dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            size_hint: None, None
            # width: self.minimum_width
            # height: self.minimum_height

            MDButton:
                on_release:
                    root.current = "opsi_harga_putra"
                style: "elevated"
                pos_hint: {"x": .4, "y": .5} 
                MDButtonText:
                    text: "Kos Putra"
                
            MDButton:
                on_release:
                    root.current = "opsi_harga_putri"
                style: "elevated"
                pos_hint: {"x": .4, "y": .5} 
                MDButtonText:
                    text: "Kos Putri"  


    # OPSI_HARGA_PUTRI
    MDScreen:
        name: "opsi_harga_putri"
        md_bg_color: "orange"

        MDLabel:
            text: "Pilih Range Harga Kosanmu!"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_style: "Display"
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
                id: putri_under
                on_release:
                    root.current = "putri_under"

                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8
                MDLabel:
                    text: "Under 5 Juta/Tahun"
                    halign: "center"

            MDCard:
                id: putri_middle
                on_release:
                    root.current = "putri_middle"

                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8
                MDLabel:
                    text: "5-10 Juta/Tahun"
                    halign: "center"

            MDCard:
                id: putri_upper
                on_release:
                    root.current = "putri_upper"

                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8
                MDLabel:
                    text: "Above 10 Juta/Tahun"
                    halign: "center"


    # OPSI_UNDER_PUTRI
    MDScreen:
        name: "putri_under"
        md_bg_color:"olive"

        MDLabel:
            text: "KOST PUTRI"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_style: "Display"
            bold: True

        MDLabel:
            text: "Daftar Kost dengan Harga Under 5 Juta/Tahun"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            role: "large"
            bold: True

        GridLayout:
            cols: 2
            rows: 2
            padding: "20dp"
            spacing: "80dp", "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            size_hint: None, None
            width: self.minimum_width
            height: self.minimum_height

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                FitImage:
                    source: "gambar\P_1.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8
            
                FitImage:
                    source: "gambar\P_2.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Wisma Sri"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True

                
            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Kost Putri Barokah"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True


    # OPSI_MIDDLE_PUTRI
    MDScreen:
        name: "putri_middle"
        md_bg_color:"purple"

        MDLabel:
            text: "KOST PUTRI"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_style: "Display"
            bold: True

        MDLabel:
            text: "Daftar Kost dengan Harga 5 - 10 Juta/Tahun"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            role: "large"
            bold: True

        GridLayout:
            cols: 2
            rows: 2
            padding: "20dp"
            spacing: "80dp", "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            size_hint: None, None
            width: self.minimum_width
            height: self.minimum_height

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                FitImage:
                    source: "gambar\P_3.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8
            
                FitImage:
                    source: "gambar\P_4.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Kost Putri Aisha"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True

                
            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Kost Bu Erna"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True


    # OPSI_UPPER_PUTRI
    MDScreen:
        name: "putri_upper"
        md_bg_color:"purple"

        MDLabel:
            text: "KOST PUTRI"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_style: "Display"
            bold: True

        MDLabel:
            text: "Daftar Kost dengan Harga Above 10 Juta/Tahun"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            role: "large"
            bold: True

        GridLayout:
            cols: 2
            rows: 2
            padding: "20dp"
            spacing: "80dp", "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            size_hint: None, None
            width: self.minimum_width
            height: self.minimum_height

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                FitImage:
                    source: "gambar\P_5.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8
            
                FitImage:
                    source: "gambar\P_6.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Kost Gang Amarta 2"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True

                
            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Wisma Putri Sri Rejeki"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True


    # OPSI_HARGA_PUTRA
    MDScreen:
        name: "opsi_harga_putra"
        md_bg_color: "orange"

        MDLabel:
            text: "Pilih Range Harga Kosanmu!"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_style: "Display"
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
                on_release:
                    root.current = "putra_under"

                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8
                MDLabel:
                    text: "Under 5 Juta/Tahun"
                    halign: "center"

            MDCard:
                on_release:
                    root.current = "putra_middle"

                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8
                MDLabel:
                    text: "5-10 Juta/Tahun"
                    halign: "center"

            MDCard:
                on_release:
                    root.current = "putra_upper"

                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8
                MDLabel:
                    text: "Above 10 Juta/Tahun"
                    halign: "center"

    # OPSI_UNDER_PUTRA
    MDScreen:
        name: "putra_under"
        md_bg_color:"olive"

        MDLabel:
            text: "KOST PUTRA"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_style: "Display"
            bold: True

        MDLabel:
            text: "Daftar Kost dengan Harga Under 5 Juta/Tahun"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            role: "large"
            bold: True

        GridLayout:
            cols: 2
            rows: 2
            padding: "20dp"
            spacing: "80dp", "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            size_hint: None, None
            width: self.minimum_width
            height: self.minimum_height

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                FitImage:
                    source: "gambar\L_1.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8
            
                FitImage:
                    source: "gambar\L_2.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Kost Superboyo"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True

                
            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Kost Pak Sulis"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True


    # OPSI_MIDDLE_PUTRA
    MDScreen:
        name: "putra_middle"
        md_bg_color:"purple"

        MDLabel:
            text: "KOST PUTRA"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_style: "Display"
            bold: True

        MDLabel:
            text: "Daftar Kost dengan Harga 5 - 10 Juta/Tahun"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            role: "large"
            bold: True

        GridLayout:
            cols: 2
            rows: 2
            padding: "20dp"
            spacing: "80dp", "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            size_hint: None, None
            width: self.minimum_width
            height: self.minimum_height

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                FitImage:
                    source: "gambar\L_3.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8
            
                FitImage:
                    source: "gambar\L_4.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Kost Pandawa"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True

                
            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Griya Berkah"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True


    # OPSI_UPPER_PUTRA
    MDScreen:
        name: "putra_upper"
        md_bg_color:"purple"

        MDLabel:
            text: "KOST PUTRA"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_style: "Display"
            bold: True

        MDLabel:
            text: "Daftar Kost dengan Harga Above 10 Juta/Tahun"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            role: "large"
            bold: True

        GridLayout:
            cols: 2
            rows: 2
            padding: "20dp"
            spacing: "80dp", "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            size_hint: None, None
            width: self.minimum_width
            height: self.minimum_height

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                FitImage:
                    source: "gambar\L_5.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "250dp"
                radius: [15, 15, 15, 15]
                elevation: 8
            
                FitImage:
                    source: "gambar\L_6.jpg"
                    radius: [15, 15, 15, 15]

            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Kost Putra SN"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True

                
            MDCard:
                style: "elevated"
                orientation: "vertical"
                size_hint: None, None
                size: "250dp", "50dp"
                radius: [15, 15, 15, 15]
                elevation: 8

                MDLabel:
                    text: "Omah Ngaji Al Anshori"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": 0.65}
                    bold: True

'''



class KosanKu(MDApp):
    dialog  = None
    dialog2 = None
    dialog3 = None

    def build(self):
        return Builder.load_string(homepage)

    def notif_1(self):
        if not self.dialog:
            self.dialog = MDDialog(
                MDDialogHeadlineText(
                    text="Selamat Datang {}!".format(self.root.ids.username_IN.text),
                    ),
            )
        self.dialog.open()

    def notif_2(self):
        if not self.dialog2:
            self.dialog2 = MDDialog(
                MDDialogHeadlineText(
                    text="Akun Belum Terdaftar",
                    ),
            )
        self.dialog2.open()

    def notif_3(self):
        if not self.dialog3:
            self.dialog3 = MDDialog(
                MDDialogHeadlineText(
                    text="Akun Terbuat!",
                    ),
            )
        self.dialog3.open()

    def sign_in(self):
        # Membaca file CSV dengan Pandas
        def baca_csv(file_path):
            data = pd.read_csv(file_path)
            return data

        # Memeriksa username dan password
        def periksa_login(username, password, data):
            if username in data['username'].values and password in data['password'].values:
                return True
            return False

        # Menjalankan program
        file_path = 'datauser.csv' 
        data = baca_csv(file_path)

        username = self.root.ids.username_IN.text
        password = self.root.ids.password_IN.text

        if periksa_login(username, password, data):
            self.notif_1()
        else:
            self.notif_2()
    
    def sign_up(self):
        username = self.root.ids.username_UP.text
        password = self.root.ids.password_UP.text

        # Membuka file CSV
        with open('datauser.csv', 'a') as file:
            # Membuat objek penulis CSV
            writer = csv.writer(file)

            # Menulis username dan password ke file CSV
            writer.writerow([username, password])
            self.notif_3()

    # def kos_putri():

    # def kos_putra():

KosanKu().run()


