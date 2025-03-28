from shutil import copytree
from pathlib import PurePath

def copy(src: PurePath, dst: PurePath, dirs_exist_ok: bool = True) -> None:
    copytree(src=src, dst=dst, dirs_exist_ok=dirs_exist_ok)
