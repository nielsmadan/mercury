# TODOs

## future

### sources

* `[ ]` any text object

### execution

* `[ ]` add support for compiled languages.

### destinations

* `[ ]` bubble

### misc

* `[ ]` end to end testing

--------------------------------------------------------------------------------

## version 1.1

### execution

* `[ ]` add support for: perl, vimscript, clojure, php
* `[ ]` get stdout / stderr from killed process
* `[ ]` option: for all languages, add options to override executable and options
* `[X]` option: add default option if filetype isn't recognized
* `[X]` option: allow option to override one filetype with another

* `[ ]` python: smarter code parsing for final print statement
* `[ ]` python: print assignment statement
* `[ ]` python: import any modules if they are imported in file
* `[ ]` python: look into dealing with python3.

### options

### misc

* `[ ]` only load language specific module on first loading a file?
* `[ ]` option: create options to override splitbelow and splitright
* `[ ]` option: make timeout configurable

--------------------------------------------------------------------------------

## version 1.0

### sources

* `[X]` line
* `[X]` selection
* `[X]` buffer

### execution

* `[X]` remove indentation (for python)
* `[X]` add print to last line of code if it doesn't have one.
* `[X]` import some subset of standard modules if they are imported in file
* `[X]` handle std err
* `[X]` javascript support

### destinations

* `[X]` register
    * `[X]` use default register
    * `[X]` prompt for register
* `[X]` selection
* `[X]` split
    * `[X]` horizontal split
    * `[X]` vertical split
    * `[X]` set split to be nofile (so it can be closed without prompt for saving)
* `[X]` message window

### misc

* `[X]` options
    * `[X]` option to set start of mapping sequence
    * `[X]` option to disable default mapping
    * `[X]` all functions available as vimscript
    * `[X]` option to set default register
* `[X]` test coverage
    * `[X]` fix stdout for tests
    * `[X]` test for execution part
* `[X]` help file
* `[X]` README
