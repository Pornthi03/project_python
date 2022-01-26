from tkinter import *

#About Pepsi
#Pepsi
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def win_1_sort():
    #Pepsi_sort
    # sort screen for easy to use it 
    #-----------------------------------------------------------------
    about_pepsi.grid(row=1,column=0,padx=4,pady=4)
    inp_pepsi.grid(row=1,column=1,padx=4,pady=4)
    bt_pepsi_p.grid(row=2,column=1,padx=4,pady=5)
    bt_ok_pepsi.grid(row=3,column=0,pady=10)
    bt_close_pepsi.grid(row=3,column=1,pady=10)
    #-----------------------------------------------------------------
    
#-----------------------------------------------------------------
def process_pepsi():
    global pepsi_p ; global shw_pepsi ;global check_ok_pepsi
    global secound_p
    #-----------------------------------------------------------------
    
    check_ok_pepsi = 1
    try :
        #Check input is number ?
        int(pepsi_var.get())
        
        #Check if secound click process ..it will create new text  
        if secound_p >1:
            shw_pepsi.destroy()
        secound_p += 1
        
        #process cost
        pepsi_p = pepsi_var.get() * pepsi_rate

        #check frist screen has been destroy? if yes variable = 8 and let's repair screen  
        if check_r_pp != 8 :
            shw_pepsi = Label(win_1,text=pepsi_p,font="8")
            shw_pepsi.grid(row=2,column=0)
        else:
            repair_p_win1()
        
        
    except Exception as e:
        #if input is wrong and error another ... print for check problem
        inp_pepsi.delete(first="0",last="end")
        print("Wrong Input...")
        print(secound_p)
        print(pepsi_p)

    #-----------------------------------------------------------------

#record variable to list 
def record_pepsi():
    global check_ok_pepsi
    # try test if no variable for if it can tell user that ... No - Process !!
    try:
        #check ok button has been click? 
        if check_ok_pepsi == 1:
            lst_pepsi.append(pepsi_p)
            print("Lst_pepsi = ",lst_pepsi)
            
        #and set check = 0 because need to run process again and can click this 
        check_ok_pepsi = 0
    except Exception :
        print("No-process")

#call form main menu for use again and again 
def call_win1():
    #repair frist and sort 
    repair_win_1()
    win_1_sort


def repair_win_1 ():
    global check_ok_pepsi ; global secound_p ; global pepsi_var ; global pepsi_rate
    global check_r_pp  ; global shw_pepsi ; global inp_pepsi ;global pepsi_p ;global repair_p_win1

    #set variable's repair be 8 for process check that ... repair????
    check_r_pp = 8

    #repair screen Gui
    win_1 = Tk()
    win_1.title("Pepsi - Process")
    win_1.minsize(200,120)

    #repair variable for sure 
    pepsi_var = IntVar(win_1)
    pepsi_rate = 16

    #repair fpr record and set to defult
    
    secound_p = 0
    check_ok_pepsi = 1

    #repair gui setting
    about_pepsi = Label(win_1,text="Pepsi Process",font="8")
    inp_pepsi = Entry(win_1,textvariable = pepsi_var)
    
    bt_pepsi_p = Button(win_1,text="Process",command=process_pepsi,width=15)
    bt_close_pepsi = Button(win_1,text="Close",command=win_1.destroy,width=5)
    bt_ok_pepsi = Button(win_1,text="OK",command=record_pepsi,width=5)

    #repair sort
    about_pepsi.grid(row=1,column=0,padx=4,pady=4)
    inp_pepsi.grid(row=1,column=1,padx=4,pady=4)
    bt_pepsi_p.grid(row=2,column=1,padx=4,pady=5)
    bt_ok_pepsi.grid(row=3,column=0,pady=10)
    bt_close_pepsi.grid(row=3,column=1,pady=10)

    #repair process update variable every click process
    def repair_p_win1():
        global pepsi_p ; global shw_pepsi
        if secound_p >1:
            shw_pepsi.destroy()
        pepsi_rate = 16
        pepsi_p = pepsi_var.get() * pepsi_rate
        shw_pepsi = Label(win_1,text=pepsi_p,font="8")
        shw_pepsi.grid(row=2,column=0)

    repair_p_win1()
    
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------



