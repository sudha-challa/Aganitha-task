# PubMed Papers Fetcher

## Organization

- `pubmedpapers/`: Module with API, filtering, and CSV logic
- `cli.py`: Command-line interface

## Installation

```bash
poetry install
```

## Usage

```bash
poetry run get-papers-list "cancer immunotherapy" -f results.csv --debug
```

- `-h, --help`: Show help
- `-d, --debug`: Enable debug output
- `-f, --file`: Output filename (CSV)

## External Tools

- [Typer](https://typer.tiangolo.com/) for CLI
- [requests](https://docs.python-requests.org/)
- [pandas](https://pandas.pydata.org/)
- [PubMed API](https://pubmed.ncbi.nlm.nih.gov/)

## LLMs

No LLMs are used in the code, but development leveraged GitHub Copilot and ChatGPT for design.

## Publishing

To publish the module to TestPyPI:
```bash
poetry build
poetry publish -r testpypi
```