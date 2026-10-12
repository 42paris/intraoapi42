#!/usr/bin/env python3

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml


INDEX_FILE_NAME = "_index.yaml"
DIRECTORIES = ("paths", "schemas", "parameters")


def normalize_object_ref(ref: str) -> str:
    """
    Escape a JSON Pointer token.

    Example:
        /languages/{id}
        -> ~1languages~1{id}
    """
    return ref.replace("~", "~0").replace("/", "~1")


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if data is None:
        return {}

    if not isinstance(data, dict):
        raise ValueError(
            f"{path} must contain a YAML mapping at its root"
        )

    return data


def relative_ref(from_file: Path, target_file: Path) -> str:
    """
    Return a POSIX relative path from one YAML file to another.
    """
    return os.path.relpath(
        target_file,
        start=from_file.parent,
    ).replace(os.sep, "/")


def generate_index_file(directory: Path) -> None:
    index_file_path = directory / INDEX_FILE_NAME
    index_data: dict[str, dict[str, str]] = {}

    # Recursively include YAML files from nested directories.
    yaml_files = sorted(
        path
        for path in directory.rglob("*.yaml")
        if path.name != INDEX_FILE_NAME
    )

    for file_path in yaml_files:
        data = load_yaml(file_path)

        for top_level_key in data:
            if top_level_key in index_data:
                raise ValueError(
                    f"Duplicate key {top_level_key!r} "
                    f"found while indexing {directory}"
                )

            normalized_key = normalize_object_ref(top_level_key)
            ref_path = relative_ref(index_file_path, file_path)

            index_data[top_level_key] = {
                "$ref": f"{ref_path}#/{normalized_key}",
            }

    with index_file_path.open("w", encoding="utf-8") as file:
        yaml.safe_dump(
            index_data,
            file,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
        )

    print(f"Generated {index_file_path}")


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    specs_directory = project_root / "specs"

    for directory_name in DIRECTORIES:
        directory = specs_directory / directory_name

        if not directory.is_dir():
            raise FileNotFoundError(
                f"Missing directory: {directory}"
            )

        # Generate only the index in the configured parent directory.
        generate_index_file(directory)


if __name__ == "__main__":
    main()