"""Hello name module"""
from fastapi import APIRouter, Path
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="", tags=["hello"])


@router.get("/hello/{name}", response_class=PlainTextResponse)
async def get_hello_name(name: str = Path(...)) -> str:
    """Endpoint to return hello name message

    Args:
        name (str): name to concatenate

    Returns:
        str: concatenate string
    """
    return "Hello " + name + " !"
