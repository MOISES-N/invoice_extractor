from pydantic import BaseModel
import yaml


class ProjectConfig(BaseModel):
    """Configuration settings for the invoice extraction project."""

    field_extractors: dict[str, str]

    @classmethod
    def from_yaml(cls, config_path: str) -> "ProjectConfig":
        """Load configuration settings from a YAML file.

        Args:
            config_path (str): Path to the YAML configuration file.

        Returns:
            ProjectConfig: A populated configuration object.
        """

        with open(config_path, encoding="utf-8") as f:
            config_dict = yaml.safe_load(f)

        return cls(**config_dict)