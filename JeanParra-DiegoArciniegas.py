import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk




def IA():
    opction1=0
    opction2=0
    opction3=0
    opction4=0
    opction5=0
    opction6=0
    if AMHJ.get()==1 or HJM.get()==1 or DCTN.get()==1 or CHJ.get()==1:
        if AMHJ.get()==1:
            opction1+=1
        if HJM.get()==1:
            opction1+=1
        if DCTN.get()==1:
            opction1+=1  
        if CHJ.get()==1:
            opction1+=1 
    if MCM.get()==1 or CPH.get()==1:
        if MCM.get()==1:
            opction2+=1 
        if CPH.get()==1:
            opction2+=1 
    if DPE.get()==1 or CCE.get()==1 or BLM.get()==1:
        if DPE.get()==1:
            opction3+=1 
        if CCE.get()==1:
            opction3+=1 
        if BLM.get()==1:
            opction3+=1
    if DG.get()==1 or PV.get()==1 or ECP.get()==1:
        if DG.get()==1:
            opction4+=1
        if PV.get()==1:
            opction4+=1
        if ECP.get()==1:
            opction4+=1
    if RDHR.get()==1 or PCA.get()==1 or SCMH.get()==1:
        if RDHR.get()==1:
            opction5+=1
        if PCA.get()==1:
            opction5+=1
        if SCMH.get()==1:
            opction5+=1
    if P39.get()==1 or AHA.get()==1 or MBFE.get()==1:
        if P39.get()==1:
            opction6+=1
        if AHA.get()==1:
            opction6+=1
        if MBFE.get()==1:
            opction6+=1
    if(opction1 > opction2 and opction1 > opction3 and opction1 > opction4 and opction1 > opction5 and opction1 > opction6):
        graficar1()
        datos()
    elif(opction2 > opction1 and opction2 > opction3 and opction2 > opction4 and opction2 > opction5 and opction2 > opction6):
        graficar2()
        datos()
    elif(opction3 > opction1 and opction3 > opction2 and opction3 > opction4 and opction3 > opction5 and opction3 > opction6):
        graficar3()
        datos()
    elif(opction4 > opction1 and opction4 > opction2 and opction4 > opction3 and opction4 > opction5 and opction4 > opction6):
        graficar4()
        datos()
    elif(opction5 > opction1 and opction5 > opction2 and opction5 > opction3 and opction5 > opction4 and opction5 > opction6):
        graficar5()
        datos()
    elif(opction6 > opction1 and opction6 > opction2 and opction6 > opction3 and opction6 > opction4 and opction6 > opction5):
        graficar6()
        datos()
  
def datos():
    tk.Label(root, text="1").place(x=570, y=15)
    tk.Label(root, text="2").place(x=570, y=48)
    tk.Label(root, text="3").place(x=570, y=81)
    tk.Label(root, text="4").place(x=570, y=114)
    tk.Label(root, text="5").place(x=570, y=147)
    tk.Label(root, text="6").place(x=570, y=180)
    tk.Label(root, text="7").place(x=570, y=213)
    tk.Label(root, text="8").place(x=570, y=246)
    tk.Label(root, text="9").place(x=570, y=279)
    tk.Label(root, text="10").place(x=565, y=312)
    tk.Label(root, text="11").place(x=565, y=345)
    tk.Label(root, text="12").place(x=565, y=378)
    tk.Label(root, text="13").place(x=565, y=411)
    tk.Label(root, text="14").place(x=565, y=444)
    tk.Label(root, text="15").place(x=565, y=477)
    tk.Label(root, text="16").place(x=565, y=510)
    tk.Label(root, text="17").place(x=565, y=543)
    tk.Label(root, text="18").place(x=565, y=576)
    