#About Coke
#Coke
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def win_2_sort () :
    #Coke_sort
    #-----------------------------------------------------------------
    about_coke.grid(row=1,column=0,padx=4,pady=4)
    inp_coke.grid(row=1,column=1,padx=4,pady=4)
    bt_coke_p.grid(row=2,column=1,padx=4,pady=5)
    bt_ok_coke.grid(row=3,column=0,pady=10)
    bt_close_coke.grid(row=3,column=1,pady=10)
    #----------------------------------------------------------------- 
#-----------------------------------------------------------------
def process_coke():
    global coke_p ; global shw_coke ; global check_ok_coke
    global secound_c
    #-----------------------------------------------------------------
    check_ok_coke = 1
    try :
        int(coke_var.get())
        
        if secound_c > 1 :
            shw_coke.destroy()
        secound_c += 1

        #process cost
        coke_p = coke_var.get() * coke_rate
        
        if check_r_pc != 8 :
            shw_coke = Label(win_2,text=coke_p,font="8")
            shw_coke.grid(row=2,column=0)
        else:
            repair_p_win2()
            
    except Exception :
        inp_coke.delete(first="0",last="end")
        print("Wrong Input...")
        print(secound_p)
        print(coke_p)
        
    #-----------------------------------------------------------------
        
    
    
def record_coke() :
    global check_ok_coke
    try:
        if check_ok_coke == 1:
            lst_coke.append(coke_p)
            print("Lst_Coke = ",lst_coke)
        check_ok_coke = 0
    except Exception :
        print("No-process")

def call_win2():
    #repair frist and sort 
    repair_win_2()
    win_2_sort

def repair_win_2 ():
    global check_ok_coke ; global secound_c ; global coke_var ; global coke_rate
    global check_r_pc  ; global shw_coke ; global inp_coke ;global coke_p ;global repair_p_win2
    
    #set variable's repair be 8 for process check that ... repair????
    check_r_pc = 8

    #repair screen Gui
    win_2 = Tk()
    win_2.title("Coke-Process")
    win_2.minsize(200,120)

    #repair variable for sure 
    coke_var = IntVar(win_2)
    coke_rate = 14

    #repair fpr record and set to defult
    
    secound_c = 0
    check_ok_coke = 1

    #repair gui setting
    about_coke = Label(win_2,text="Coke Process",font="8")
    inp_coke = Entry(win_2,textvariable = coke_var)

    bt_coke_p = Button(win_2,text="Process" ,command = process_coke , width=15)
    bt_close_coke = Button (win_2,text="Close",command=win_2.destroy,width=5)
    bt_ok_coke = Button (win_2,text="OK",command = record_coke,width=5)

    #repair sort
    about_coke.grid(row=1,column=0,padx=4,pady=4)
    inp_coke.grid(row=1,column=1,padx=4,pady=4)
    bt_coke_p.grid(row=2,column=1,padx=4,pady=5)
    bt_ok_coke.grid(row=3,column=0,pady=10)
    bt_close_coke.grid(row=3,column=1,pady=10)

    #repair process update variable every click process
    def repair_p_win2():
        global coke_p ; global shw_coke
        if secound_c >1:
            shw_coke.destroy()
        coke_rate = 14
        coke_p = coke_var.get() * coke_rate
        shw_coke = Label(win_2,text=coke_p,font="8")
        shw_coke.grid(row=2,column=0)

    repair_p_win2()
    
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------




#About Est
#Est
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def win_3_sort():
    #Est_sort
    #-----------------------------------------------------------------
    about_est.grid(row=1,column=0,padx=4,pady=4)
    inp_est.grid(row=1,column=1,padx=4,pady=4)
    bt_est_p.grid(row=2,column=1,padx=4,pady=5)
    bt_ok_est.grid(row=3,column=0,pady=10)
    bt_close_est.grid(row=3,column=1,pady=10)
    #-----------------------------------------------------------------

def process_est():
    global est_p ; global shw_est ; global check_ok_est
    global secound_e
    #-----------------------------------------------------------------
    check_ok_est = 1
    try :
        int(est_var.get())
        
        if secound_e > 1 :
            shw_est.destroy()
        secound_e += 1

        #process cost
        est_p = est_var.get() * est_rate

        if check_r_pe != 8 :
            shw_est = Label(win_3,text=est_p,font="8")
            shw_est.grid(row=2,column=0)
        else:
            repair_p_win3()
            
    except Exception :
        inp_est.delete(first="0",last="end")
        print("Wrong Input...")
        print(secound_e)
        print(est_p)
        
