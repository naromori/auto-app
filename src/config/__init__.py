from .prod import ProdConfig
from .dev import DevConfig
from .debug import DebugConfig
from utils import EnvManager


def get_config():
    mode = EnvManager.get_env("ENV_MODE")

    if not mode:
        return ProdConfig
    
    match mode:
        case "dev":
            return DevConfig
        case "debug":
            return DebugConfig
        case _:
            return ProdConfig