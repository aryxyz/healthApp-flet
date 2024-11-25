import flet as ft
from anyio.abc import value
from certifi import contents

mainColor = "#138d75"

pageColor = "#f7f9f9"
class TextHeader(ft.Container):
    def __init__(self,text = "test",font_size = 50,bg = mainColor,):
        super().__init__()

        self.content = ft.Text(value=text,color=pageColor,size=font_size,weight=ft.FontWeight.BOLD)
        self.bgcolor = bg
        self.padding = ft.padding.all(20)
        self.border_radius = ft.border_radius.all(5)



class BMIShow(ft.Column):
    def __init__(self, BMI):
        super().__init__()
        self.showColor = mainColor
        self.showText = ""
        self.alignment = ft.alignment.center
        if BMI >=30:
            self.showColor = " #ec7063 "
            self.showText = "Obese"
        elif BMI >=25:
            self.showColor = " #f4d03f "
            self.showText = "Overweight"
        elif BMI >=18.5:
            self.showColor = mainColor
            self.showText = "Normal weight"
        elif BMI <18.5:
            self.showColor = "#5dade2"
            self.showText = "Underweight"

        self.controls = [
            ft.Container(
                content=ft.Text(value=self.showText,size=40,color=self.showColor,weight=ft.FontWeight.BOLD),
                alignment=ft.alignment.center

            ) ,
            ft.Container(
                content=ft.Text(value=BMI,size=30,color=self.showColor,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                alignment=ft.alignment.center
            )


        ]


class showWater(ft.Container):
    def __init__(self,page):
        super().__init__()
        self.page = page
        if not self.page.client_storage.contains_key("waterUsage"):
            self.page.client_storage.set("waterUsage",0.0)

        self.pb = ft.ProgressBar(width=self.page.width / 4,height=50,color="#3498db",bgcolor="#ecf0f1")

        self.content = ft.Column([
            self.pb,


        ])
        self.alignment = ft.alignment.center
        self.pb.value = self.page.client_storage.get("waterUsage")



    # def addWater(self):
    #    usage = self.page.client_storage.get("waterUsage")
    #    usage += 0.125
    #    self.page.client_storage.set("waterUsage",usage)
    #    self.pb.value = usage






