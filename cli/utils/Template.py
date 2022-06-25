import os 
from conf.conf import main_repos
class TemplatesProcess:

    def __init__(self) -> None:
        self.__state = "IDLE"
        self.__mainRepos = main_repos
        self.__totalRepos = len(main_repos)
        self.__confirmedRepo=0

    def __sendRepoRequest(self,url:str):
        print(f"url > {url}")
        return  1


    def __checkRepositories(self):
        
        print("Checking templates")
        self.__confirmedRepo=0
        for item in self.__mainRepos:
            self.__confirmedRepo+=self.__sendRepoRequest(item)
            print(f"{self.__confirmedRepo}/{self.__totalRepos} checked")

        if self.__confirmedRepo==self.__totalRepos:
            print("All templates confirmed")
            self.__state="SELECT_TEMPLATE"
        else:
            print("Cannot confirm templates")
            print("Aborting")
            self.__state="DONE"
    

    def __selectTemplate(self):
        print("Select a template")
        result=input()
        print(f"--->{result}")
        self.__state="SELECT_ENVIRON"

    def __selectDevEnviroment(self):
        print("Select a development enviroment")
        result=input()  
        print(f"--->{result}")
        self.__state="SELECT_DATABASE" 
    
    def __selectDatabase(self):
        print("Select a database")
        result=input()
        print(f"--->{result}") 
        self.__state="SELECT_STYLE"

    def __selectStyle(self):
        print("Select a style template")
        result=input()
        print(f"--->{result}") 
        self.__state="SELECT_BACKUP"

    def __selectRepository(self):
        print("Select backup repository")
        result=input()
        print(f"--->{result}") 
        self.__state="DONE"



    def run(self):
        
        while self.__state!= "DONE":

            if self.__state=="IDLE":
                self.__checkRepositories()
            if self.__state=="SELECT_TEMPLATE":
                self.__selectTemplate()
            if self.__state=="SELECT_ENVIRON":
                self.__selectDevEnviroment()
            if self.__state=="SELECT_DATABASE":
                self.__selectDatabase()
            if self.__state=="SELECT_STYLE":
                self.__selectStyle()
            if self.__state=="SELECT_BACKUP":
                self.__selectRepository()
