import click
from utils.logging import log
from utils.Template import TemplatesProcess
from utils.Flush import FLushProcess


@click.group()
def cli():
    pass 

@click.command()
def init():
    log("INITIALIZING APP","","green",True,True)
    template_process=TemplatesProcess()
    template_process.run()


@click.command()
def flush():
    log("ATTENTION","","red",True,False)
    log("The following action will delete content.","red","",False,False)
    log("Mapping content ...","red","",False,False)
    flush_process = FLushProcess()
    flush_process.run()

if __name__ == "__main__":
    cli.add_command(init)
    cli.add_command(flush)
    cli()