def graficar1():       
    canvas = Canvas(width=500, height=650)
    canvas.pack()
    #Grafica 1
    canvas.create_oval(10, 10, 40, 40,fill='yellow')
    canvas.create_oval(10, 43, 40, 73,fill='yellow')
    canvas.create_oval(10, 76, 40, 106,fill='yellow')
    canvas.create_oval(10, 109, 40, 139,fill='yellow')
    canvas.create_oval(100, 25, 130, 55,fill='blue')
    canvas.create_oval(100, 91, 130,121,fill='blue')
    canvas.create_oval(190, 58, 220,88,fill='red')
    #Grafica 2
    canvas.create_oval(10, 142, 40, 172)
    canvas.create_oval(10, 175, 40, 205)
    canvas.create_oval(100, 157, 130,187)
    canvas.create_oval(190, 157, 220,187)
    #Grafica 3
    canvas.create_oval(10, 208, 40, 238)
    canvas.create_oval(10, 241, 40, 271)
    canvas.create_oval(10, 274, 40, 304)
    canvas.create_oval(100, 223, 130, 253)
    canvas.create_oval(190, 238, 220, 268)
    #Grafica 4
    canvas.create_oval(10, 307, 40, 337)
    canvas.create_oval(10, 340, 40, 370)
    canvas.create_oval(10, 373, 40, 403)
    canvas.create_oval(100, 322, 130, 352)
    canvas.create_oval(190, 337, 220, 367)
    #Grafica 5
    canvas.create_oval(10, 406, 40, 436)
    canvas.create_oval(10, 439, 40, 469)
    canvas.create_oval(10, 472, 40, 502)
    canvas.create_oval(100, 421, 130, 451)
    canvas.create_oval(190, 436, 220, 466)
    #Grafica 6
    canvas.create_oval(10, 505, 40, 535)
    canvas.create_oval(10, 538, 40, 568)
    canvas.create_oval(10, 571, 40, 601)
    canvas.create_oval(100, 520, 130, 550)
    canvas.create_oval(190, 535, 220,565 )
    tk.Label(root, text="Pudrición del cogollo",font=("Arial", 25) ).place(x=950, y=10)
    tk.Label(root, text="Es una de las enfermedades más serias y devastadoras, con episodios severos en Brasil,").place(x=870, y=90)
    tk.Label(root, text="Colombia, Ecuador, Panamá, Surinam, Costa Rica, Nicaragua, Honduras, Perú y Venezuela.").place(x=870, y=110)
    tk.Label(root, text="Esta enfermedad comienza en los tejidos inmaduros de las flechas, pero se expande con ").place(x=870, y=150)
    tk.Label(root, text="rapidez afectando los nuevos tejidos.").place(x=870, y=170)
    tk.Label(root, text="Tratamiento: Lo más importante es una detección temprana para poder remover el tejido").place(x=870, y=210)
    tk.Label(root, text="afectado y protejer el tejido sano con insecticidas, fungicidad y bactericidas.").place(x=870, y=230)
    tk.Label(root, text="Es recomendable realizar un programa de aspersión para eliminar los estados avanzados").place(x=870, y=270)
    tk.Label(root, text="de la enfermedad y remover lotes afectados.").place(x=870, y=290)

    
def graficar2():
    canvas = Canvas(width=500, height=650)
    canvas.pack()
    #Grafica 1
    canvas.create_oval(10, 10, 40, 40)
    canvas.create_oval(10, 43, 40, 73)
    canvas.create_oval(10, 76, 40, 106)
    canvas.create_oval(10, 109, 40, 139)
    canvas.create_oval(100, 25, 130, 55)
    canvas.create_oval(100, 91, 130,121)
    canvas.create_oval(190, 58, 220,88)
    #Grafica 2
    canvas.create_oval(10, 142, 40, 172,fill='yellow')
    canvas.create_oval(10, 175, 40, 205,fill='yellow')
    canvas.create_oval(100, 157, 130,187,fill='blue')
    canvas.create_oval(190, 157, 220,187,fill='red')
    #Grafica 3
    canvas.create_oval(10, 208, 40, 238)
    canvas.create_oval(10, 241, 40, 271)
    canvas.create_oval(10, 274, 40, 304)
    canvas.create_oval(100, 223, 130, 253)
    canvas.create_oval(190, 238, 220, 268)
    #Grafica 4
    canvas.create_oval(10, 307, 40, 337)
    canvas.create_oval(10, 340, 40, 370)
    canvas.create_oval(10, 373, 40, 403)
    canvas.create_oval(100, 322, 130, 352)
    canvas.create_oval(190, 337, 220, 367)
    #Grafica 5
    canvas.create_oval(10, 406, 40, 436)
    canvas.create_oval(10, 439, 40, 469)
    canvas.create_oval(10, 472, 40, 502)
    canvas.create_oval(100, 421, 130, 451)
    canvas.create_oval(190, 436, 220, 466)
    #Grafica 6
    canvas.create_oval(10, 505, 40, 535)
    canvas.create_oval(10, 538, 40, 568)
    canvas.create_oval(10, 571, 40, 601)
    canvas.create_oval(100, 520, 130, 550)
    canvas.create_oval(190, 535, 220,565 )
    tk.Label(root, text="Moteado",font=("Arial", 25) ).place(x=1000, y=10)
    tk.Label(root, text="No es un síntoma que caracterice la enfermedad y se presenta independientemente de las").place(x=870, y=90)
    tk.Label(root, text="pudriciones de flecha-cogollo; sin embargo, palmas con pudriciones de flecha acentúan").place(x=870, y=110)
    tk.Label(root, text="el síntoma de moteado. Los moteados leves o moderados desaparecen con los cambios de").place(x=870, y=130)
    tk.Label(root, text="clima y buenas prácticas agronómicas.").place(x=870, y=150)
    tk.Label(root, text="Tratamiento: 1.Revisar cuidadosamente las palmitas de vivero, ante su transplante a").place(x=870, y=190)
    tk.Label(root, text="sitio definitivo, a fin e eliminar todas aquellas sospechosas de estar infectadas").place(x=870, y=210)
    tk.Label(root, text="2.Eliminar especies de gramíneas en los lotes, reemplazándolas por cobertura de").place(x=870, y=230)
    tk.Label(root, text="pueraria Erradicar las palmas, tan pronto presenten síntomas de la enfermedare").place(x=870, y=250)
    tk.Label(root, text="3.Mantener libre de malezas los círculos (zona de plateo) de las palma").place(x=870, y=270)
    tk.Label(root, text="4.Protección de las palmas, especialmente en el vivero, mediante la aplicación de").place(x=870, y=290)
    tk.Label(root, text="insecticidas que eliminen posibles vectores de la enfermedad").place(x=870, y=310)

