from ex04_get_all_interface import get_interfaces_from_cfg


def test_only_phy():
    input_cfg = (
        "!\n"
        "interface FastEthernet0/0\n"
        " switchport mode access\n"
        " switchport access vlan 10\n"
        "!\n"
        "interface FastEthernet0/1\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport trunk allowed vlan 100,200\n"
        " switchport mode trunk\n"
        "!\n"
        "interface FastEthernet0/2\n"
        " switchport mode access\n"
        " switchport access vlan 20\n"
        "!\n"
    )
    correct_intf_list = ["FastEthernet0/0", "FastEthernet0/1", "FastEthernet0/2"]
    intf_list = get_interfaces_from_cfg(input_cfg)
    assert intf_list == correct_intf_list


def test_only_phy_and_loopback():
    input_cfg = (
        "!\n"
        "interface FastEthernet0/0\n"
        " switchport mode access\n"
        " switchport access vlan 10\n"
        "!\n"
        "interface FastEthernet0/1\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport trunk allowed vlan 100,200\n"
        " switchport mode trunk\n"
        "!\n"
        "interface FastEthernet0/2\n"
        " switchport mode access\n"
        " switchport access vlan 20\n"
        "!\n"
        "interface Loopback100\n"
        " description test\n"
    )
    correct_intf_list = ["FastEthernet0/0", "FastEthernet0/1", "FastEthernet0/2", "Loopback100"]
    intf_list = get_interfaces_from_cfg(input_cfg)
    assert intf_list == correct_intf_list


def test_empty_cfg():
    input_cfg = ""
    correct_intf_list = []
    intf_list = get_interfaces_from_cfg(input_cfg)
    assert intf_list == correct_intf_list
