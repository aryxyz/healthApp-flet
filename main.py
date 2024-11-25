
import flet as ft



from MyItems import *
from Calculates import  *



pageColor = "#f7f9f9"
mainColor = "#138d75"


txtWeight = ft.TextField(label="Weight",border_color=mainColor,color=mainColor,cursor_color=mainColor,label_style=ft.TextStyle(color=mainColor),border_width=3,input_filter=ft.NumbersOnlyInputFilter(),hint_text="Kg")
txtName = ft.TextField(label="Name",border_color=mainColor,color=mainColor,cursor_color=mainColor,label_style=ft.TextStyle(color=mainColor),border_width=3,input_filter=ft.TextOnlyInputFilter())
txtHeight =ft.TextField(label="Height",border_color=mainColor,color=mainColor,cursor_color=mainColor,label_style=ft.TextStyle(color=mainColor),border_width=3,input_filter=ft.NumbersOnlyInputFilter(),hint_text="Cm")
txtAge = ft.TextField(label="Age",border_color=mainColor,color=mainColor,cursor_color=mainColor,label_style=ft.TextStyle(color=mainColor),border_width=3,input_filter=ft.NumbersOnlyInputFilter())
rdiGender = ft.RadioGroup(content=ft.Row([
    ft.Radio(value="male",label="Male",label_style=ft.TextStyle(color=mainColor),fill_color=mainColor),
    ft.Radio(value="female",label="Female",label_style=ft.TextStyle(color=mainColor),fill_color=mainColor)
]))

