"""
Copyright 2017-2023 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from pathlib import Path
import shutil

def exists(path: str) -> bool:
    return Path(path).exists()

def copy(from_path: str, to_path: str, force: bool = False) -> None:
    to_path_obj = Path(to_path)
    if to_path_obj.exists():
        if force:
            shutil.rmtree(to_path)
        else:
            raise FileExistsError(f"Destination path '{to_path}' already exists.")
    shutil.copytree(from_path, to_path)

def move(from_path: str, to_path: str, force: bool = False) -> None:
    to_path_obj = Path(to_path)
    if to_path_obj.exists() and not force:
        raise FileExistsError(f"Destination path '{to_path}' already exists.")
    shutil.move(from_path, to_path)

def mkdir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

def rm(path: str) -> None:
    path_obj = Path(path)
    if path_obj.is_dir():
        shutil.rmtree(path)
    elif path_obj.is_file():
        path_obj.unlink()
    else:
        raise FileNotFoundError(f"No file or directory found at '{path}'.")

def cwd() -> str:
    return str(Path.cwd())

def cd(path: str) -> None:
    Path(path).chdir()