def graficar3():
    canvas = Canvas(width=500, height=650)
    canvas.pack()
    #Grafica 1
    canvas.create_oval(10, 10, 40, 40)
    canvas.create_oval(10, 43, 40, 73)
    canvas.create_oval(10, 76, 40, 106)
    canvas.create_oval(10, 109, 40, 139)
    canvas.create_oval(100, 25, 130, 55)
    canvas.create_oval(100, 91, 130,121)
    canvas.create_oval(190, 58, 220,88)
    #Grafica 2
    canvas.create_oval(10, 142, 40, 172)
    canvas.create_oval(10, 175, 40, 205)
    canvas.create_oval(100, 157, 130,187)
    canvas.create_oval(190, 157, 220,187)
    #Grafica 3
    canvas.create_oval(10, 208, 40, 238,fill='yellow')
    canvas.create_oval(10, 241, 40, 271,fill='yellow')
    canvas.create_oval(10, 274, 40, 304,fill='yellow')
    canvas.create_oval(100, 223, 130, 253,fill='blue')
    canvas.create_oval(190, 238, 220, 268,fill='red')
    #Grafica 4
    canvas.create_oval(10, 307, 40, 337)
    canvas.create_oval(10, 340, 40, 370)
    canvas.create_oval(10, 373, 40, 403)
    canvas.create_oval(100, 322, 130, 352)
    canvas.create_oval(190, 337, 220, 367)
    #Grafica 5
    canvas.create_oval(10, 406, 40, 436)
    canvas.create_oval(10, 439, 40, 469)
    canvas.create_oval(10, 472, 40, 502)
    canvas.create_oval(100, 421, 130, 451)
    canvas.create_oval(190, 436, 220, 466)
    #Grafica 6
    canvas.create_oval(10, 505, 40, 535)
    canvas.create_oval(10, 538, 40, 568)
    canvas.create_oval(10, 571, 40, 601)
    canvas.create_oval(100, 520, 130, 550)
    canvas.create_oval(190, 535, 220,565 )
    tk.Label(root, text="Pudrición basal del tronco",font=("Arial", 25) ).place(x=900, y=10)
    tk.Label(root, text="Esta enfermedad es mas común en Africa, Asia e Indonesia. Es causada por Ganoderma").place(x=870, y=90)
    tk.Label(root, text="Lucidum y G. Zonatum. Produce que los tejidos invadidos se descompongan y aparezcan").place(x=870, y=110)
    tk.Label(root, text="cavidades más o menos grandes en la base del estipe.").place(x=870, y=130)
    tk.Label(root, text="Tratamiento: Se recomienda la remoción de los tejidos infectados y la aplicación de").place(x=870, y=170)
    tk.Label(root, text="fungicidas protectores con una pasta cicatrizante. Las plantas afectadas deben").place(x=870, y=190)
    tk.Label(root, text="destruirse 'in situ', al igual que sus raíces.").place(x=870, y=210)
    
