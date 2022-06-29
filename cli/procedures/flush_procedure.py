import os
from .procedure_meta import ProcedureMeta
from .mapping_procedure import map_dirs,remove_dir,check_dir
from .logging import log


class FLushProcess(ProcedureMeta):
    def __init__(self,conf_path:str) -> None:
        super().__init__()
        self.confContent=self.readConf(conf_path)
        self.state = "IDLE"
        self.templates = {}
        self.target_template = ""

  
    def mapping_files(self):
            # self.templates = map_dirs(ignore_this).copy()
            if len(self.templates) == 0:
                self.state = "DONE"
                log(f"{len(self.templates)} no templates available")
            else:
                log(f"{len(self.templates)} templates available:")
                print("\n")
                for item in self.templates:
                    log(f"  ---> {item}")
                print("\n")
                self.state = "SELECTING"


    def select_template(self):
            log("Enter the name of the template that will be deleted : ")
            log("Press ctrl + c  to exit/cancel")
            name = input()
            if self.templates.get(name) is None:
                log(f"The template name '{name}' does not exist","red")
                self.state = "MAPPING"
            else:
                self.target_template = name
                self.state = "CHECKING"


    def check_template_dir(self):
        if not check_dir(self.templates[self.target_template]):
            log(f"The template '{self.target_template}' cannot be found","red")
            self.state =  "DONE"
        else:
            self.state = "DELETING"


    def delete_template(self):
        item = self.templates[self.target_template]
        log(f"Deleting {self.target_template}","yellow")
        if remove_dir(item):
            log(f"{self.target_template} successfully deleted","green")
        else:
            log("ERROR","","red",True,True)
            log(f"Cannot delete --> {item}","","red",True,True)
        self.state =  "DONE"


    def run(self):
        while self.state != "DONE":
            if self.state == "IDLE":
                self.mapping_files()
            if self.state == "MAPPING":
                self.mapping_files()
            if self.state == "SELECTING":
                self.select_template()
            if self.state == "CHECKING":
                self.check_template_dir()
            if self.state == "DELETING":
                self.delete_template()
        self.state = "IDLE"
            
    
    