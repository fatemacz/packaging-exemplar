# Packaging Exemplar

This repository serves as an example of how to package a Python project. It includes all the necessary files and instructions to help you get started with packaging your own Python projects.

## Project Structure

```
packaging-exemplar/
│
├── src/
│   └── example_package_fatemacz/
│       ├── __init__.py
│       └── example.py
├── tests/
│   └── test_example.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Running Tests

To run the tests, use the following command:

```bash
pytest
```

## Building the Package

To build the package, navigate to the root directory of the project and run:

```bash
python -m build
```

This will generate distribution archives in the `dist/` directory.

## Uploading the Package

To upload the package to PyPI using Twine, first ensure you have Twine installed:

```bash
python -m pip install --upgrade twine
```

Then, upload the package by running:

```bash
python -m twine upload --repository testpypi dist/*
```

## Installation

To install the package, clone the repository and run:

```bash
pip install -i https://test.pypi.org/simple/ packaging-exemplar-fatemacz
```

## Usage

After installation, you can use the package as follows:

```python
from example_package import example

example.sum_all(1, 2, 3, 4)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.
