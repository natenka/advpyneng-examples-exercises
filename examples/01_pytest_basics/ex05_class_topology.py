class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        normalized_topology = {}
        for box, neighbor in topology_dict.items():
            if not neighbor in normalized_topology:
                normalized_topology[box] = neighbor
        return normalized_topology

    def delete_link(self, from_port, to_port):
        if self.topology.get(from_port) == to_port:
            del self.topology[from_port]
        elif self.topology.get(to_port) == from_port:
            del self.topology[to_port]
        else:
            print("Такого соединения нет")

    def __add__(self, other):
        return Topology({**self.topology, **other.topology})


topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

topology_example2 = {
    ("R1", "Eth0/4"): ("R7", "Eth0/0"),
    ("R1", "Eth0/6"): ("R9", "Eth0/0"),
}
