#Samuel Reyes 8/20/2022
from tkinter import *

gui = Tk(className='matrix algebra calculator')
gui.configure(background="light blue")
gui .geometry("500x500")


def split(lst,n):
    return [lst[i::n] for i in range(n)]
#ALGEBRA SELECTOR FUNCTION
selected="new"


def m_select():
    global selected
    if selected=="new" or selected=="mult":
        selected="mult"
        mult_button.config(highlightbackground = "red", highlightcolor= "red")
        response.configure(text="Multiplication selected",fg="blue")
    else:
        sub_button.config(highlightbackground = "white", highlightcolor= "white")
        add_button.config(highlightbackground = "white", highlightcolor= "white")
        selected="mult"
        mult_button.config(highlightbackground = "red", highlightcolor= "red")
        response.configure(text="Multiplication selected",fg="blue")
def a_select():
    global selected
    if selected=="new" or selected=="add":
        selected="add"
        add_button.config(highlightbackground = "red", highlightcolor= "red")
        response.configure(text="Addition selected",fg="blue")
    else:
        sub_button.config(highlightbackground = "white", highlightcolor= "white")
        mult_button.config(highlightbackground = "white", highlightcolor= "white")
        selected="add"
        add_button.config(highlightbackground = "red", highlightcolor= "red")
        response.configure(text="Addition selected",fg="blue")

def s_select():
    global selected
    if selected=="new" or selected=="sub":
        selected="sub"
        sub_button.config(highlightbackground = "red", highlightcolor= "red")
        response.configure(text="Subtraction selected",fg="blue")
    else:
        mult_button.config(highlightbackground = "white", highlightcolor= "white")
        add_button.config(highlightbackground = "white", highlightcolor= "white")
        selected="sub"
        sub_button.config(highlightbackground = "red", highlightcolor= "red")
        response.configure(text="Subtraction selected",fg="blue")


#TYPE OF ALGEBRA SELECTOR
mult_button = Button(gui, text="Multiply [A*B]  ",highlightthickness=2,command=m_select,fg='black')
mult_button.grid(row=51, column=1)

add_button = Button(gui, text= "Addition [A+B] ",command=a_select,fg='black')
add_button.grid(row=52, column=1)

sub_button = Button(gui, text="Subtract [A-B] ",command=s_select,fg='black')
sub_button.grid(row=50, column=1)

