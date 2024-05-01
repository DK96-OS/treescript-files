# TreeScript Files
`treescript-files` is a command-line tool built in Python designed to interpret a unique file format known as "treescript." This format is used to describe file and folder directory structures. The primary function of `treescript-files` is to parse a treescript file and output a comprehensive list of file paths defined within the script to the standard output. An optional parameter allows users to prefix all file paths with a specified parent directory, enhancing the tool's flexibility in various file management tasks.

## Features
- **Parse Treescript**: Efficiently reads and processes treescript files.
- **Output File Paths**: Prints the complete list of file paths from the treescript.
- **Directory Prefixing**: Optional addition of a parent directory to all file paths.

## Installation
To install `treescript-files`, you will need Python installed on your system. The tool can be installed directly via pip:

```bash
pip install treescript-files
```

Alternatively, you can clone this repository and install the tool manually:

```bash
git clone https://github.com/yourusername/treescript-files.git
cd treescript-files
python setup.py install
```

## Usage
To use `treescript-files`, run the following command in your terminal:

```bash
treescript-files <path_to_treescript_file>
```

### Options
- **--parent `<directory>`**: Prefixes all output file paths with the specified directory.

### Example
Given a `treescript` file named `example.treescript`, you can display the file paths as follows:

```bash
treescript-files example.treescript
```

To prefix the paths with a parent directory `src/`:

```bash
treescript-files --parent src/ example.treescript
```

## Contributing
Contributions to `treescript-files` are welcome!

## License
`treescript-files` is open-source software licensed under the GPLv3 License. See the `LICENSE` file for more details.
