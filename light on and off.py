import flet as ft
 
def main(page: ft.Page):
    luz = {"prendida":r"programing class\lightbulbon.jpg",
           "apagada": r"programing class\luz apagada.png"}
   
    def turn_on_off(e):
        if boton.value:
            imagenluz.src = luz["prendida"]
        else:
            imagenluz.src = luz["apagada"]
        if boton2.value:
            imagenluz2.src = luz["prendida"]
        else:
            imagenluz2.src = luz["apagada"]
        if boton3.value:
            imagenluz3.src = luz["prendida"]
        else:
            imagenluz3.src = luz["apagada"]
        page.update()
        imagenluz.update()
 
 
 
    boton= ft.Switch (label= "", value= False, on_change= turn_on_off)
    imagenluz = ft.Image(src=r"programing class\luz apagada.png", width= 300, height= 300 )
    boton2= ft.Switch (label= "", value= False, on_change= turn_on_off)
    imagenluz2 = ft.Image(src=r"programing class\luz apagada.png", width= 300, height= 300 )
    boton3= ft.Switch (label= "", value= False, on_change= turn_on_off)
    imagenluz3 = ft.Image(src=r"programing class\luz apagada.png", width= 300, height= 300 )
    lineal = ft.Row(controls=[imagenluz, imagenluz2, imagenluz3])
 
    page.add(lineal, boton, boton2, boton3)
 
ft.app(target = main)