#user input feedback label
response= Label(gui,text="",bg="light blue",fg="red")
response.grid(row=25,column=1,sticky=W+E)
response.configure(text="Select Operation !",fg="blue",font=('calibri',9))
#user input gate
#Function used when grids are filled out
def check():
    matrix_a_nums=[]
    matrix_b_nums=[]
    matrix_c_nums=[]
    response2= Label(gui,text="",bg="light blue",fg="red")
    response2.grid(row=100,column=100)
    
    #multiplication method
    if selected=="mult":
        try:
            for x in matrix_A_list:
                matrix_a_nums.append(int(x.get()))
            
            for x in matrix_B_list:
                matrix_b_nums.append(int(x.get()))
            print("matrix a")
            print(matrix_a_nums)
            print("matrix b")
            print(matrix_b_nums)
            print("done")
            #add matrixes 
            #for i in range(len(matrix_a_nums)):
              #  matrix_c_nums.append(matrix_a_nums[i]+matrix_b_nums[i])
            #print("matrix c")
            #print(matrix_c_nums)
           # clear()
            n=lenA
            
            organized_A_matrix= [matrix_a_nums[i::n] for i in range(n)]
            
            print("organized a matrix")
            print(organized_A_matrix)
            organized_B_matrix=[]
            
            h=0
            while h < witB*lenB:
                organized_B_matrix.append(matrix_b_nums[h:h+lenB])
                h+=lenB
            print("organized matrix b")
            print(organized_B_matrix)
            
            
            mult_matrix=[]
           
            for x in organized_A_matrix:
                for y in organized_B_matrix:
                    s=0
                    for _ in range(witA):
                        mult_matrix.append(x[s]*y[s])
                        s+=1
            print("multi matrix")
            print(mult_matrix)
            print("length")
            print(len(mult_matrix))


            finalmatrix=[]
            h=0
            
            index=0
            

            print(lenA)
            print(witA)
            print(lenB)
            print(witB)
            if lenA ==1 or witB==1:
                while h < witB*witA:
                    finalmatrix.append(mult_matrix[index:index+lenB])
                    index+=lenB
                    h+=1
            if lenA > 1 or lenB>1:

                while h < pow(lenA,lenB):
                    finalmatrix.append(mult_matrix[index:index+lenB])
                    index+=lenB
                    h+=1
            finalmatrix2=[]
            for x in finalmatrix:
                finalmatrix2.append(sum(x))


            print('final')
            print(finalmatrix)
            print("final 2")
            print(finalmatrix2)
            organized_final_matrix=[]
            
            e=0
            
            while e < lenA*witB:
                organized_final_matrix.append(finalmatrix2[e:e+witB])
                e+=witB
            clear()
            print("org final")
            print(organized_final_matrix)
            for x in organized_final_matrix:
                Label (gui,bg="white",text=x,fg="black",height="1",borderwidth=3,relief="solid",width="15",font=("Times New Roman", 20)).pack()
            


           
            
            #for x in organized_B_matrix:
              
              #  Label (gui,bg="white",text=x,fg="black",height="1",width="10",font=("Times New Roman", 20)).pack()
            


          #  print(*organized_B_matrix,sep='\n')

            
            #print("deconstructed list")
            #print(biglist)
            #Label (gui,bg="white",text=organizedmatrix,fg="black",height="50",width="50",font="none 12 bold").place(relx=0.5, rely=0.5, anchor=CENTER)
            
        except:
            response2.configure(text="all values must be integers")
   
    
    
    #adding function
    if selected=="add":
        try:
            for x in matrix_A_list:
                matrix_a_nums.append(int(x.get()))
            
            for x in matrix_B_list:
                matrix_b_nums.append(int(x.get()))
            print("matrix a")
            print(matrix_a_nums)
            print("matrix b")
            print(matrix_b_nums)
            #add matrixes 
            for i in range(len(matrix_a_nums)):
                matrix_c_nums.append(matrix_a_nums[i]+matrix_b_nums[i])
            print("matrix c")
            print(matrix_c_nums)
            clear()
            

            print(lenA)
            print(witA)
            print(lenB)
            print(witB)
            
            

            organizedmatrix= [matrix_c_nums[i::lenA] for i in range(lenA)]
            
            for x in organizedmatrix:
                
                Label (gui,bg="white",text=x,fg="black",height="1",borderwidth=3,relief="solid",width="15",font=("Times New Roman", 20)).pack()
            
            print("org matrix")
            print(organizedmatrix)

            
            print(*organizedmatrix,sep='\n')

            
            #print("deconstructed list")
            #print(biglist)
            #Label (gui,bg="white",text=organizedmatrix,fg="black",height="50",width="50",font="none 12 bold").place(relx=0.5, rely=0.5, anchor=CENTER)
            
        except:
            response2.configure(text="all values must be integers")
   
   #SUBTRACT METHOD
    
    if selected=="sub":
        try:
            for x in matrix_A_list:
                matrix_a_nums.append(int(x.get()))
            
            for x in matrix_B_list:
                matrix_b_nums.append(int(x.get()))
            print("matrix a")
            print(matrix_a_nums)
            print("matrix b")
            print(matrix_b_nums)
            #add matrixes 
            for i in range(len(matrix_a_nums)):
                matrix_c_nums.append(matrix_a_nums[i]-matrix_b_nums[i])
            print("matrix c")
            print(matrix_c_nums)
            clear()
            n=witA
            
            organizedmatrix= [matrix_c_nums[i::n] for i in range(n)]
            
            for x in organizedmatrix:
                
                Label (gui,bg="white",text=x,fg="black",height="1",borderwidth=3,relief="solid",width="15",font=("Times New Roman", 20)).pack()
            


            print(*organizedmatrix,sep='\n')

            
            #print("deconstructed list")
            #print(biglist)
            #Label (gui,bg="white",text=organizedmatrix,fg="black",height="50",width="50",font="none 12 bold").place(relx=0.5, rely=0.5, anchor=CENTER)
            
        except:
            response2.configure(text="all values must be integers")
            



