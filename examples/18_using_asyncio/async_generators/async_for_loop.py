async def async_for(items):
    iterator = items.__aiter__()
    while True:
        try:
            item = await iterator.__anext__()
            print(item)
        except StopAsyncIteration:
            break
