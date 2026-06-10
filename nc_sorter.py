import os 
import shutil
import threading
import tkinter as tk 
from tkinter import filedialog, scrolledtext,ttk


DSTV_KODY={
    #blachy
    "B":        "blachy",
    "BL":       "blachy",
    "PL":       "blachy",
    "PLT":      "blachy",
    "PLATE":    "blachy",
    "FLAT":     "blachy",
    "FB":       "blachy",       
    "FL":       "blachy",       
    "BLECH":    "blachy",       
    "SHEET":    "blachy",
    "STRIP":    "blachy",
    #dwuteowe
    "I":        "belki_dwuteowe",
    "IPE":      "belki_dwuteowe",
    "IPN":      "belki_dwuteowe",
    "HEA":      "belki_dwuteowe",
    "HEB":      "belki_dwuteowe",
    "HEM":      "belki_dwuteowe",
    "HEAA":     "belki_dwuteowe",
    "HD":       "belki_dwuteowe",
    "HP":       "belki_dwuteowe",
    "W":        "belki_dwuteowe",
    "S":        "belki_dwuteowe",  
    "UB":       "belki_dwuteowe",   
    "UC":       "belki_dwuteowe",   
    "UBP":      "belki_dwuteowe",
    #ceowniki
    "U":        "ceowniki",
    "C":        "ceowniki",
    "UPN":      "ceowniki",
    "UPE":      "ceowniki",
    "UPA":      "ceowniki",
    "UNP":      "ceowniki",
    "PFC":      "ceowniki",        
    "CH":       "ceowniki",
    "MC":       "ceowniki",         
    "CHANNEL":  "ceowniki",
    "U-PROFIL": "ceowniki",
    "C-PROFIL": "ceowniki",
    "L":        "katowniki",
    "ANGLE":    "katowniki",
    "EA":       "katowniki",        
    "UA":       "katowniki",       
 
    #Teowniki 
    "T":        "teowniki",
    "WT":       "teowniki",        
    "ST":       "teowniki",         
    "MT":       "teowniki",        
    "TEE":      "teowniki",
 
    #Rury okragle
    "RO":       "rury_okragle",     
    "CHS":      "rury_okragle",    
    "PIPE":     "rury_okragle",
    "ROHR":     "rury_okragle",     
    "OB":       "rury_okragle",    
    "SO":       "rury_okragle",     
    "E":        "rury_okragle",     
    "TR":       "rury_okragle",     
    "SH":       "rury_okragle",     
 
    #Prety okragle
    "RU":       "prety_okragle",    
    "RND":      "prety_okragle",
    "ROD":      "prety_okragle",
    "BAR":      "prety_okragle",
    "RB":       "prety_okragle",
    "RUNDSTAHL":"prety_okragle",    
 
    # Rury prostokat 
    "M":        "rury_prostokat",   
    "RHS":      "rury_prostokat",  
    "SHS":      "rury_prostokat",   
    "CFRHS":    "rury_prostokat",   
    "CFSHS":    "rury_prostokat",  
    "HSS":      "rury_prostokat",   
    "BOX":      "rury_prostokat",
    "HOHLPROFIL":"rury_prostokat", 
 
    #specjalne
    "SF":       "profile_specjalne",    
    "Z":        "profile_specjalne",
    "ZED":      "profile_specjalne",
    "ZETA":     "profile_specjalne",
    "SIGMA":    "profile_specjalne",
    "OMEGA":    "profile_specjalne",
    "HAT":      "profile_specjalne",
    "COLD":     "profile_specjalne",    
    "CF":       "profile_specjalne",   
}

