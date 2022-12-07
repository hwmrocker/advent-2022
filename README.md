# advent-2020

My solutions to the [Advent of Code 2020](https://adventofcode.com/2020) puzzles.

## Installation

### Install the dependencies
This project uses [poetry](https://python-poetry.org/) to manage dependencies. To install the dependencies, run the following command:

```bash
$ poetry install
```

It also uses [direnv][1] to manage environment variables.
Alternatively you can put the bin folder in your path or run the scripts directly.

```bash
$ export PATH=$PATH:$(pwd)/bin
```


## Usage

### run the code for the latest day
```bash
$ run
```

### run the code for the latest day and part
```bash
$ run b
```

### run the code for a specific day
```bash
$ run 1
```

### run the code for a specific day and part
```bash
$ run 1 b
```

### bootstrap a new day
```bash
$ bootstrap
Bootstrapping day02
Press enter to continue...
```

confirm with Enter or exit with Ctrl-C. When you confirmed the the bootstrap folder for the new day will be created.

## License

[MIT License](LICENSE)

[1]: https://direnv.net/docs/installation.html
