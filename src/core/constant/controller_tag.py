from dataclasses import dataclass


@dataclass(frozen=True)
class ControllerTag:
    USER_SAMPLE_TAG_NAME: str = "This is just Sample"
    HEALTH_TAG_NAME: str = "Checking Infra Health"
