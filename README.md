# Dash Standalone Boilerplate

This package is a template for [dash](https://dash.plotly.com) and [Flask](https://flask.palletsprojects.com/en/3.0.x/) based apps that want to compile.

The chosen compiler is [Nuitka](https://nuitka.net).

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