NAZWA_PREFIKSY=[
    #Belki dwuteowe I/H
    ("HEAA",     "belki_dwuteowe"),
    ("HEM",      "belki_dwuteowe"),
    ("HEB",      "belki_dwuteowe"),
    ("HEA",      "belki_dwuteowe"),
    ("IPE",      "belki_dwuteowe"),
    ("IPN",      "belki_dwuteowe"),
    ("HD ",      "belki_dwuteowe"),   
    ("HP ",      "belki_dwuteowe"),
    ("UB",       "belki_dwuteowe"),   
    ("UC",       "belki_dwuteowe"),   
    ("UBP",      "belki_dwuteowe"),
    ("W ",       "belki_dwuteowe"),   
    ("W1",       "belki_dwuteowe"),
    ("W2",       "belki_dwuteowe"),
    ("W3",       "belki_dwuteowe"),
    ("W4",       "belki_dwuteowe"),
    ("W5",       "belki_dwuteowe"),
    ("W6",       "belki_dwuteowe"),
    ("W8",       "belki_dwuteowe"),
    ("S ",       "belki_dwuteowe"),  
 
    #Ceowniki
    ("UPN",      "ceowniki"),
    ("UPE",      "ceowniki"),
    ("UPA",      "ceowniki"),
    ("UNP",      "ceowniki"),
    ("PFC",      "ceowniki"),
    ("MC",       "ceowniki"),
    ("CH",       "ceowniki"),
 
    #Katowniki
    ("L ",       "katowniki"),        
    ("L1",       "katowniki"),
    ("L2",       "katowniki"),
    ("L3",       "katowniki"),
    ("L4",       "katowniki"),
    ("L5",       "katowniki"),
    ("L6",       "katowniki"),
    ("L7",       "katowniki"),
    ("L8",       "katowniki"),
    ("L9",       "katowniki"),
    ("EA",       "katowniki"),
    ("UA",       "katowniki"),
 
    #Teowniki
    ("WT",       "teowniki"),
    ("MT",       "teowniki"),
    ("T ",       "teowniki"),        
    ("T1",       "teowniki"),
    ("T2",       "teowniki"),
    ("T3",       "teowniki"),
 
    #Rury prostokat / kwadrat
    ("CFRHS",    "rury_prostokat"),
    ("CFSHS",    "rury_prostokat"),
    ("RHS",      "rury_prostokat"),
    ("SHS",      "rury_prostokat"),
    ("HSS",      "rury_prostokat"),
    ("TR",       "rury_prostokat"), 
 
    #Rury okragle / owalne
    ("CHS",      "rury_okragle"),
    ("RO",       "rury_okragle"),
    ("OB",       "rury_okragle"),     
    ("SO",       "rury_okragle"),     
    ("SH",       "rury_okragle"),     
    ("E ",       "rury_okragle"),     
 
    #Prety okragle lite
    ("RU",       "prety_okragle"),
    ("RND",      "prety_okragle"),
    ("ROD",      "prety_okragle"),
 
    #Blachy / plaskowniki
    ("PLT",      "blachy"),
    ("PL",       "blachy"),
    ("BL",       "blachy"),           
    ("FB",       "blachy"),          
    ("FL",       "blachy"),
 
    #Profile specjalne
    ("ZED",      "profile_specjalne"),
    ("ZETA",     "profile_specjalne"),
    ("SIGMA",    "profile_specjalne"),
    ("OMEGA",    "profile_specjalne"),
    ("HAT",      "profile_specjalne"),
    ("SF",       "profile_specjalne"),
    ("Z ",       "profile_specjalne"),
]

def _dopasuj_prefiks(tekst_upper,prefiksy):
    for prefiks, folder in prefiksy:
        if tekst_upper.startswith(prefiks):
            return folder
        return None

def identyfikuj_typ(linie):
    BLOKI = {"AK","BO","SI","EN","IK","PU","KO","KA","BA","PI"}
    st_linie= []
    wewnatrz_st=False
    
    for linia in linie:
        s=linia.strip()
        if s =="ST":
            wewnatrz_st=True
            st_linie.append(s)
            continue
        if wewnatrz_st:
            if s and s[:2].upper() in BLOKI:
                break
            st_linie.append(s)
    st_dane= [l for l in st_linie if l]
    nazwa_profilu=st_dane[7].strip() if len(st_dane)>= 8 else "?"
    kod_dstv_raw =st_dane[8].strip() if len(st_dane)>= 9 else ""

    if kod_dstv_raw:
        kod_upper=kod_dstv_raw.upper()
        if kod_upper in DSTV_KODY:
            return DSTV_KODY[kod_upper],nazwa_profilu

    if nazwa_profilu != "?":
        folder= _dopasuj_prefiks(nazwa_profilu.upper(),NAZWA_PREFIKSY)
        if folder:
            return folder,nazwa_profilu
    for linia in st_dane[1:]:
        u=linia.strip().upper()
        if u in DSTV_KODY:
            return DSTV_KODY[u],linia.strip()
        folder = _dopasuj_prefiks(u,NAZWA_PREFIKSY)
        if folder:
            return folder,linia.strip()
    return "inne",nazwa_profilu

