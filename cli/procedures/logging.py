import click 
from datetime import datetime



def log(message:str,color:str="",background:str="",bold:bool=False,date:bool=False):
    current_date = ""
    if date:
        current_date=datetime.now()
        message = message + " "+str(current_date)
    click.secho(message,fg=color,bg=background,bold=bold)