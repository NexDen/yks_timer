from tkinter import*
from datetime import datetime
from datetime import timedelta


def bekle(ms):
    for _ in range(ms):
        p.after(1)
        p.update()

if __name__ == '__main__':
    # pencereyi ayarla
    p = Tk()
    p.geometry(f"300x170+{p.winfo_screenwidth()-300}+0")
    p.config(bg="black")
    p.resizable(0,0)
    p.overrideredirect(True)
    p.attributes("-transparentcolor", "black")

    # font = "Bahnschrift"
    font = "Segoe UI"

    Label(p, text="YKS'ye", bg="black", fg="white",font=(font, 20)).pack()

    l_gün = Label(p, bg="black", fg="white", font=(font, 48))
    l_gün.pack()

    l_diğer = Label(p, bg="black", fg="white", font=(font, 10))
    l_diğer.pack()

    # ana döngü: yks ye kalan zamanı hesapla
    yks = datetime(2023, 6, 17, 10)
    while True:
        şuan = datetime.now()
        sec = (yks-şuan).total_seconds()
        td_str = str(timedelta(seconds=sec))
        zaman_str = td_str.split(':') # giriş formatı: "dddd days, hh:mm:ss.ssssss"
        gün = zaman_str[0].split("days,")[0].strip()
        saat = zaman_str[0].split("days,")[1].strip()
        dakika = zaman_str[1]
        saniye = int(float(zaman_str[2])) # SADECE int() ÇALIŞMADI !

        l_gün.config(text=f"{gün} GÜN")
        l_diğer.config(text=f"{saat} SAAT {dakika} DAKİKA {saniye} SANİYE")
        bekle(10)