def sortuj_pliki_nc(folder_wejsciowy,log_func,gotowe_func):
    pliki_nc= [p for p in os.listdir(folder_wejsciowy) if p.lower().endswith(".nc")]

    if not pliki_nc:
        print("[INFO] Brak plików .nc w folderze ")
        return
    katalog_bazowy = os.path.dirname(folder_wejsciowy)
    liczniki={}

    log_func(f"\nPrzetwarzam {len(pliki_nc)} plikow  NC... \n")
    for plik in sorted(pliki_nc):
        sciezka_src = os.path.join(folder_wejsciowy,plik)
        try:
            with open(sciezka_src, "r", encoding="utf-8", errors="replace") as f:
                linie=f.readlines()
        except Exception as e:
            log_func(f" [BLAD] {plik}: {e}")
            folder_docelowy_nazwa="inne"
            nazwa_profilu="BLAD_ODCZYTU"
        else:
            folder_docelowy_nazwa, nazwa_profilu = identyfikuj_typ(linie)

        folder_docelowy=os.path.join(katalog_bazowy, folder_docelowy_nazwa)
        if not os.path.exists(folder_docelowy_nazwa):
            os.makedirs(folder_docelowy)
            print(f"[INFO] Nowy folder: {folder_docelowy_nazwa}/")

        shutil.copy(sciezka_src,os.path.join(folder_docelowy,plik))
        liczniki[folder_docelowy_nazwa]=liczniki.get(folder_docelowy_nazwa, 0 ) +1
        tag = "INNE ?" if folder_docelowy_nazwa == "inne" else folder_docelowy_nazwa
        log_func(f"{plik:<42} -> [{tag:<22}] profil:{nazwa_profilu}")
    gotowe_func(liczniki)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NC Sorter")
        self.resizable(False,False)
        self.configure(bg="#1e1e2e")
        self._build_ui()

    def _build_ui(self):
        PAD = 14
        BG = "#1e1e2e"
        BG2 = "#2a2a3e"
        ACCENT = "#7c5cbf"
        ACCENT_H = "#9b78e0"
        FG = "#cdd6f4"
        FG_DIM = "#6c7086"
        GREEN = "#a6e3a1"
        RED = "#f38ba8"
        YELLOW = "#f9e2af"
        FONT = ("Segoe UI",10)
        FONT_B = ("Segoe UI",10, "bold")
        FONT_BIG = ("Segoe UI", 13 ,"bold")

        self._fg = FG
        self._green= GREEN
        self._red = RED
        self._yellow = YELLOW
        self._bg2 = BG2
        self._accent = ACCENT

        hdr = tk.Frame(self,bg=ACCENT, pady=10)
        hdr.pack(fill="x")
        tk.Label(hdr, text="NC Sorter", font=("Segoe UI",16, "bold"), bg=ACCENT,fg="white").pack()
        tk.Label(hdr, text="Sortowanie plikow NC wedlug typu profilu", font=("Segoe UI",9), bg=ACCENT, fg="#e0d5f5").pack()

        frm_path=tk.Frame(self,bg=BG,padx=PAD,pady=PAD)
        frm_path.pack(fill="x")
        tk.Label(frm_path,text="Folder z plikami NC:", font=FONT_B,bg=BG,fg=FG).pack(anchor="w")
        
        row = tk.Frame(frm_path,bg=BG)
        row.pack(fill="x", pady=(4,0))
        
        self._var_folder = tk.StringVar()
        entry= tk.Entry(row,textvariable=self._var_folder, font=FONT,bg=BG2,fg=FG,insertbackground=FG,relief="flat",bd=0,highlightthickness=1,highlightbackground=FG_DIM, highlightcolor=ACCENT)
        entry.pack(side="left",fill="x",expand=True,ipady=6,padx=(0,8))

        tk.Button(row,text="Przegladaj...",font=FONT_B,bg=ACCENT,fg="white",activebackground=ACCENT_H,activeforeground="white",relief="flat",bd=0,padx=14,pady=6,cursor="hand2",command=self._wybierz_folder).pack(side="left")
        tk.Frame(self,bg=FG_DIM, height=1).pack(fill="x", padx=PAD)

        frm_log=tk.Frame(self,bg=BG,padx=PAD,pady=10)
        frm_log.pack(fill="both",expand=True)
        tk.Label(frm_log,text="Log:",font=FONT_B,bg=BG,fg=FG).pack(anchor="w")

        self._log=scrolledtext.ScrolledText(
            frm_log, font=("Consolas",9),bg=BG2,fg=FG,insertbackground=FG,relief="flat",bd=0,highlightthickness=1,highlightbackground=FG_DIM,state="disabled",width=78,height=18
        )
        self._log.pack(fill="both",expand=True,pady=(4,0))

        self._log.tag_config("ok",foreground=GREEN)
        self._log.tag_config("err",foreground=RED)
        self._log.tag_config("info",foreground=YELLOW)
        self._log.tag_config("dim",foreground=FG_DIM)
        self._log.tag_config("header",foreground=ACCENT_H)
        frm_prog=tk.Frame(self,bg=BG,padx=0,pady=8)
        frm_prog.pack(fill="x")

        style=ttk.Style()
        style.theme_use("clam")
        style.configure("nc.Horizontal.TProgressbar",troughcolor=BG2,background=ACCENT,bordervolor=BG,lightcolor=ACCENT,darkcolor=ACCENT)
        self._progress=ttk.Progressbar(frm_prog,style="nc.Horizontal.TProgressbar",mode="indeterminate",length=400)
        self._progress.pack(fill="x") 

        frm_btn=tk.Frame(self,bg=BG,padx=PAD,pady=0)
        frm_btn.pack(fill="x")

        self._btn_start=tk.Button(frm_btn,text="=> START",font=("Segoe UI",11,"bold"),bg=ACCENT,fg="white",activebackground=ACCENT_H,activeforeground="white",relief="flat",bd=0,padx=24,pady=10,cursor="hand2",command=self._start)
        self._btn_start.pack(side="right")
        self._lbl_status=tk.Label(frm_btn,text="Gotowy.",font=FONT,bg=BG,fg=FG_DIM)
        self._lbl_status.pack(side="left",pady=4)

    def _wybierz_folder(self):
            folder=filedialog.askdirectory(title="Wybierz folder z plikami NC")
            if folder:
                self._var_folder.set(folder)
                self._lbl_status.config(text="Folder wybrany kliknij START.")

    def _start(self):
            folder=self._var_folder.get().strip()
            if not folder or not os.path.isdir(folder):
                self._log_write("[BLAD] Wybierz prawidlowy folder przed startem.\n","err")
                return
            self._btn_start.config(state="disabled")
            self._progress.start(12)
            self._lbl_status.config(text="Przetwarzanie...")
            self._log_clear()

            threading.Thread(
                target=sortuj_pliki_nc,
                args=(folder,self._log_write_safe,self._on_done),
                daemon=True
            ).start()
    def _on_done(self,liczniki):
            self.after(0,self._pokaz_podsumowanie,liczniki)
    def _pokaz_podsumowanie(self,liczniki):
            self._progress.stop()
            self._btn_start.config(state="normal")
            if not liczniki:
                self._lbl_status.config(text="Brak plikow NC.")
                return
            razem=sum(liczniki.values())
            self._log_write("\n" + "-"*60 +"\n","dim")
            self._log_write("PODSUMOWANIE\n","header") 
            self._log_write("-"*60 + "\n","dim")  
            for folder,ile in sorted(liczniki.items()):
                znacznik="(?)" if folder=="inne" else ""
                tag="err" if folder == "inne" else "ok"
                self._log_write(f" {folder:<30}: {ile:>4} plikow{znacznik}\n",tag)

            self._log_write("-"*60 + "\n","dim")
            self._log_write(f" {'RAZEM':<30}: {razem:>4} plikow\n","header")
            if "inne" in liczniki:
                self._log_write(
                    f"\n [UWAGA] {liczniki['inne']} plik(ow) trafilo do 'inne'- sprawdz je recznie.\n","err"
                )   
                self._lbl_status.config(text=f"Gotowe. {razem} plkow ({liczniki['inne']} nierozpoznanych).")
            else:
                self._lbl_status.config(text=f"Gotowe. Posortowano {razem} plikow.")
    def _log_write(self, tekst, tag=None):
            self._log.config(state="normal")
            if tag:
                self._log.insert("end", tekst, tag)
            else:
                self._log.insert("end", tekst)
            self._log.see("end")
            self._log.config(state="disabled")
 
    def _log_write_safe(self, tekst):
        
        tag = None
        if "[BLAD]" in tekst or "INNE" in tekst:
            tag = "err"
        elif "[+]" in tekst or "[INFO]" in tekst:
            tag = "info"
        elif "->" in tekst:
            tag = "ok"
        self.after(0, self._log_write, tekst + "\n", tag)
 
    def _log_clear(self):
        self._log.config(state="normal")
        self._log.delete("1.0", "end")
        self._log.config(state="disabled")
 
 

if __name__ == "__main__":
    app = App()
    app.mainloop()       