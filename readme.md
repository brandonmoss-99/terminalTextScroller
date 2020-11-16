# terminalTextScroller

terminalTextScroller is a Python script for displaying a scrolling text message across a terminal window.

## Dependancies
- [Python](https://www.python.org/downloads/) 3+

## Usage

To use terminalTextScroller, simply call it:

```bash
$ python3 scroller.py [OPTIONS]...
```

See also `python3 scroller.py --help`.

### Options

Required:

`-m` or `--message`: Text message to be shown scrolling across the terminal window.

Optional:

`-t` or `--trail`: Number of whitespace characters to append to the end of the message before it is repeated. (Default=15)

`-w` or `--width`: Column width of the window/display to show the message on. (Default=60)

### Example

Print the message 'Hello World!' with the default trailspace of 15 characters and display width of 60 columns:

```bash
$ python3 scroller.py -m 'Hello World!'
```

Print the message 'Hello World!' with a trailspace of 10 characters and display width of 80 columns:

```bash
$ python3 scroller.py -m 'Hello World!' -t 10 -w 80
```

## Compatibility
These files were only written as a personal test project, and designed to work on my MacOS machine (MacOS 10.14.6) for the Bash shell. I haven't tested its functionality for anything else, I imagine it should also work on Linux as well as other shells with some minor issues, but not Windows.