#checks if all user inputs are integers excluding 0/ command when 1st submit is clicked
def numbercheck():
    try: 
       #Valid integer gate
        int(matrix_A_length.get())
        int(matrix_A_width.get())
        int(matrix_B_length.get())
        int(matrix_B_width.get())
        #Non zero gate
        1/int(matrix_A_length.get())
        1/int(matrix_A_width.get())
        1/int(matrix_B_length.get())
        1/int(matrix_B_width.get())
        
        #Non negative gate
        if int(matrix_A_length.get())<0 or int(matrix_B_length.get()) <0 or int(matrix_B_width.get()) < 0 or int(matrix_A_width.get()) < 0:
            response.configure(text="all values must be positive integers",fg="red")
            return

        #Max input of 15 gate
        if int(matrix_A_length.get())>15 or int(matrix_B_length.get()) >15 or int(matrix_B_width.get()) > 15 or int(matrix_A_width.get())> 15:
            response.configure(text="15 is max input",fg='red')
            return



        #operation selected gate

        if selected=="new":
            response.configure(text="Select option",fg='red')
            return

        # correct inputs for matrix multiplication gate
        if selected=="mult" and int(matrix_A_width.get())!= int(matrix_B_length.get()):
            response.configure(text="Matrix A column and B row amount need to be the same.",fg='red')
            return
        
         # correct inputs for matrix addition and subtraction gate
        if (selected=="add" or selected=="sub")  and int(matrix_A_length.get())!= int(matrix_B_length.get()):
            response.configure(text="Matrix A and B need to be the same in size.",fg='red')
            return
        if (selected=="add" or selected=="sub")  and int(matrix_A_width.get())!= int(matrix_B_width.get()):
            response.configure(text="Matrix A and B need to be the same in size.",fg='red')
            return
        
        
        response.configure(text="good input")
        graph()
        #print(selected)
    except:
        # bad input/ non integer gate
        response.configure(text="all values must be positive integers",fg="red")
        




#clears the screen

def clear():
    for widget in gui.winfo_children():
        widget.destroy()

 #Function which changes screen when submit is clicked and user input is verified/ called on by numcheck
   
def graph():    
    
    global lenA
    global witA
    global witB
    global lenB

    entered_matrixA_length=int(matrix_A_length.get())
    entered_matrixA_width = int(matrix_A_width.get())
    entered_matrixB_length =int(matrix_B_length.get())
    entered_matrixB_width = int(matrix_B_width.get())
   
    #for grid only
    entered_matrixA_length2=int(matrix_A_width.get())
    entered_matrixA_width2 = int(matrix_A_length.get())
    entered_matrixB_length2 =int(matrix_B_width.get())
    entered_matrixB_width2 = int(matrix_B_length.get())
   
    lenA = entered_matrixA_length
    witA= entered_matrixA_width
    lenB = entered_matrixB_length
    witB= entered_matrixB_width
    
    
    
    for widget in gui.winfo_children():
        widget.destroy()
    

#MATRIX A GRID FORMATION
    
    initial=0
    while initial< entered_matrixA_length2:
        A_length=Entry(gui,highlightthickness=2,width=1,bg="white")
        A_length.config(highlightbackground = "blue", highlightcolor= "blue")
        A_length.grid(row=1, column=1+initial,sticky=E)
        holder=1+initial
        principle=entered_matrixA_width2
        increment=1
        matrix_A_list.append(A_length)
        while principle>1:
            A_width=Entry(gui,highlightthickness=2,width=1,bg="white")
            A_width.config(highlightbackground = "blue", highlightcolor= "blue")
            A_width.grid(row=increment+1, column=holder,sticky=W)
            increment+=1
            principle-=1
            matrix_A_list.append(A_width)
           # print(q)
        initial+=1
    #print(matrix_A_list)
    wallwidth=max(entered_matrixB_width2,entered_matrixA_width2)
#LABEL WALL
    Label (gui,bg="light blue",fg="black",height="5",width="1",font="none 12 bold").grid(row=entered_matrixA_width2+1, column=1,sticky=E)
    #Label (gui,bg="black",fg="black",height="50",width="1",font="none 12 bold").grid( row=0,column=wallwidth+20,sticky=E)
    #ll=Entry(gui,highlightthickness=2,width=1,bg="white")
    #ll.config(highlightbackground = "red", highlightcolor= "red")
    #ll.grid(row=1000, column=1)
    #11.pack(expand=True)
    
