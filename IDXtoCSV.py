import pandas as pd 
import csv
import os


def IdxtoCsv(filename):
    indexfile = pd.read_table(filename,skiprows=4,index_col=0,encoding = "ISO-8859-1")
    index_content = indexfile.index
    list_content = list(index_content)
    del list_content[1]
    data = pd.DataFrame({list_content[0]: list_content[1:]})

    # dropping null value columns to avoid errors 
    data.dropna(inplace = True) 
    # new data frame with split value columns 
    new = data[list_content[0]].str.split("|", n = 0, expand = True) 
    data["CIK"]= new[0] 
    data["Company Name"]= new[1] 
    data["Form Type"]= new[2] 
    data["Date Filed"]= new[3]
    data["Filename"]= new[4]
    # Dropping old Name columns 
    data.drop(columns =[list_content[0]], inplace = True) 

    filename = filename.replace('.idx','')
    data.to_csv(filename +'.csv', index = False)


if __name__ == '__main__':
    for file_path,sub_dirs,files in os.walk(r"C:\Users\CH.4644\Downloads"):
        for file_name in files:
            print(file_name) 
            IdxtoCsv(file_name)

         






