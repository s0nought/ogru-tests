import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

def load(file: Path, mode: str = "rt", encoding: str = "UTF-8") -> Any:
    try:
        with open(file=file, mode=mode, encoding=encoding) as f:
            return json.load(f)
    except FileNotFoundError as e:
        logger.warning(e)
        raise
