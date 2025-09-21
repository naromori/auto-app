from .prod import ProdConfig
from .dev import DevConfig
from .debug import DebugConfig
from os import getenv


def get_config():
    mode = getenv("ENV_MODE")

    if not mode:
        return ProdConfig
    match mode:
        case "dev":
            return DevConfig
        case "debug":
            return DebugConfig
        case _:
            return ProdConfig