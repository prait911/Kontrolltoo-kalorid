from tkinter import *
import os
import csv

def arvuta_bmr():
    try:
        kaal = float(kaal_entry.get())
        pikkus = float(pikkus_entry.get())
        vanus = int(vanus_entry.get())
        sugu = sugu_var.get()
        aktiivsus_tase = aktiivsus_var.get()



        if sugu == "Mees":
            bmr = 88.36 + (13.4 * kaal) + (4.8 * pikkus) - (5.7 * vanus)
        else:
            bmr = 447.6 + (9.2 * kaal) + (3.1 * pikkus) - (4.3 * vanus)

        aktiivsus_kordaja = {
            "istuv eluviis": 1.2,
            "väike aktiivsus": 1.375,
            "mõõdukas aktiivsus": 1.55,
            "kõrge aktiivsus": 1.725,
            "väga kõrge aktiivsus": 1.9
        }

        bmr_aktiivsus = bmr * aktiivsus_kordaja[aktiivsus_tase]

        tulemus_label.config(text=f"Päevane kalorivajadus: {round(bmr_aktiivsus)} kcal")
    except Exception as e:
        tulemus_label.config(text="Palun sisesta korrektsed andmed!")

raam = Tk()
raam.title("Kalorite Kalkulaator")
raam.geometry("400x500")
raam.configure(bg="lightblue")

pealkiri_label = Label(raam, text="BMR Kalkulaator", font=("Calibri", 16), bg="lightblue")
pealkiri_label.pack(pady=10)

kaal_label = Label(raam, text="Sisesta kaal (kg):", font=("Calibri", 12), bg="lightblue")
kaal_label.pack()
kaal_entry = Entry(raam)
kaal_entry.pack()

pikkus_label = Label(raam, text="Sisesta pikkus (cm):", font=("Calibri", 12), bg="lightblue")
pikkus_label.pack()
pikkus_entry = Entry(raam)
pikkus_entry.pack()

vanus_label = Label(raam, text="Sisesta vanus (1-100):", font=("Calibri", 12), bg="lightblue")
vanus_label.pack()
vanus_entry = Entry(raam)
vanus_entry.pack()

sugu_label = Label(raam, text="Sugu:", font=("Calibri", 12), bg="lightblue")
sugu_label.pack()
sugu_var = StringVar(value="Mees")
mees_radio = Radiobutton(raam, text="Mees", variable=sugu_var, value="Mees", font=("Calibri", 10), bg="lightblue")
mees_radio.pack()
naine_radio = Radiobutton(raam, text="Naine", variable=sugu_var, value="Naine", font=("Calibri", 10), bg="lightblue")
naine_radio.pack()

aktiivsus_label = Label(raam, text="Aktiivsuse tase:", font=("Calibri", 12), bg="lightblue")
aktiivsus_label.pack()
aktiivsus_var = StringVar(value="istuv eluviis")
aktiivsus_valik = OptionMenu(raam, aktiivsus_var, "istuv eluviis", "väike aktiivsus", "mõõdukas aktiivsus", "kõrge aktiivsus", "väga kõrge aktiivsus")
aktiivsus_valik.pack()

arvuta_nupp = Button(raam, text="Arvuta", font=("Calibri", 12), command=arvuta_bmr)
arvuta_nupp.pack(pady=12)

tulemus_label = Label(raam, text="", font=("Calibri", 12), bg="lightblue")
tulemus_label.pack(pady=10)


kaust = "andmed"
faili_nimi = os.path.join(kaust, "toit_kalorid.csv")

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
        for line in csvreader:


if not os.path.exists(kaust):
    os.makedirs(kaust)





raam.mainloop()

