from app.registry import RegistryLoader

loader = RegistryLoader()

registry = loader.load()

print()

print(

    registry.list()

)