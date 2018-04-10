from tkinter import *

def getLog():
    import subprocess
    lst = []
    dataCompleta = []
    lstSegundaria = []
    p = subprocess.check_output("cscript C:\\Users\\Thiago\\Desktop\\verifica_eventos2.vbs", shell=True)
    p = p[118:].decode('ascii')
    lst.append(p.split("\n"))
    t = lst[0]
    for i in range(len(t)):
        lstSegundaria.append(t[i])
    for i in range(1, len(lstSegundaria), 2):
        try:
            horas = int(lstSegundaria[i][22:24]) - 3
            dia = lstSegundaria[i][20:22]
            DiminuiDia = int(dia)
            mes = lstSegundaria[i][18:20]
            data = lstSegundaria[i][14:18]
            if (horas < 0):
                horas = 24 - horas - 3
                DiminuiDia = DiminuiDia - 1

            x = str(dia) + "/" + str(mes) + "/" + str(data) + " " + str(horas) + " horas"
            dataCompleta.append(x)
            print(lstSegundaria[i][13:])

        except Exception:
            pass
    print(dataCompleta)
    return dataCompleta



master = Tk()

listbox = Listbox(master)
listbox.pack()

data = getLog()
i = 0
for item in data:
    listbox.insert(END, item)
    i += 1
w = Label(master, text="Desligado" + str(i) + " vezes")
w.pack()

mainloop()