def record_est() :
    global check_ok_est
    try:
        if check_ok_est == 1:
            lst_est.append(est_p)
            print("Lst_est = ",lst_est)
        check_ok_est = 0
    except Exception :
        print("No-process")

def call_win3():
    #repair frist and sort 
    repair_win_3()
    win_3_sort

    
def repair_win_3 ():
    global check_ok_est ; global secound_e ; global est_var ; global est_rate
    global check_r_pe  ; global shw_est ; global inp_est ;global est_p ;global repair_p_win3
    
    #set variable's repair be 8 for process check that ... repair????
    check_r_pe = 8

    #repair screen Gui
    win_3 = Tk()
    win_3.title("Est-Process")
    win_3.minsize(200,120)

    #repair variable for sure 
    est_var = IntVar(win_3)
    est_rate = 12

    #repair fpr record and set to defult
    
    secound_e = 0
    check_ok_est = 1

    #repair gui setting
    about_est = Label(win_3,text="Est Process",font="8")
    inp_est = Entry(win_3,textvariable = est_var)

    bt_est_p = Button(win_3,text="Process" ,command = process_est , width=15)
    bt_close_est = Button (win_3,text="Close",command=win_3.destroy,width=5)
    bt_ok_est = Button (win_3,text="OK",command = record_est,width=5)

    #repair sort
    about_est.grid(row=1,column=0,padx=4,pady=4)
    inp_est.grid(row=1,column=1,padx=4,pady=4)
    bt_est_p.grid(row=2,column=1,padx=4,pady=5)
    bt_ok_est.grid(row=3,column=0,pady=10)
    bt_close_est.grid(row=3,column=1,pady=10)

    #repair process update variable every click process
    def repair_p_win3():
        global est_p ; global shw_est
        if secound_e >1:
            shw_est.destroy()
        est_rate = 12
        est_p = est_var.get() * est_rate
        shw_est = Label(win_3,text=est_p,font="8")
        shw_est.grid(row=2,column=0)

    repair_p_win3()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------



#variable
#-----------------------------------------------------
#GUI
#-------------------------------
#Option
#----------------------
win = Tk()
win.title("P&N STORE")
win.minsize(460,460)


win_1 = Tk()
win_1.title("Pepsi - Process")
win_1.minsize(200,120)



win_2 = Tk()
win_2.title("Coke-Process")
win_2.minsize(200,120)

win_3 = Tk()
win_3.title("Est-Process")
win_3.minsize(200,120)

#------------------------------------------------------

#Pepsi
#--------------------
pepsi_var = IntVar(win_1)
pepsi_rate = 16
#--------------------
#Coke
#--------------------
coke_var = IntVar(win_2)
coke_rate = 14
#--------------------
#Est
#--------------------
est_var = IntVar(win_3)
est_rate = 12
#--------------------

#------------------------------------------------------


#Pepsi-variable 
#----------------------------------------***
lst_pepsi = []
secound_p = 1
about_pepsi = Label(win_1,text="Pepsi Process",font="8")
inp_pepsi = Entry(win_1,textvariable = pepsi_var)

bt_pepsi_p = Button(win_1,text="Process",command=process_pepsi,width=15)
bt_close_pepsi = Button(win_1,text="Close",command=win_1.destroy,width=5)
bt_ok_pepsi = Button(win_1,text="OK",command=record_pepsi,width=5)

#frist screen need to hide 
win_1.destroy()
#----------------------------------------***

#Coke-variable
#----------------------------------------***
lst_coke = []
secound_c = 1
about_coke = Label(win_2,text="Coke Process",font="8")
inp_coke = Entry(win_2,textvariable = coke_var)

bt_coke_p = Button(win_2,text="Process" ,command = process_coke , width=15)
bt_close_coke = Button (win_2,text="Close",command=win_2.destroy,width=5)
bt_ok_coke = Button (win_2,text="OK",command = record_coke,width=5)

#frist screen need to hide 
win_2.destroy()
#----------------------------------------***

#Est-variable
#----------------------------------------***
lst_est = []
secound_e = 1
about_est = Label(win_3,text="Est Process",font="8")
inp_est = Entry(win_3,textvariable = est_var)

