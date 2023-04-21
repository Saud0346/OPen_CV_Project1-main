import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('C:/Users/sauds/Desktop/OPen_CV_Project1-main/Students_Data.csv')
#s_data = pd.DataFrame(data, columns=['Name,', 'Reg Number', 'Time IN', 'Date IN', 'Time OUT', 'Date OUT', 'Batch', 'Faculty'])


#This function shows all the details of a student 
def a_student_details():
 
     data_frame =  data.groupby(['Reg Number','Name'])['Time IN','Date IN','Time OUT','Date OUT','Batch','Faculty']
     total_count_in = data_frame.count() 
     
     name = input("Enter Reg Number of a student ")
     total_count_in.loc[int(name)].plot(kind='bar')
     
    
def batch_details():
    data_frame = data.groupby(['Batch'])['Time IN','Date IN','Time OUT','Date OUT','Faculty']
    total_count_in = data_frame.count() 
    
    name = input("Enter Batch ")
    total_count_in.loc[int(name)].plot(kind='bar',color ='green')
    

def faculty_details():
    data_frame = data.groupby(['Faculty'])['Time IN','Date IN','Time OUT','Date OUT']
    total_count_in = data_frame.count() 
    
    name = input("Enter faculty ")
    total_count_in.loc[name].plot(kind='bar',color ='purple')
    
    