def main(page: ft.Page):
    # page.client_storage.clear()
    waterState  =  showWater(page)
    # page.client_storage.remove("waterUsage")
    page.window_width = 360
    page.window_height = 800
    # page.window_max_width = 300
    # page.window_max_height = 800

    page.padding = ft.padding.all(0)



    def addWater(e):
        print("a")
        print(page.client_storage.get("waterUsage"))
        usage = page.client_storage.get("waterUsage")
        usage += 0.125
        page.client_storage.set("waterUsage",usage)
        waterState.pb.value = usage
        waterState.pb.update()


    def save_information():

        if txtName.value and txtWeight.value and txtHeight.value and txtAge.value and rdiGender.value:
            page.client_storage.set("weight",txtWeight.value)
            page.client_storage.set("height",txtHeight.value)
            page.client_storage.set("age",txtAge.value)
            page.client_storage.set("name",txtName.value)
            page.client_storage.set("gender",rdiGender.value)

            route_change(page.route)



    def navigation_handler(e):

        if navigation_bar.selected_index == 0:
            page.go("/BMIPage")
        elif navigation_bar.selected_index == 1:

            page.go("/BMRPage")
        elif navigation_bar.selected_index == 2:
            page.go("/waterPage")
        elif navigation_bar.selected_index == 3:
            page.go("/comingSoon")
        elif navigation_bar.selected_index == 4:
            page.go("/comingSoon")

        route_change(page.route)

    navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=mainColor,
        inactive_color= "#e8f8f5" ,
        active_color=pageColor,
        on_change=lambda e: navigation_handler(e),
        destinations=[
            ft.NavigationDestination(icon=ft.icons.MONITOR_WEIGHT, label="BMI"),
            ft.NavigationDestination(icon=ft.icons.MONITOR_HEART, label="BMR"),
            ft.NavigationDestination(icon=ft.icons.WATER_DROP, label="Water"),
            ft.NavigationDestination(icon=ft.icons.RUN_CIRCLE, label="Calorie"),
            ft.NavigationDestination(icon=ft.icons.LINE_WEIGHT, label="Best Weight"),

        ],
        selected_index= 0,
        height= page.height /12

    )

    # I know but I'm so tired


    def route_change(route):
        print(page.route)
        page.views.clear()
        if not page.client_storage.contains_key("name"):
            page.client_storage.set("firstTime","yes")
            page.views.append(
                ft.View(
                    route="/",
                    controls=[

                        ft.Container(
                            width=page.width,
                            height=page.height -30 ,
                            # bgcolor="red",


                            content=ft.Stack(
                                controls=[
                                    ft.Container(
                                        content=ft.Text(value="Get Started With SHealth", color=mainColor, size=40,
                                                        weight=ft.FontWeight.BOLD),
                                        alignment=ft.alignment.center,
                                        padding=ft.padding.all(20)

                                    ),

                                    ft.Container(
                                        content= ft.IconButton(icon=ft.icons.NAVIGATE_NEXT,bgcolor=mainColor,icon_color=pageColor,icon_size=50,on_click=lambda _:page.go("/formPage")),

                                        alignment= ft.alignment.bottom_right,
                                        right=20,
                                        bottom=0



                                    ),


                                ]
                            )
                        )

                    ]

                )
            )


        elif page.client_storage.get("firstTime") == "yes":

            page.go("/BMIPage")
            page.client_storage.set("firstTime","no")











        if page.route =="/formPage":
            page.views.append(
                ft.View(
                    route="/",
                    controls=[

                        ft.Container(
                            width=page.width,
                            height=page.height - 30,
                            # bgcolor="red",

                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        content=ft.Text(value="Write Your Information", color=mainColor, size=40,
                                                        weight=ft.FontWeight.BOLD),
                                        alignment=ft.alignment.top_center,
                                        padding=ft.padding.all(20),
                                        height= page.height /5,


                                    ),

                                    ft.Container(
                                        content=ft.Column([
                                            ft.Container(
                                                content=txtName,


                                            ),
                                            ft.Container(
                                                content=txtWeight,
                                                margin= ft.margin.only(0, 30,0,0)

                                            ),
                                            ft.Container(
                                                content=txtHeight,
                                                margin= ft.margin.only(0, 30,0,0)

                                            ),
                                            ft.Container(
                                                content=txtAge,
                                                margin= ft.margin.only(0, 30,0,0)

                                            ),
                                            ft.Container(
                                                content=rdiGender,
                                                margin= ft.margin.only(0, 30,0,0)

                                            ),



                                        ],alignment=ft.alignment.center),


                                        alignment=ft.alignment.top_center,
                                        padding=ft.padding.all(20)

                                    ),

                                    ft.Container(
                                        content=ft.IconButton(icon=ft.icons.NAVIGATE_NEXT, bgcolor=mainColor,
                                                              icon_color=pageColor, icon_size=50,
                                                              on_click=lambda _:save_information()),

                                        alignment=ft.alignment.bottom_right,
                                        margin= ft.margin.only(0,page.width/6,20,0)
                                        # right=20,
                                        # bottom=0

                                    ),

                                ]
                            )
                        )

                    ]

                )
            )




        if page.route == "/BMIPage":
            print("BMR selected")
            page.views.append(
                ft.View(
                    route="/BMIPage",
                    controls=[
                        ft.Container(
                            content=ft.Column([
                                TextHeader("Your BMI"),
                            ]),alignment= ft.alignment.center,
                            height= page.height / 4,
                            margin = ft.margin.only(0,100,0,0),

                        ),

                        ft.Container(
                            content=ft.Column([
                                BMIShow(calculateBMI(page.client_storage.get("weight"),page.client_storage.get("height")))
                            ]), alignment=ft.alignment.center,

                            margin=ft.margin.only(0, 30, 0, 0),

                        )
                    ]
                )
            )


        if page.route == "/BMRPage":
            page.views.append(
                ft.View(
                    route="/BMRPage",
                    controls=[
                        ft.Container(
                            content=ft.Column([
                                TextHeader("Your BMR"),
                            ]),alignment= ft.alignment.center,
                            height= page.height / 4,
                            margin = ft.margin.only(0,100,0,0),

                        ),

                        ft.Container(
                            content=ft.Column([
                                TextHeader(text=calculateBMR(weight=page.client_storage.get("weight"),height=page.client_storage.get("height"),age=page.client_storage.get("age"),gender=page.client_storage.get("gender")))
                            ]), alignment=ft.alignment.center,

                            margin=ft.margin.only(0, 30, 0, 0),

                        ) ,ft.Container(
                            content=ft.Column([
                                TextHeader(text="Calories")
                            ]), alignment=ft.alignment.center,

                            margin=ft.margin.only(0, 30, 0, 0),

                        )
                    ]
                )
            )
        if page.route == "/waterPage":
            page.views.append(
                ft.View(
                    route="/waterPage",
                    controls=[
                        ft.Container(
                            content=ft.Column([
                                TextHeader("Water Usage"),
                            ]),alignment= ft.alignment.center,
                            height= page.height / 4,
                            margin = ft.margin.only(0,100,0,0),

                        ),

                        ft.Container(
                            content=ft.Column([
                                waterState,


                            ]), alignment=ft.alignment.center,

                            margin=ft.margin.only(0, 30, 0, 0),

                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.CupertinoButton(text="I Drink another glass",bgcolor="#3498db",color=pageColor,on_click=addWater,)


                            ]), alignment=ft.alignment.center,

                            margin=ft.margin.only(0, 30, 0, 0),

                        )
                    ]
                )
            )
        if page.route == "/comingSoon":
            page.views.append(
                ft.View(
                    route="/comingSoon",
                    controls=[
                        ft.Container(
                            content=ft.Column([
                                TextHeader("Buy Premium",font_size=30),
                            ]),alignment= ft.alignment.center,
                            height= page.height / 4,
                            margin = ft.margin.only(0,100,0,0),

                        ),




                    ]
                )
            )

        if not page.route=="/" and  not page.route == "/formPage":

            page.views[-1].navigation_bar = navigation_bar

        page.views[-1].padding = ft.padding.all(0)
        page.views[-1].bgcolor = pageColor

        page.client_storage.set("lastPage",page.route)

        page.update()



    def pop_view(view):
        page.views.pop()
        top_page = page.views[-1]
        page.go(top_page.route)


    page.on_view_pop = pop_view

    page.on_route_change = route_change


    if not page.client_storage.contains_key("lastPage"):
        page.client_storage.set("lastPage","/")


    page.go(page.client_storage.get("lastPage"))




ft.app(main)
