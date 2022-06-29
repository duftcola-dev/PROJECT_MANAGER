import json 

class ProcedureMeta:

    def __init__(self) -> None:
        pass

    def readConf(self,path:str):
        try:
            file=open(path,"r")
            content=file.read()
            jsonContent=json.loads(content)
            file.close()
            return jsonContent
        except FileNotFoundError as notFound:
            print(str(notFound))
        except Exception as unknown:
            print(str(unknown))

    
    def writeConf(self,path:str,content:dict):
        try:
            file=open(path,"w")
            content=json.dump(content)
            file.write(content)
            file.close()
        except FileNotFoundError as notFound:
            print(str(notFound))
        except Exception as unknown:
            print(str(unknown))


  