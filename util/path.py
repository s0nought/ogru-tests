from pathlib import Path, PurePath

def get_path(*args: str) -> Path:
    return Path(*args)

def get_pure_path(*args: str) -> PurePath:
    return PurePath(*args)