def graficar4():
    canvas = Canvas(width=500, height=650)
    canvas.pack()
    #Grafica 1
    canvas.create_oval(10, 10, 40, 40)
    canvas.create_oval(10, 43, 40, 73)
    canvas.create_oval(10, 76, 40, 106)
    canvas.create_oval(10, 109, 40, 139)
    canvas.create_oval(100, 25, 130, 55)
    canvas.create_oval(100, 91, 130,121)
    canvas.create_oval(190, 58, 220,88)
    #Grafica 2
    canvas.create_oval(10, 142, 40, 172)
    canvas.create_oval(10, 175, 40, 205)
    canvas.create_oval(100, 157, 130,187)
    canvas.create_oval(190, 157, 220,187)
    #Grafica 3
    canvas.create_oval(10, 208, 40, 238)
    canvas.create_oval(10, 241, 40, 271)
    canvas.create_oval(10, 274, 40, 304)
    canvas.create_oval(100, 223, 130, 253)
    canvas.create_oval(190, 238, 220, 268)
    #Grafica 4
    canvas.create_oval(10, 307, 40, 337,fill='yellow')
    canvas.create_oval(10, 340, 40, 370,fill='yellow')
    canvas.create_oval(10, 373, 40, 403,fill='yellow')
    canvas.create_oval(100, 322, 130, 352,fill='blue')
    canvas.create_oval(190, 337, 220, 367,fill='red')
    #Grafica 5
    canvas.create_oval(10, 406, 40, 436)
    canvas.create_oval(10, 439, 40, 469)
    canvas.create_oval(10, 472, 40, 502)
    canvas.create_oval(100, 421, 130, 451)
    canvas.create_oval(190, 436, 220, 466)
    #Grafica 6
    canvas.create_oval(10, 505, 40, 535)
    canvas.create_oval(10, 538, 40, 568)
    canvas.create_oval(10, 571, 40, 601)
    canvas.create_oval(100, 520, 130, 550)
    canvas.create_oval(190, 535, 220,565 )
    tk.Label(root, text="Añublo foliar",font=("Arial", 25) ).place(x=1000, y=10)
    tk.Label(root, text="Esta enfermedad es mas común en Africa, Asia e Indonesia. Es causada por Ganoderma").place(x=870, y=90)
    tk.Label(root, text="Lucidum y G. Zonatum. Produce que los tejidos invadidos se descompongan y aparezcan").place(x=870, y=110)
    tk.Label(root, text="cavidades más o menos grandes en la base del estipe.").place(x=870, y=130)
    tk.Label(root, text="Tratamiento: Se recomienda la remoción de los tejidos infectados y la aplicación de").place(x=870, y=170)
    tk.Label(root, text="fungicidas protectores con una pasta cicatrizante. Las plantas afectadas deben").place(x=870, y=190)
    tk.Label(root, text="destruirse 'in situ', al igual que sus raíces.").place(x=870, y=210)

    
def graficar5():
    canvas = Canvas(width=500, height=650)
    canvas.pack()
    #Grafica 1
    canvas.create_oval(10, 10, 40, 40)
    canvas.create_oval(10, 43, 40, 73)
    canvas.create_oval(10, 76, 40, 106)
    canvas.create_oval(10, 109, 40, 139)
    canvas.create_oval(100, 25, 130, 55)
    canvas.create_oval(100, 91, 130,121)
    canvas.create_oval(190, 58, 220,88)
    #Grafica 2
    canvas.create_oval(10, 142, 40, 172)
    canvas.create_oval(10, 175, 40, 205)
    canvas.create_oval(100, 157, 130,187)
    canvas.create_oval(190, 157, 220,187)
    #Grafica 3
    canvas.create_oval(10, 208, 40, 238)
    canvas.create_oval(10, 241, 40, 271)
    canvas.create_oval(10, 274, 40, 304)
    canvas.create_oval(100, 223, 130, 253)
    canvas.create_oval(190, 238, 220, 268)
    #Grafica 4
    canvas.create_oval(10, 307, 40, 337)
    canvas.create_oval(10, 340, 40, 370)
    canvas.create_oval(10, 373, 40, 403)
    canvas.create_oval(100, 322, 130, 352)
    canvas.create_oval(190, 337, 220, 367)
    #Grafica 5
    canvas.create_oval(10, 406, 40, 436,fill='yellow')
    canvas.create_oval(10, 439, 40, 469,fill='yellow')
    canvas.create_oval(10, 472, 40, 502,fill='yellow')
    canvas.create_oval(100, 421, 130, 451,fill='blue')
    canvas.create_oval(190, 436, 220, 466,fill='red')
    #Grafica 6
    canvas.create_oval(10, 505, 40, 535)
    canvas.create_oval(10, 538, 40, 568)
    canvas.create_oval(10, 571, 40, 601)
    canvas.create_oval(100, 520, 130, 550)
    canvas.create_oval(190, 535, 220,565 )
    tk.Label(root, text="Deficiencia de magnesio",font=("Arial", 25) ).place(x=900, y=10)
    tk.Label(root, text="Esta enfermedad es mas común en Africa, Asia e Indonesia. Es causada por Ganoderma").place(x=870, y=90)
    tk.Label(root, text="Se caracteriza por un amarillamiento de las hojas de la base del tronco.").place(x=870, y=110)
    tk.Label(root, text="La deficiencia de este elemento es causada por reservas bajas de él en el suelo,").place(x=870, y=150)
    tk.Label(root, text="por la presencia de un subsuelo muy ácido y por el desbalance entre el magnesio").place(x=870, y=170)
    tk.Label(root, text="Tratamiento: El fertilizante más comúnmente empleado para corregir esta deficiencia").place(x=870, y=210)
    tk.Label(root, text="es el sulfato de magnesio.").place(x=870, y=230)

