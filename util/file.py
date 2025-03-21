import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def write(file: Path, content: str, mode: str = "wt", encoding: str = "UTF-8") -> None:
    try:
        with open(file=file, mode=mode, encoding=encoding) as f:
            f.write(content)
    except Exception as e:
        logger.warning(e)
        raise
