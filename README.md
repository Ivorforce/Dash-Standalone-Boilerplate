# Dash Standalone Boilerplate

This package is a template for [Dash](https://dash.plotly.com) (and generally [Flask](https://flask.palletsprojects.com/en/3.0.x/)) based Python web programs that want to be an app rather than a local website.

## Setup

First, [install poetry](https://python-poetry.org/docs/). Then:

```bash
# set up project
poetry install
# test; you can skip this step
poetry run python src/dnb/main.py
# compile binary
poetry run python -m nuitka --output-dir=build --onefile --macos-create-app-bundle --include-package=dash --include-package-data=dash --include-package=dash_core_components --include-package-data=dash_core_components --include-package=dash_html_components --include-package-data=dash_html_components --include-package=packaging --include-package-data=packaging --include-package=plotly --include-package-data=plotly --include-package=dnb --include-package-data=dnb src/dnb/main.py
# run binary
./main.bin
```

## How does it work?

First, a [Flask](https://flask.palletsprojects.com/en/3.0.x/) server is opened through a local port (8050). This server can be accessed through any local web browser. [Dash](https://dash.plotly.com) is attached to the Flask server.

To make it a standalone app, a web view (through [pywebview](https://pywebview.flowrl.com)) is opened to visit the address. In contrast to something like Electron, the web view is completely native and thus not included in the final app bundle. This makes the app leaner and less RAM intensive.

Finally, the app is bundled into an executable using [Nuitka](https://nuitka.net). Nuitka compiles the whole python interpreter, including required packages, into an app that can be run without an existing python installation.

These tricks combine to make an app that behaves just as one would expect from a normal app, avoiding the myriad issues that are normally associated with shipping a python web app.
