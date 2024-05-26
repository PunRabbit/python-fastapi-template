import yaml
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration


def load_config():
    with open("core/config.yaml", "r") as file:
        config: dict = yaml.safe_load(file)
        working_environment: str = config.get("environment").get("work_env")
        return config.get(working_environment)


class ConfigContainer(DeclarativeContainer):
    config: Configuration = Configuration()

    config.from_dict(load_config())
    wiring_config: WiringConfiguration = WiringConfiguration(modules=["util.app.builder"])
