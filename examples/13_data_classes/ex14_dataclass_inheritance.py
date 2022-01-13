from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class BaseTransportArgs:
    transport_options: Dict[str, Any]
    host: str
    port: int = 22
    timeout_socket: float = 10.0
    timeout_transport: float = 30.0
    logging_uid: str = ""

    def __init__(self):
        pass

@dataclass
class PluginTransportArgs(BaseTransportArgs):
    host: str = "0.0.0.0"
    auth_username: str = ""
    auth_private_key: str = ""
    auth_strict_key: bool = True
    ssh_config_file: str = ""
    ssh_known_hosts_file: str = ""