def graficar6():
    canvas = Canvas(width=500, height=650)
    canvas.pack()
    #Grafica 1
    canvas.create_oval(10, 10, 40, 40)
    canvas.create_oval(10, 43, 40, 73)
    canvas.create_oval(10, 76, 40, 106)
    canvas.create_oval(10, 109, 40, 139)
    canvas.create_oval(100, 25, 130, 55)
    canvas.create_oval(100, 91, 130,121)
    canvas.create_oval(190, 58, 220,88)
    #Grafica 2
    canvas.create_oval(10, 142, 40, 172)
    canvas.create_oval(10, 175, 40, 205)
    canvas.create_oval(100, 157, 130,187)
    canvas.create_oval(190, 157, 220,187)
    #Grafica 3
    canvas.create_oval(10, 208, 40, 238)
    canvas.create_oval(10, 241, 40, 271)
    canvas.create_oval(10, 274, 40, 304)
    canvas.create_oval(100, 223, 130, 253)
    canvas.create_oval(190, 238, 220, 268)
    #Grafica 4
    canvas.create_oval(10, 307, 40, 337)
    canvas.create_oval(10, 340, 40, 370)
    canvas.create_oval(10, 373, 40, 403)
    canvas.create_oval(100, 322, 130, 352)
    canvas.create_oval(190, 337, 220, 367)
    #Grafica 5
    canvas.create_oval(10, 406, 40, 436)
    canvas.create_oval(10, 439, 40, 469)
    canvas.create_oval(10, 472, 40, 502)
    canvas.create_oval(100, 421, 130, 451)
    canvas.create_oval(190, 436, 220, 466)
    #Grafica 6
    canvas.create_oval(10, 505, 40, 535,fill='yellow')
    canvas.create_oval(10, 538, 40, 568,fill='yellow')
    canvas.create_oval(10, 571, 40, 601,fill='yellow')
    canvas.create_oval(100, 520, 130, 550,fill='blue')
    canvas.create_oval(190, 535, 220,565 ,fill='red')
    
    tk.Label(root, text="Pudrición de los racimos",font=("Arial", 25) ).place(x=900, y=10)
    tk.Label(root, text="Esta enfermedad es mas común en Africa, Asia e Indonesia. Es causada por Ganoderma").place(x=870, y=90)
    tk.Label(root, text="La pudrición de los frutos y racimos causada por el hongo Marasmius es más frecuente").place(x=870, y=110)
    tk.Label(root, text="en palmas de 3 a 9 años de edad y bajo condiciones de alta humedad ambiental, como").place(x=870, y=130)
    tk.Label(root, text="consecuencia de períodos prolongados de lluvias.").place(x=870, y=150)
    tk.Label(root, text="Los frutos toman una coloración marrón, se vuelven blandos y al final de color negro,").place(x=870, y=190)
    tk.Label(root, text="con el mesocarpió descompuesto casi en su totalidad.").place(x=870, y=210)
    tk.Label(root, text="Tratamiento: Los racimos infectados deben retirarse de las palmas, así como también").place(x=870, y=250)
    tk.Label(root, text="los restos de inflorescencias, mediantes podas sanitarias regulares. Cuando sea").place(x=870, y=270)
    tk.Label(root, text="necesario se realiza la polinización asistida para conseguir un mejor cuajamiento de").place(x=870, y=290)
    tk.Label(root, text="los frutos, para así disminuir el exceso de humedad ambiental mediante un control de").place(x=870, y=310)
    tk.Label(root, text="malezas y mejoramientos de las condiciones de drenaje").place(x=870, y=330)

