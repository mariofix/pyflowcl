import typer
from rich import print
from rich.console import Console
from rich.table import Table

from .openapi3 import FlowAPI

app = typer.Typer(help="CLI para Flow Chile")


@app.command("listar-operaciones", help="Muestra las operaciones disponibles.")
def listar_operaciones():
    """
    Comando para mostrar las operaciones disponibles en un recurso de la API de Flow.
    """
    flow = FlowAPI(api_key="key", api_secret="secret", endpoint="sandbox")
    table = Table(title="Operaciones Flow", collapse_padding=True, pad_edge=True, leading=1)
    table.add_column("Operación", no_wrap=True)
    table.add_column("Uso", no_wrap=True, justify="center")
    table.add_column("Descripción", justify="center")

    for op in flow.objetos._operation_map.items():
        table.add_row(
            f"[bold green]{op[0]}[/bold green]",
            f"FlowAPI().objetos.[bold green]call_{op[0]}[/bold green](**kwargs)",
            f"{op[1].description.strip()[:60]}...",
        )

    console = Console()
    console.print(table)


@app.command("buscar-operaciones", help="Busca operaciones disponibles.")
def buscar_operaciones():
    """
    Comando para buscar las operaciones disponibles en un recurso de la API de Flow.
    """
    flow = FlowAPI(api_key="key", api_secret="secret", endpoint="sandbox")
    table = Table(title="Operaciones Flow", collapse_padding=True, pad_edge=True, leading=1)
    table.add_column("Operación", no_wrap=True)
    table.add_column("Uso", no_wrap=True, justify="center")
    table.add_column("Descripción", justify="center")

    for op in flow.objetos._operation_map.items():
        table.add_row(
            f"[bold green]{op[0]}[/bold green]",
            f"FlowAPI().objetos.[bold green]call_{op[0]}[/bold green](**kwargs)",
            f"{op[1].description.strip()[:60]}...",
        )

    console = Console()
    console.print(table)


@app.command("info-operacion")
def info_operacion(operacion: str = None):
    """
    Comando para mostrar información de una operación específica de la API de Flow.

    Args:
        operacion (str, optional): Nombre de la operación. Default es None.
    """
    flow = FlowAPI(api_key="key", api_secret="secret", endpoint="sandbox")
    print(flow.objetos.operacion.ayuda)
