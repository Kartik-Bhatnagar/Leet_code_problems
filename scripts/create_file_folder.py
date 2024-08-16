#this code helps to create the Folder and 2 empty files inside the new folder
#all folder will be created under the problem level category
#folder name : <problem_number>_<problem_title>
#file1 : <problem_category>_<problem_number>_<problem_title>.txt
#file2: <problem_category>_<problem_number>_<problem_title>.py
#    #file2 inital line will contain particular tags including the Author name, date created, url of the problem desciption

import os
file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
os.chdir(dir_path)
from datetime import date
import sys
class Problem():
    def __init__(self) -> None:
        self.problem_category = {"0":"Easy","1":"Medium","2":"Hard"}#new problem folder will be placed under these folder names
        self.take_input()
        self.create_problem_folder()
        self.create_problem_txt_file()
        self.create_problem_py_file()

    def take_cat_input(self):
        valid_category = False
        print("Enter the category of the problem ")
        valid_inp_cat =[0,1,2]
        print("Enter either 0 or 1 or 2.\n0 for Easy level problem\n1 for medium level problem or \n2 for hard level problem")
        retry_stmt = f"Retry! Please enter the valid value . {valid_inp_cat} are the valid values"
        cat=-1
        while not valid_category:
            try :
                cat = int(input("Enter the probem category : "))
                if cat in valid_inp_cat:
                    print(f"Problem selcted {self.problem_category[str(cat)]}")
                    valid_category = True
                else:
                    print(retry_stmt)
            except KeyboardInterrupt:
                print("\nUser interrupted Exiting...")  
                sys.exit()   
                break   
            except Exception as e:
                print(f"An error occured :  {e}")
                print(retry_stmt)
        return str(cat)
    def take_title_number(self):
        #take a valid positive number as problem title number
        valid_tno = False
        retry_stmt ="Please enter the valid problem number"
        while(not valid_tno):
            try:
                tno = input("Enter the problem number :  ")
                if tno.isdigit():
                    #by checking string is digit or not it's ensured that tno is integer and in range(0,+infinity)
                    valid_tno =True
                else:
                    print(retry_stmt)
            except KeyboardInterrupt:
                print("\nUser interrupted Exiting...")  
                sys.exit()
            except Exception as e:
                print(f"Error occured : {e}")
                print(retry_stmt)
        return tno

    def format_title(self):
        #replace spaces with underscore
        return "_".join((self.title).split())
    
    def take_input(self):
        self.category = self.take_cat_input()
        self.url = str(input("Enter the Problem description URl : "))
        self.title_num =self.take_title_number()
        self.title = str(input("Enter the Problem title : "))
        self.f_title = self.format_title()

    def show_input(self):
        print(f"Category :  {self.problem_category[self.category]}")
        print(f"Problem Title : {self.title}")
        print(f"URL: {self.url}")

    def create_problem_folder(self):
        self.folder_category_path = (os.path.abspath(os.path.join(os.getcwd(),"./..",self.problem_category[self.category])))
        folder_name = f"{self.title_num}_{self.f_title}"
        self.problem_folder_path = os.path.join(self.folder_category_path,folder_name)
        #creating folders if it doesn't exist
        os.makedirs(self.problem_folder_path,exist_ok=True)

    def get_inital_txt_content(self):
        line1 = f"#URL : {self.url}\n"
        line2=f"Description : "
        return line1+line2
        
    def get_inital_py_content(self):
        #returns the content to write in python file
        author ="Kartik Bhatnagar"
        today_date = str(date.today())
        lines = [ 
            f"#URL : {self.url}\n",
            f"#[{self.problem_category[self.category]}] [{self.title_num}] \n",
            f"#Title: [{self.title}]\n",
            f"#Author: {author}\n",
            f"#Date : {today_date} (YYYY-MM-DD)\n",
            "\nif __name__ == \"__main__\"\n":,
            "    s=Solution()\n"
        ]
        return "".join(lines)

    def create_problem_txt_file(self):
        try:
            txt_file_name = f"{self.title_num}_description.txt"
            txt_file_path = os.path.join(self.problem_folder_path,txt_file_name)
            try:
                with open(txt_file_path,"w",encoding="utf-8") as txt_file:
                    txt_file.write(self.get_inital_txt_content())
                    print(f"{txt_file_name} is created {txt_file_name}")
            except Exception as e:
                print(f"Not able to create {txt_file_name} file")
                print(f"Exception : {e}")
        except Exception as e:
            print(f"create_problem_txt_file function failed")
            print(f"Exception : {e}")

    def create_problem_py_file(self):
        try:
            py_file_name = f"{self.title_num}.py"
            py_file_path = os.path.join(self.problem_folder_path,py_file_name)
            try:
                with open(py_file_path,"a",encoding="utf-8") as txt_file:
                    txt_file.write(self.get_inital_py_content())
                    print(f"{py_file_name} is created {py_file_path}")
            except Exception as e:
                print(f"Not able to create {py_file_path} file")
                print(f"Exception : {e}")
        except Exception as e:
            print(f"create_problem_py_file function failed")
            print(f"Exception : {e}")
        
        
    

if __name__ == "__main__":
    print(os.path.abspath(os.path.join(os.getcwd(),"./..")))
    p1 = Problem()
    


#future scope : user can just enter the problem number  or the URL and the data  will be extracted and the suitable folder and files will be created
#problem category, problem title and problem description will be extracted