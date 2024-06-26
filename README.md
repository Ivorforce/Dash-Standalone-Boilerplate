# Dash Standalone Boilerplate

This package is a template for [dash](https://dash.plotly.com) and [Flask](https://flask.palletsprojects.com/en/3.0.x/) based apps that want to compile.

The chosen compiler is [Nuitka](https://nuitka.net).

## Setup

First, [install poetry](https://python-poetry.org/docs/). Then:

```bash
poetry install  # install
poetry run python src/dnb/main.py  # test
poetry run python -m nuitka --onefile --include-package=dash --include-package-data=dash --include-package=dash_core_components --include-package-data=dash_core_components --include-package=dash_html_components --include-package-data=dash_html_components --include-package=packaging --include-package-data=packaging --include-package=plotly --include-package-data=plotly src/dnb/main.py  # compile
./main.bin  # run binary
```
