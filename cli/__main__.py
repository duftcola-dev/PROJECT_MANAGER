import click
import os

from procedures.logging import log
from procedures.template_procedure import TemplatesProcedure
from procedures.flush_procedure import FLushProcess
from procedures.procedure_meta import ProcedureMeta
conf_path=os.getcwd()+"/cli/conf/conf.json"


@click.group()
def cli():
    pass 

@click.command()
def edit_conf():
    read_conf=ProcedureMeta()
    read_conf.readConf(conf_path)



@click.command()
def init():
    log("INITIALIZING APP","","green",True,True)
    template_process=TemplatesProcedure(conf_path)
    commands=template_process.run()
    print(commands)


@click.command()
def flush():
    log("ATTENTION","","red",True,False)
    log("The following action will delete content.","red","",False,False)
    log("Mapping content ...","red","",False,False)
    flush_process = FLushProcess(conf_path)
    flush_process.run()

if __name__ == "__main__":
    cli.add_command(init)
    cli.add_command(flush)
    cli.add_command(edit_conf)
    cli()