#MATRIX B GRID FORMATION
    
    initial2=0
    while initial2< entered_matrixB_length2:
        B_length=Entry(gui,highlightthickness=2,width=1,bg="white")
        B_length.config(highlightbackground = "red", highlightcolor= "red")
        B_length.grid(row=50, column=1+initial2,sticky=E)
        holder2=1+initial2
        principle2=entered_matrixB_width2
        increment2=1
        matrix_B_list.append(B_length)
        while principle2>1:
            B_width=Entry(gui,highlightthickness=2,width=1,bg="white")
            B_width.config(highlightbackground = "red", highlightcolor= "red")
            B_width.grid(row=50+increment2, column=holder2,sticky=W)
            increment2+=1
            principle2-=1
           # print(q)
            matrix_B_list.append(B_width)
        initial2+=1
    #NEW GRID LABELS
    Label (gui,text="fill in matrix [A]",bg="light blue",fg="blue",font="none 12 bold").grid(row=1,column=wallwidth+4,sticky=NE)
    Label (gui,text="fill in matrix [B]",bg="light blue",fg="red",font="none 12 bold").grid(row=1,column=wallwidth+5,sticky=NE)
    # NEW SUBMIT BUTTON
    submit_button2 = Button(gui, text="",command=check,fg='black')

    submit_button2.config(highlightbackground="green",highlightcolor="green")
    submit_button2.grid(row=1,column=wallwidth+6,sticky=NE)
    if selected=='mult':
        submit_button2.config(text="click for [A*B]")
    if selected=='add':
        submit_button2.config(text="click for [A+B]")
    if selected=='sub':
        submit_button2.config(text="click for [A-B]")



matrix_A_list=[]
matrix_B_list=[]
#MATRIX A INPUT
Label (gui,text="enter matrix [A] length x width:",bg="light blue",fg="black",font="none 12 bold").grid(row=1, column=1,sticky=E)
#Label (gui,text="x",bg="light blue",fg="black",font="none 12 bold").grid(row=2, column=2,sticky=W)
#Label (gui,text="enter matrix [A] length x width:",bg="light blue",fg="black",font="none 12 bold").grid(row=1, column=1, sticky=W)
matrix_A_length=Entry(gui,width=2,bg="white")
lenA=0
witA=0
witB=0
lenB=0
matrix_A_length.grid(row=2, column=1, sticky=E)
Label (gui,text="x",bg="light blue",fg="black",font="none 12 bold").grid(row=2, column=2,sticky=E)
matrix_A_width=Entry(gui,width=2,bg="white")
matrix_A_width.grid(row=2, column=3, sticky=E)


#Matrix B INPUT
Label (gui,text="enter matrix [B] length x width:",bg="light blue",fg="black",font="none 12 bold").grid(row=5, column=1,sticky=E)
#Label (gui,text="x",bg="light blue",fg="black",font="none 12 bold").grid(row=2, column=2,sticky=W)
#Label (gui,text="enter matrix [A] length x width:",bg="light blue",fg="black",font="none 12 bold").grid(row=1, column=1, sticky=W)
matrix_B_length=Entry(gui,width=2,bg="white")
matrix_B_length.grid(row=6, column=1, sticky=E)
Label (gui,text="x",bg="light blue",fg="black",font="none 12 bold").grid(row=6, column=2,sticky=E)
matrix_B_width=Entry(gui,width=2,bg="white")
matrix_B_width.grid(row=6, column=3, sticky=E)

#SUBMIT BUTTON
submit_button = Button(gui, text="Submit",command=numbercheck,fg='green')

submit_button.config(highlightbackground="green",highlightcolor="green")
submit_button.grid(row=10, column=10,sticky=W+S)


#EXIT BUTTON
#exit_button = Button(gui, text="Exit", command=gui.destroy)
#exit_button.grid(row=0, column=9,sticky=W)
#exit_button.pack(side="top",anchor="nw")

gui.mainloop()