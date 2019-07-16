local snapcraft = import 'snapcraft.libsonnet';

snapcraft {
    name: "sc-jsonnet",
    version: "0.1",
    summary: "Build your snapcraft.yaml with jsonnet!",
    description: "Use jsonnet syntax to build your snapcraft.yaml.
For information about jsonnet see https://jsonnet.org/",
    grade: "stable",
    confinement: "strict",

    parts: {
        "sc-jsonnet": {
            plugin: "python",
            source: ".",
            "python-version": "python3",
            "build-packages": ["git"],
        },
    },

    apps: {
        "sc-jsonnet": {
            command: "bin/sc-jsonnet",
            plugs: [
                "home",
                "network",
                "removable-media",
            ],
        },
    },
}
