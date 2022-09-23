class matrix_data:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def addition (self,other):
        if ((len(self.matrix) != len(other)) or (len(self.matrix[0]) != len(other[0]))):
            return ("The two matrix cannot be added as the two matrix have different order")
        else :
            res = []
            for i in range(len(self.matrix)):
                res.append([])
                for j in range(len(self.matrix[0])):
                    res[i].append(self.matrix[i][j] + other[i][j] )
            return res  
    def subtraction (self,other):
        if ((len(self.matrix) != len(other)) or (len(self.matrix[0]) != len(other[0]))):
            return ("The two matrix cannot be subtracted as the two matrix have different order")
        else :
            res = []
            for i in range(len(self.matrix)):
                res.append([])
                for j in range(len(self.matrix[0])):
                    res[i].append(self.matrix[i][j] - other[i][j] )
            return res  
    def Multiplication(self,other):
        if ((len(self.matrix[0]) != len(other))):
            return ("The two matrix cannot be multiplied as the two matrix don't have proper multiplying property of order")
        else :
            res = []
            for i in range(len(self.matrix)):
                res.append([])
                for j in range(len(other[0])):
                    res[i].append(0)
                    for k in range(len(other)):
                        res[i][j] += (self.matrix[i][k] * other[k][j] )    
            return res            
    def transpose (self):
        res = []
        for j in range(len(self.matrix[0])):
            res.append([])
            for i in range(len(self.matrix)):
                res[j].append(self.matrix[i][j])
        return res            
        
        
    def get_list(self):
        return self.matrix  
    
          
def show_matrix (net_list):
    for i in range(len(net_list)):
        res = ""
        for j in range(len(net_list[i])):
            res += str(net_list[i][j]) + " "
        print(res)
        
        
while (1>0):
    print("========================================================")
    menu = int(input("Enter the menu option you want to select\n1)Enter the data\n0)Exit\n"))
    if(menu== 0):
        break
    elif (menu == 1):
        temp = []
        print("Enter the data of first matrix \nEnter the number of data of matrix spaced separated and press enter to go on the next row \nPress enter and leave a blank column when done\n")        
        while (1>0):
            try:
                temp.append(list(map(int,input().split())))
            except:
                print("An exception occurred")
                break
            if (len(temp[len(temp)-1])==0):
                temp.pop()
                break    
        m1 = matrix_data(temp)   
        temp = []
        print("Enter the data of second matrix \nEnter the number of data of matrix spaced separated and press enter to go on the next row \nType D when done with entering data\n")        
        while (1>0):
            temp.append(list(map(int,input().split())))
            if (len(temp[len(temp)-1])==0):
                temp.pop()
                break    
        m2 = matrix_data(temp)
        while(1>0):
            print("========================================================")
            menu1=int(input("\nEnter the menu choice you want to perform \n1)Addition of the two matrix\n2)Subtraction of the two matrix\n3)Multiplication of the two matrix\n4)Transpose of a matrix\n0)Return to main menu / Change the string\n"))
            print("========================================================")
            if(menu1 == 0):
                break
            elif(menu1==1):
                temp1 =  m2.get_list() 
                show_matrix(m1.addition(temp1))
            elif(menu1==2):
                temp1 =  m2.get_list() 
                show_matrix(m1.subtraction(temp1))    
            elif(menu1==3):
                temp1 =  m2.get_list() 
                show_matrix(m1.Multiplication(temp1))    
            elif(menu1==4):
                menu2=int(input("Enter 1 if you want transpose of matrix 1 and 2 for matrix 2"))
                if(menu2 == 1):
                    show_matrix(m1.transpose())
                elif (menu2 == 2):
                    show_matrix(m2.transpose())
                else:
                    print("Enter valid input so please try again")             
            
