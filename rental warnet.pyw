import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import pymysql
import datetime
import time


root = Tk()
class WindowDraggable():

        def __init__(self, label):
                self.label = label
                label.bind('<ButtonPress-1>', self.StartMove)
                label.bind('<ButtonRelease-1>', self.StopMove)
                label.bind('<B1-Motion>', self.OnMotion)

        def StartMove(self, event):
                self.x = event.x
                self.y = event.y

        def StopMove(self, event):
                self.x = None
                self.y = None

        def OnMotion(self,event):
                x = (event.x_root - self.x - self.label.winfo_rootx() + self.label.winfo_rootx())
                y = (event.y_root - self.y - self.label.winfo_rooty() + self.label.winfo_rooty())
                root.geometry("+%s+%s" % (x, y))
                
judul_kolom = ("ID","Nama","Internet","Mengetik","GO","Scan","Print WR","Print HP","Teh Botol","Total")
class Warnet:
        def __init__(self, parent):
                self.parent = parent
                self.parent.protocol("WM_DELETE_WINDOWS", self.keluar)
                lebar=650
                tinggi=670
                setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
                setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
                self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
                self.parent.overrideredirect(1)
                self.aturKomponen()
                self.auto()
                
        def keluar(self,event=None):
                self.parent.destroy()
                
        def OnDoubleClick(self, event):

                self.entKode.config(state="normal")
                self.entKode.delete(0, END)
                self.entNama.delete(0, END)
                self.entInternet.delete(0, END)
                self.entMengetik.delete(0, END)
                self.entGO.delete(0, END)
                self.entScan.delete(0, END)
                self.entPrintWarna.delete(0, END)
                self.entPrintHitamPutih.delete(0, END)
                self.entTehBotol.delete(0, END)
            
                it = self.trvTabel.selection()[0]
                ck = str(self.trvTabel.item(it,"values"))[2:6]
                    
                self.entKode.insert(END, ck)
                
                cKode = self.entKode.get()
                con = pymysql.connect(db="db_warnet", user="root", passwd="", host="localhost", port=3306,autocommit=True)
                cur = con.cursor()
                sql = "SELECT nama,internet,mengetik,game_online,scan,print_warna,print_hitam_putih,teh_botol FROM warnet WHERE kode = %s"
                cur.execute(sql,cKode)
                data = cur.fetchone()
                
        
                self.entNama.insert(END, data[0])
                
                #
                self.entInternet.insert(END, data[1])                
                self.entMengetik.insert(END, data[2])
                self.entGO.insert(END, data[3])
                self.entScan.insert(END, data[4])
                self.entPrintWarna.insert(END, data[5])
                self.entPrintHitamPutih.insert(END, data[6])
                self.entTehBotol.insert(END, data[7])
                self.entKode.config(state="disable")
                self.btnSave.config(state="disable")
                self.btnUpdate.config(state="normal")
                self.btnDelete.config(state="normal")
                
        def aturKomponen(self):
                frameWin = Frame(self.parent, bg="#ADD8E6")
                frameWin.pack(fill=X,side=TOP)
                WindowDraggable(frameWin)
                Label(frameWin, text='Warnet Connect',bg="#ADD8E6",fg="black").pack(side=LEFT,padx=20)
                buttonx = Button(frameWin, text="X",fg="white", bg="#FA8072", width=6, height=2,bd=0,\
                                 activebackground="#FB8072",activeforeground="white", command=self.onClose, relief=FLAT)
                buttonx.pack(side=RIGHT)
                mainFrame = Frame(self.parent)
                mainFrame.pack(side=TOP,fill=X)
                btnFrame = Frame(self.parent)
                btnFrame.pack(side=TOP, fill=X)
                tabelFrame = Frame(self.parent)
                tabelFrame.pack( expand=YES, side=TOP,fill=Y)
       
                Label(mainFrame, text='  ').grid(row=0, column=0)
                Label(btnFrame, text='  ').grid(row=1, column=0)

                Label(mainFrame, text='ID').grid(row=1, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=1, column=1, sticky=W,pady=5,padx=10)
                self.entKode = Entry(mainFrame, width=30)
                self.entKode.grid(row=1, column=2,sticky=W)


                Label(mainFrame, text="Nama Customer").grid(row=2, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=2, column=1, sticky=W,pady=5,padx=10)
                self.entNama = Entry(mainFrame, width=30)
                self.entNama.grid(row=2, column=2,sticky=W)

                Label(mainFrame, text="Internet").grid(row=3, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=3, column=1, sticky=W,pady=5,padx=10)
                Label(mainFrame, text='Menit').grid(row=3, column=3, sticky=W,pady=5,padx=10)
                self.entInternet = Entry(mainFrame, width=30)
                self.entInternet.grid(row=3, column=2,sticky=W) 
                
                Label(mainFrame, text="Mengetik").grid(row=4, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=4, column=1, sticky=W,pady=5,padx=10)
                Label(mainFrame, text='Menit').grid(row=4, column=3, sticky=W,pady=5,padx=10)
                self.entMengetik = Entry(mainFrame, width=30)
                self.entMengetik.grid(row=4, column=2,sticky=W)

                Label(mainFrame, text="Game Online").grid(row=5, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=5, column=1, sticky=W,pady=5,padx=10)
                Label(mainFrame, text='Menit').grid(row=5, column=3, sticky=W,pady=5,padx=10)
                self.entGO = Entry(mainFrame, width=30)
                self.entGO.grid(row=5, column=2,sticky=W)

                Label(mainFrame, text="Scan").grid(row=6, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=6, column=1, sticky=W,pady=5,padx=10)
                Label(mainFrame, text='File').grid(row=6, column=3, sticky=W,pady=5,padx=10)
                self.entScan = Entry(mainFrame, width=30)
                self.entScan.grid(row=6, column=2,sticky=W)

                Label(mainFrame, text="Print Warna").grid(row=7, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=7, column=1, sticky=W,pady=5,padx=10)
                Label(mainFrame, text='Lembar').grid(row=7, column=3, sticky=W,pady=5,padx=10)
                self.entPrintWarna = Entry(mainFrame, width=30)
                self.entPrintWarna.grid(row=7, column=2,sticky=W)

                Label(mainFrame, text="Print Hitam Putih").grid(row=8, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=8, column=1, sticky=W,pady=5,padx=10)
                Label(mainFrame, text='Lembar').grid(row=8, column=3, sticky=W,pady=5,padx=10)
                self.entPrintHitamPutih = Entry(mainFrame, width=30)
                self.entPrintHitamPutih.grid(row=8, column=2,sticky=W)

                Label(mainFrame, text="Teh Botol").grid(row=9, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=9, column=1, sticky=W,pady=5,padx=10)
                Label(mainFrame, text='Pcs').grid(row=9, column=3, sticky=W,pady=5,padx=10)
                self.entTehBotol = Entry(mainFrame, width=30)
                self.entTehBotol.grid(row=9, column=2,sticky=W)


                self.btnSave = Button(btnFrame, text='Save',\
                                        command=self.onSave, width=10,\
                                        relief=FLAT, bd=2, bg="#ADD8E6", fg="black",activebackground="#ADD8E6",activeforeground="white" )
                self.btnSave.grid(row=0, column=1,padx=5)

                self.btnUpdate = Button(btnFrame, text='Update',\
                                        command=self.onUpdate,state="disable", width=10,\
                                        relief=FLAT, bd=2, bg="#ADD8E6", fg="black",activebackground="#ADD8E6",activeforeground="white")
                self.btnUpdate.grid(row=0,column=2,pady=10, padx=5)
                
                self.btnClear = Button(btnFrame, text='Clear',\
                                        command=self.onClear, width=10,\
                                       relief=FLAT, bd=2, bg="#ADD8E6", fg="black",activebackground="#ADD8E6",activeforeground="black")
                self.btnClear.grid(row=0,column=3,pady=10, padx=5)

                self.btnDelete = Button(btnFrame, text='Delete',\
                                        command=self.onDelete,state="disable", width=10,\
                                        relief=FLAT, bd=2, bg="#FC6042", fg="white",activebackground="#FC6042",activeforeground="black")
                self.btnDelete.grid(row=0,column=4,pady=10, padx=5)


                self.fr_data = Frame(tabelFrame, bd=10)
                self.fr_data.pack(fill=BOTH, expand=YES)
                self.trvTabel = ttk.Treeview(self.fr_data, columns=judul_kolom,show='headings')
                self.trvTabel.bind("<Double-1>", self.OnDoubleClick)
                sbVer = Scrollbar(self.fr_data, orient='vertical',command=self.trvTabel.yview)
                sbVer.pack(side=RIGHT, fill=Y)
                
                self.trvTabel.pack(side=TOP, fill=BOTH)
                self.trvTabel.configure(yscrollcommand=sbVer.set)
                self.table()
                
        def table(self):

        
                con = pymysql.connect(db="db_warnet", user="root", passwd="", host="localhost", port=3306,autocommit=True)
                cur = con.cursor()
                cur.execute("SELECT kode AS ID,nama,FORMAT(if(internet >0 and internet <=30,(30/60)*4000,(internet/60)*4000),0)internet,FORMAT(if(mengetik >0 and mengetik <=30,(30/60)*2000,(mengetik/60)*2000),0)mengetik,FORMAT(if(game_online >0 and game_online <=30,(30/60)*5000,(game_online/60)*5000),0)game_online,FORMAT((scan*1000),0)scan,FORMAT((print_warna*500),0)print_warna,FORMAT((print_hitam_putih*300),0)print_hitam_putih,FORMAT((teh_botol*3000),0)teh_botol,FORMAT(if(internet >0 and internet <=30,(30/60)*4000,(internet/60)*4000)+if(mengetik >0 and mengetik <=30,(30/60)*2000,(mengetik/60)*2000)+if(game_online >0 and game_online <=30,(30/60)*5000,(game_online/60)*5000)+(scan*1000)+(print_warna*500)+(print_hitam_putih*300)+(teh_botol*3000),0) total FROM warnet order by kode desc")
                data_table = cur.fetchall()

                for kolom in judul_kolom:
                    self.trvTabel.heading(kolom,text=kolom)
                self.trvTabel.column("ID", width=35,anchor="w")
                self.trvTabel.column("Nama", width=70,anchor="center")
                self.trvTabel.column("Internet", width=60,anchor="e")
                self.trvTabel.column("Mengetik", width=60,anchor="e")
                self.trvTabel.column("GO", width=50,anchor="e")
                self.trvTabel.column("Scan", width=60,anchor="e")
                self.trvTabel.column("Print WR", width=60,anchor="e")
                self.trvTabel.column("Print HP", width=60,anchor="e")
                self.trvTabel.column("Teh Botol", width=60,anchor="e") 
                self.trvTabel.column("Total", width=60,anchor="e")
                i=0
                for dat in data_table:
                    if(i%2):
                        baris="genap"
                    else:
                        baris="ganjil"
                    self.trvTabel.insert('', 'end', values=dat, tags=baris)
                    i+=1

                self.trvTabel.tag_configure("ganjil", background="#FFFFFF")
                self.trvTabel.tag_configure("genap", background="whitesmoke")
                cur.close()
                con.close()        
                       

        def auto(self):
                con = pymysql.connect(db='db_warnet', user='root', passwd='', host='localhost', port=3306,autocommit=True)
                cur = con.cursor()
                cuv = con.cursor()
                sqlkode = "SELECT max(kode) FROM warnet"
                sql = "SELECT kode FROM warnet"
                cur.execute(sqlkode)
                cuv.execute(sql)
                maxkode = cur.fetchone()
                
                if cuv.rowcount> 0:      
                    autohit = int(maxkode[0])+1
                    hits = "000"+str(autohit)
                    if len(hits) == 4:
                        self.entKode.insert(0, hits)
                        self.entNama.focus_set()
                    elif len(hits) == 5:
                        hit = "00"+str(autohit)
                        self.entKode.insert(0, hit)
                        self.entNama.focus_set()
                    elif len(hits) == 6:
                        hit = "0"+str(autohit)
                        self.entKode.insert(0, hit)
                        self.entNama.focus_set()
                    elif len(hits) == 7:
                        hit = ""+str(autohit)
                        self.entKode.insert(0, hit)
                        self.entNama.focus_set()
                    
                    else:
                        messagebox.showwarning(title="Peringatan", \
                                    message="maaf lebar data hanya sampai 4 digit")
                        
                else:
                    hit = "0001"
                    self.entKode.insert(0, hit)
                    self.entNama.focus_set()
                    
                self.entKode.config(state="readonly")
        def onClose(self, event=None):
                self.parent.destroy()


        def onDelete(self):
                con = pymysql.connect(db='db_warnet', user='root', passwd='', host='localhost', port=3306,autocommit=True)
                cur = con.cursor()
                self.entKode.config(state="normal")
                cKode = self.entKode.get()
                sql = "DELETE FROM warnet WHERE kode =%s"
                cur.execute(sql,cKode)
                self.onClear()
                messagebox.showinfo(title="Informasi", \
                                    message="Data sudah di hapus.")
                
                cur.close()
                con.close()


        def onClear(self):
                self.btnSave.config(state="normal")
                self.btnUpdate.config(state="disable")
                self.btnDelete.config(state="disable")
                self.entKode.config(state="normal")
                self.entKode.delete(0, END)
                self.entNama.delete(0, END)
                self.entInternet.delete(0, END)
                self.entMengetik.delete(0, END)
                self.entGO.delete(0, END)
                self.entScan.delete(0, END)
                self.entPrintWarna.delete(0, END)
                self.entPrintHitamPutih.delete(0, END)
                self.entTehBotol.delete(0, END)
                self.trvTabel.delete(*self.trvTabel.get_children())
                self.fr_data.after(0, self.table())
        
                self.auto()
                self.entNama.focus_set()

                        
        def onSave(self):
        
                con = pymysql.connect(db='db_warnet', user='root', passwd='', host='localhost', port=3306,autocommit=True)
 
                cKode = self.entKode.get()
                cNama = self.entNama.get()

                ####
                cInternet = self.entInternet.get()
                cMengetik = self.entMengetik.get()
                cGO = self.entGO.get()
                cScan = self.entScan.get()
                cPrintWarna = self.entPrintWarna.get()
                cPrintHitamPutih = self.entPrintHitamPutih.get()
                cTehBotol = self.entTehBotol.get()
                if cNama == 0:
                        messagebox.showwarning(title="Peringatan",message="Nama Tidak boleh kosong")    
                else:         
                        cur = con.cursor()
                        sql = "INSERT INTO warnet (kode,nama,internet,mengetik,game_online,scan,print_warna,print_hitam_putih,teh_botol)"+\
                              "VALUES(%s,UPPER(%s),%s,%s,%s,%s,%s,%s,%s)"
                        cur.execute(sql,(cKode,cNama,cInternet,cMengetik,cGO,cScan,cPrintWarna,cPrintHitamPutih,cTehBotol))
                        self.onClear()
                        messagebox.showinfo(title="Informasi", \
                                            message="Data sudah di tersimpan.")
                        
                        cur.close()
                        con.close()
                
        def onUpdate(self):
                cKode = self.entKode.get()
                
                if len(cKode) == 0:
                        messagebox.showwarning(title="Peringatan",message="Kode kosong.")
                        self.entKode.focus_set()

                else:
                        con = pymysql.connect(db='db_warnet', user='root', passwd='', host="localhost",\
                                      port=3306, autocommit=True)
                        cur = con.cursor()
                        cKode = self.entKode.get()
                        cNama = self.entNama.get()
                        cInternet = self.entInternet.get()
                        cMengetik = self.entMengetik.get()
                        cGO = self.entGO.get()
                        cScan = self.entScan.get()
                        cPrintWarna = self.entPrintWarna.get()
                        cPrintHitamPutih = self.entPrintHitamPutih.get()
                        cTehBotol = self.entTehBotol.get()
                        
                        sql = "UPDATE warnet SET nama=%s,internet=%s,mengetik=%s,game_online=%s,scan=%s,print_warna=%s,print_hitam_putih=%s,teh_botol=%s WHERE kode =%s"
                        cur.execute(sql,(cNama,cInternet,cMengetik,cGO,cScan,cPrintWarna,cPrintHitamPutih,cTehBotol,cKode))
                        self.onClear()
                        messagebox.showinfo(title="Informasi", \
                                    message="Data sudah di terupdate.")

                        cur.close()
                        con.close()   
                     

def main():
    Warnet(root)
    root.mainloop()
main()