bt_est_p = Button(win_3,text="Process" ,command = process_est , width=15)
bt_close_est = Button (win_3,text="Close",command=win_3.destroy,width=5)
bt_ok_est = Button (win_3,text="OK",command = record_est,width=5)

#frist screen need to hide 
win_3.destroy()
#----------------------------------------***


    
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def clear_data_day ():
    global lst_pepsi ; global lst_coke ; global lst_est
    lst_pepsi = []
    lst_coke=[]
    lst_est=[]
    print("----------------------------------------------")
    print("Clear lst_pepsi = ",lst_pepsi)
    print("Clear lst_coke = ",lst_coke)
    print("Clear lst_est = ",lst_est)
    print("----------------------------------------------")


checker = 1     
def saver_day ():
    global checker ;global shw_recorder_day ; global shw_recorder_sday ; global s_lst_day
    lst_day = []
    lst_day.append(sum(lst_pepsi))
    lst_day.append(sum(lst_coke))
    lst_day.append(sum(lst_est))
    s_lst_day = sum(lst_day)
    
    print("----------------------------------------------")
    print("adder - lst_day [ Pepsi , Coke , Est ]= ",lst_day)
    print("checker = ",checker)
    print("----------------------------------------------")
    
    if checker > 1 :
        shw_recorder_day.destroy()
        shw_recorder_sday.destroy()
        checker=1
        
    shw_recorder_day =Label(win,text=("Record-Day [ Pepsi , Coke , Est ] = "+str(lst_day)))
    shw_recorder_day.grid(row=7,column=0,padx=8,pady=5,sticky=W)
    
    shw_recorder_sday = Label(win,text=("Total - Day = "+str(s_lst_day)))
    shw_recorder_sday.grid(row=8,column=0,padx=8,pady=5,sticky=W)
    checker +=1

    bt_save_w = Button (win,text="Record",command=saver_week,font="8",width=20).grid(row=4,column=1,padx=4)
    bt_reader_record = Button (win,text="Read Record",font="8",width=20).grid(row=5,column=1,padx=4)


    return lst_day
def saver_week ():
    global lst_week ;global lst_month 
    if len(lst_week) < 7 :
        lst_week.append(s_lst_day)
        
        
        print("lst_week = ",lst_week)
    if len(lst_week) == 7 :
        lst_month.append(sum(lst_week))
        print("lst_month = ",lst_month)
        
        
        lst_week = []
        saver_month()
    read_record()
    

def saver_month():
    global recorder_m ; global lst_month ; global lst_week ;global recorder_m
    try:
        if len(lst_month)==4:
            print("sum month = ",sum(lst_month))
            recorder_m.append(sum(lst_month))
            print("recoder_m =",recorder_m)
            lst_month = []
        if len(lst_month)>12:
            lst_month= []
            lst_week = []
    except Exception as e :
        print(e)
            
checkrr = 1
def read_record():
    global checkrr ;global shw_lst_w  ; global shw_lst_m 
    if checkrr >1:
        shw_lst_w.destroy()
        shw_lst_m.destroy()
       
        checkrr = 1
        
    shw_lst_w = Label(win,text="Record week :"+str(lst_week))
    shw_lst_w.grid(row=7,column=1,sticky=W)
    

    
    shw_lst_m = Label(win,text="Record month "+str(lst_month))
    shw_lst_m.grid(row=8,column=1,sticky=W)
    
    checkrr += 1
        
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------   
#lst total
lst_week = []
lst_month = []

recorder_d = []
recorder_w = [] 
recorder_m = []
#main Menu
#------------------------------------------------------

bt_coke_call = Button(win,text="Coke-call",command=call_win2,font="18",width=20)   .grid(row=1,column=0,padx=6,pady=6)
bt_pepsi_call = Button(win,text="Pepsi-call",command=call_win1,font="18",width=20) .grid(row=2,column=0,padx=6,pady=6)
bt_est_call = Button(win,text="Est-call",command=call_win3,font="18",width=20)     .grid(row=3,column=0,padx=6,pady=6)


bt_clear = Button (win,text="Clear Data /day",command=clear_data_day,font="18",width=20).grid(row=4,column=0,padx=12)#------------------------------------------------------
bt_save = Button (win,text="Save - Record /day",command=saver_day,font="18",width=20,height=2).grid(row=5,column=0,padx=12,pady=4.5)

