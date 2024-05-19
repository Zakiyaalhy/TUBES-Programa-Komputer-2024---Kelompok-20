
from kivy.lang import Builder

from kivymd.app import MDApp


KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

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
        padding: "36dp", 0, "36dp" , "36dp"
        size_hint: .8, .5
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .4}
        spacing: dp(10)   

        #USERNAME
        MDTextField:
            mode: "outlined"

            MDTextFieldHintText:
                text: "Masukkan Username"
            
            MDTextFieldHelperText:
                mode: "persistent"

        #PASSWORD
        MDTextField:
            mode: "outlined"

            MDTextFieldHintText:
                text: "Masukkan Password"
            
            MDTextFieldHelperText:
                mode: "persistent"
        
        MDButton:
            style: "elevated"
            pos_hint: {"x": .4, "y": .5}  # Left button at x=0, y=0.5 (center vertically)
          
            MDButtonText:
                text: "Sign Up"

        MDButton:
            style: "elevated"
            pos_hint: {"x": .4, "y": .5}  # Middle button at x=0.5, y=1 (top center)

            MDButtonText:
                text: "Sign In"
'''
       


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"  # "Purple", "Red"
        return Builder.load_string(KV)


Example().run()


#########################################################################

KV2 = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

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
        padding: "36dp", 0, "36dp" , "36dp"
        size_hint: .8, .5
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .4}
        spacing: dp(10)   

        #USERNAME
        MDTextField:
            mode: "outlined"

            MDTextFieldHintText:
                text: "Masukkan Username"
            
            MDTextFieldHelperText:
                mode: "persistent"

        #PASSWORD
        MDTextField:
            mode: "outlined"

            MDTextFieldHintText:
                text: "Masukkan Password"
            
            MDTextFieldHelperText:
                mode: "persistent"
        
        MDButton:
            style: "elevated"
            pos_hint: {"x": .4, "y": .5}  # Left button at x=0, y=0.5 (center vertically)
          
            MDButtonText:
                text: "Sign Up"

        # MDButton:
        #     style: "elevated"
        #     pos_hint: {"x": .4, "y": .5}  # Middle button at x=0.5, y=1 (top center)

        #     MDButtonText:
        #         text: "Sign In"
'''
       


class Example2(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"  # "Purple", "Red"
        return Builder.load_string(KV2)


Example2().run()