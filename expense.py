import csv
import matplotlib.pyplot as plt
import os
data=[]
fields=[]
rows=[]
dict={"1":0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
Dict={"Shopping":0,"Travel":0,"Medical":0,"Food":0,"Entertainment":0,"Necessities":0,"Others":0}


#Adding expenses into a csv file.
def add_inform(name):
  current_date=input("Enter the date(01-01-2024)")
  print("---List of the categories---")
  categories=["Shopping","Travel","Medical","Food","Entertainment","Necessities","Others"]
  for cat in range(0,len(categories)):
    print(f"*** {categories[cat]} *** ")
  print(f"Hello {name}, Choose any category where you spend the money")
  ch=input("Enter the category name from above the list").lower()
  exp1,exp2,exp3,exp4,exp5,exp6,exp7=0,0,0,0,0,0,0
  if ch =="shopping":
    exp1=float(input("Enter the amt"))
    desc=input("give a brief description:")
  elif ch=="travel":
    exp2=float(input("Enter the amt"))
    desc=input("give a brief description:")
  elif ch=="medical":
    exp3=float(input("Enter the amt"))
    desc=input("give a brief description:")
  elif ch=="food":
    exp4=float(input("Enter the amt"))
    desc=input("give a brief description:")
  elif ch=="entertainment":
    exp5=float(input("Enter the amt"))
    desc=input("give a brief description:")
  elif ch=="necessities":
    exp6=float(input("Enter the amt"))
    desc=input("give a brief description:")
  else:
    exp7=float(input("Enter the amt"))
    desc=input("give a brief description:")
  data={"Date":current_date,"shopping":exp1,"Travel":exp2,"Medical":exp3,"Food":exp4,"Entertainment":exp5,"Necessities":exp6,"Others":exp7,"Brief description":desc}
  return data


#Create csv file for storing expenses.
def create_csv_file(filename,headers):
    with open(filename,'w') as csvfile:
    #Write headers
        csvfile.write(','.join(headers)+ '\n')
        return csvfile



#Append expenses on a daily basis.
def append_data_to_csv(file, data):
  with open(file, 'a') as csvfile:
    # Convert data to string and write to file
    csvfile.write(','.join(str(value) for value in data.values()) + '\n')
    




# Extract rows from expense recordfile.
def extract_records(filename):
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting field names through first row
        fields = next(csvreader)
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
     
    return rows        
 


# Calculate month wise expenses.
def month_wise(rows,dict):
    for i in range(0,len(rows)):
        d=rows[i][0].split('-')
        month=int(d[1])
        for j in range(1,13):
            if j==month:
                j=str(j)
                dict[j]+=float(rows[i][1])+float(rows[i][2])+float(rows[i][3])+float(rows[i][4])+float(rows[i][5])+float(rows[i][6])+float(rows[i][7])
            
    return dict


#Calculate category wise expenses.
def category_wise(rows,Dict):
    for k in range(0,len(rows)):
        Dict["Shopping"]+=float(rows[k][1])
        Dict["Travel"]+=float(rows[k][2])
        Dict["Medical"]+=float(rows[k][3])
        Dict["Food"]+=float(rows[k][4])
        Dict["Entertainment"]+=float(rows[k][5])
        Dict["Necessities"]+=float(rows[k][6])
        Dict["Others"]+=float(rows[k][7])

    return Dict






#main function   
def main():
   
    print("Welcome to the expense tracker")
    name=input("Enter your name:")
    print("Choose option 1 to 3:")
    print("Adding Expenses : 1 ")
    print("Visualize monthly wise expenditure : 2")
    print("Visualize Category Wise expenditure : 3")
    user_input=int(input("Enter the choice option"))
    x=1
    while x==1:
        if user_input==1:
            flag=1
            while flag==1: 
               try:
                  path="./Data.csv"
                  check_file=os.path.isfile(path)
                  if check_file:
                    print("File is available.")
                    file_path=path
                    Data=add_inform(name)
                    append_data_to_csv(file_path,Data)
                    print("Do you want to add more expenses? Y/N")
                    user=input().upper()
                    if user=="Y":
                      flag=1
                    else:
                      flag=0
                  else:
                    raise Exception("File is  not available")
               except:
                    path=os.getcwd()
                    filename=path+"\Data.csv"
                    filename=str(filename)
                    headers=["Date","shopping","Travel","Medical","Food","Entertainment","Necessities","Others","Brief description"]
                    print("Creating Information.csv")
                    create_csv_file(filename,headers)        
        elif user_input==2:
            filename='./Data.csv'
            records=extract_records(filename)    
            d=month_wise(records,dict)
            labels=list(d.keys())
            values=list(d.values())
            plt.bar(labels, values)
            plt.xlabel('Months')
            plt.ylabel('Values')
            plt.title('**Monthly Wise Expenses**')
            plt.show()
        else:
            filename="./Data.csv"
            records=extract_records(filename)       
            D=category_wise(records,Dict)
            labels=list(D.keys())
            values=list(D.values())
            plt.bar(labels,values)
            plt.xlabel("Categories")
            plt.ylabel("Values")
            plt.title("**Category Wise Expenses**")
            plt.show()

        print("Do you want to exit?Y/N")
        user=input("Enter input:")
        if user=='Y':
            x=0
        else:
            x=1   
            print("Adding Expenses : 1 ")
            print("Visualize monthly wise expenditure : 2")
            print("Visualize Category Wise expenditure : 3")
            user_input=int(input("Enter your choose option"))
main()

