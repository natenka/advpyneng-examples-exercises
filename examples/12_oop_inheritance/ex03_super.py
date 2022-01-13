# In [4]: rich_tree(IOSXEDriver)
# Out[4]:
# IOSXEDriver
# └── NetworkDriver
#     ├── GenericDriver
#     │   ├── Driver
#     │   │   └── BaseDriver
#     │   └── BaseGenericDriver
#     └── BaseNetworkDriver


class Custom:
    def send_command(self, *args, **kwargs):
        print("AAAAAAAAAAAAAAA")
        return super().send_command(*args, **kwargs)


class MyDriver(Custom, IOSXEDriver):
    pass


