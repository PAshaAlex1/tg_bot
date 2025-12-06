import os
from dataclasses import dataclass


def _load_env_file():
    """Загружает переменные из .env файла, если он существует."""
    env_path = ".env"
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if key and value and key not in os.environ:
                        os.environ[key] = value


@dataclass
class Config:
    bot_token: str
    payment_provider_token: str | None = None
    
    @classmethod
    def from_env(cls) -> "Config":
        _load_env_file()
        bot_token = os.getenv("BOT_TOKEN")
        if not bot_token:
            raise ValueError("BOT_TOKEN не установлен")
        return cls(
            bot_token=bot_token,
            payment_provider_token=os.getenv("PAYMENT_PROVIDER_TOKEN"),
        )

