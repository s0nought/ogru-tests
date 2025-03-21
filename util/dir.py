from os import makedirs
from shutil import copytree, rmtree
from pathlib import Path, PurePath

def create(name: Path, exist_ok: bool = True) -> None:
    makedirs(name=name, exist_ok=exist_ok)

def copy(src: PurePath, dst: PurePath, dirs_exist_ok: bool = True) -> None:
    copytree(src=src, dst=dst, dirs_exist_ok=dirs_exist_ok)

def remove(path: Path) -> None:
    rmtree(path=path)
