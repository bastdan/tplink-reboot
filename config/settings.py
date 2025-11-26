from dataclasses import dataclass
from typing import Mapping, Optional
import os

@dataclass(frozen=True)
class HostCredentials:
    hosts: list[str]
    password: str
    dry_run: bool

    @classmethod
    def from_env(cls, env: Optional[Mapping[str, str]] = None, prefix: str = "") -> "HostCredentials":
        """
        Create HostCredentials from an environment mapping.

        env: mapping with environment variables (defaults to os.environ)
        prefix: optional prefix added before HOST/USERNAME/PASSWORD (case-insensitive)
                e.g. prefix="MYAPP_" will read MYAPP_HOST, MYAPP_USERNAME, MYAPP_PASSWORD
        """
        env = env if env is not None else os.environ
        def key(name: str) -> str:
            return f"{prefix}{name}".upper()

        try:
            hosts = env[key("HOSTS")].split(",")
            password = env[key("PASSWORD")]
            dry_run = env.get(key("DRY_RUN"), "false").lower() in ("1", "true", "yes")
        except KeyError as e:
            raise KeyError(f"Missing environment variable: {e.args[0]}") from e

        return cls(hosts=hosts, password=password, dry_run=dry_run)
    def __repr__(self) -> str:
        # hide password in repr
        return f"{self.__class__.__name__}(hosts={self.hosts!r}, password='***', dry_run={self.dry_run!r})"