import os
import sys
from .procedure_meta import ProcedureMeta

class TemplatesProcedure(ProcedureMeta):

    def __init__(self,conf_path:str) -> None:
        super().__init__()
        self.__self_conf_content=self.readConf(conf_path)["commands"]
        self.__project_name=""
        self.__state = "IDLE"
        self.__commands=[]
        self.__options={
            "SELECT_PROJECT_NAME":self.__SetProjectName,
            "SELECT_TEMPLATE":self.__SelectTemplate,
            "SELECT_ENVIRON":self.__SelectDevEnviroment,
            "SELECT_DATABASE":self.__SelectDatabase,
            "SELECT_STYLE":self.__SelectStyle
        }

    
    def __SetProjectName(self):
        self.__project_name=input("Project name : ")
        print(self.__project_name)
        if (self.__project_name is not  None 
        and self.__project_name != ""
        and len(self.__project_name) > 0
        ):
            self.__state="SELECT_TEMPLATE"
        else:
            print("You must select a name from your project.")


    def __SelectTemplate(self):
        print("Templates:")
        self.__ShowOptions(self.__self_conf_content["templates"])
        self.__ParseUserInput(
            "Select a template : ",
            "SELECT_ENVIRON",
            self.__self_conf_content["templates"]
        )
    

    def __SelectDevEnviroment(self):
        print("Environments:")
        self.__ParseUserInput(
            "Select a development enviroment : ",
            "SELECT_DATABASE",
            self.__self_conf_content["environment"]
        )
    

    def __SelectDatabase(self):
        print("Databases:")
        self.__ParseUserInput(
            "Select a database : ",
            "SELECT_STYLE",
            self.__self_conf_content["database"]
        )


    def __SelectStyle(self):
        print("Styles:")
        self.__ParseUserInput(
            "Select a style template : ",
            "DONE",
            self.__self_conf_content["styles"]
        )
        if self.__project_name is not None:
            self.__AddProjectName()


    def __AddProjectName(self):
        print(self.__project_name)

    
    def __ShowOptions(self,options:dict):
        count=0
        options=list(options.keys())
        for option in options:
            print(f"    {count}) {option}")
            count+=1


    def __ParseUserInput(self,quetion:str,next_state:str,commands:dict)->int:
        try:
            result=int(input(quetion))
            command_list=list(commands.keys())
            if result > len(command_list) or result < 0:
                raise Exception("Invalid option")
            else:
                command=command_list[result]
                self.__commands+=commands[command]
            self.__state=next_state
        except TypeError as type_err:
            print(type_err)
        except Exception:
            print("The argument can ony be a number.")
            


    def run(self):
        while self.__state!= "DONE":
            if self.__state == "IDLE":
                self.__options.get("SELECT_PROJECT_NAME")()
            else:
                self.__options.get(self.__state)()
        return self.__commands