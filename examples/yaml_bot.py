#!/usr/bin/env python3

from __future__ import annotations

from mewbot.demo import Foo
from mewbot.loader import load_component


def main() -> None:
    yaml_demo = load_component(
        {
            "kind": "Condition",
            "apiVersion": "v1",
            "module": "mewbot.demo",
            "name": "Foo",
            "uuid": "3f7c493bce054566b90654ece62804c1",
            "properties": {"channel": "cat"},
        }
    )

    local_demo = Foo()
    local_demo.channel = "cat"

    print("Loaded from YAML-like object:  ", yaml_demo)
    print("Created and channel set        ", local_demo)
    print("Serialised:                    ", local_demo.serialise())
    print("Re-loaded from serialized data:", load_component(local_demo.serialise()))


if __name__ == "__main__":
    main()