root=tk.Tk()
root.geometry("4000x1000") 
root.title("Interfaz de abalones")

tk.Label(root, text="Seleccione todas los sintomas que presenta").place(x=10, y=10)

AMHJ=tk.IntVar()
HJM=tk.IntVar()
DCTN=tk.IntVar()
CHJ=tk.IntVar()
MCM=tk.IntVar()
CPH=tk.IntVar()
DPE=tk.IntVar()
CCE=tk.IntVar()
BLM=tk.IntVar()
DG=tk.IntVar()
PV=tk.IntVar()
ECP=tk.IntVar()
RDHR=tk.IntVar()
PCA=tk.IntVar()
SCMH=tk.IntVar()
P39=tk.IntVar()
AHA=tk.IntVar()
MBFE=tk.IntVar()

tk.Checkbutton(root, text="1. Amarillamiento De La Hoja Más Joven", variable=AMHJ, onvalue=1, offvalue=0).place(x=10,y=40)
tk.Checkbutton(root, text="2. Hojas Más Jóvenes Se Observa La Presencia De Un “Mordisco”", variable=HJM, onvalue=1, offvalue=0).place(x=10,y=70)
tk.Checkbutton(root, text="3. Destrucción Completa De Todos Los Nuevos Tejidos", variable=DCTN, onvalue=1, offvalue=0).place(x=10,y=100)
tk.Checkbutton(root, text="4. Colapso De Las Hojas Jóvenes", variable=CHJ, onvalue=1, offvalue=0).place(x=10,y=130)
tk.Checkbutton(root, text="5. Manchas De Color Negro Mate", variable=MCM, onvalue=1, offvalue=0).place(x=10,y=160)
tk.Checkbutton(root, text="6. Caída Prematura De Las Hojas", variable=CPH, onvalue=1, offvalue=0).place(x=10,y=190)
tk.Checkbutton(root, text="7. Descomposición De La Parte Interna Del Estipe", variable=DPE, onvalue=1, offvalue=0).place(x=10,y=220)
tk.Checkbutton(root, text="8. Color Café Claro Hasta Marrón En El Estipe", variable=CCE, onvalue=1, offvalue=0).place(x=10,y=250) 
tk.Checkbutton(root, text="9. Bandas Y Líneas De Colores Con Aspecto De Mapa", variable=BLM, onvalue=1, offvalue=0).place(x=10,y=280) 
tk.Checkbutton(root, text="10. Decoloración Del Grano", variable=DG, onvalue=1, offvalue=0).place(x=10,y=310) 
tk.Checkbutton(root, text="11. Pudrición Y Vaneamiento", variable=PV, onvalue=1, offvalue=0).place(x=10,y=340) 
tk.Checkbutton(root, text="12. Las Espiguillas Afectadas Se Tornan Color Pajizo", variable=ECP, onvalue=1, offvalue=0).place(x=10,y=370) 
tk.Checkbutton(root, text="13. Restringe El Desarrollo De Las Hojas Y Raíces", variable=RDHR, onvalue=1, offvalue=0).place(x=10,y=400) 
tk.Checkbutton(root, text="14. Parte Central Se Torna Amarillo Pálido", variable=PCA, onvalue=1, offvalue=0).place(x=10,y=430) 
tk.Checkbutton(root, text="15. Secamiento Color Marrón En Las Puntas De Las Hojas", variable=SCMH, onvalue=1, offvalue=0).place(x=10,y=460) 
tk.Checkbutton(root, text="16. Palmas De 3 A 9 Años (Más Frecuente)", variable=P39, onvalue=1, offvalue=0).place(x=10,y=490) 
tk.Checkbutton(root, text="17. Alta Humedad Ambiental", variable=AHA, onvalue=1, offvalue=0).place(x=10,y=520) 
tk.Checkbutton(root, text="18. Moho Color Blanco Sobre Los Frutos Enfermos", variable=MBFE, onvalue=1, offvalue=0).place(x=10,y=550) 


tk.Button(root, text="Diagnosticar", command=IA).place(x=100,y=600)

root.mainloop()
