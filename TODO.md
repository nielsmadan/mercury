# TODOs

## version 2.0

### sources

* `[ ]` any text object

### destinations

* `[ ]` bubble

## version 1.1

### execution

* `[ ]` vimscript: support it
* `[ ]` smarter code parsing for final print statement
* `[ ]` print assignment statement
* `[ ]` get stdout / stderr from killed process
* `[ ]` python: import any modules if they are imported in file
* `[ ]` python: look into dealing with python3.
* `[ ]` for all languages, add options to specify executable and options

### misc

* `[ ]` only load language specific module on first loading a file?
* `[ ]` less ugly tests
* `[ ]` create options to overwrite splitbelow and splitright
* `[ ]` make timeout configurable

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
* `[ ]` test coverage
    * `[ ]` fix stdout for tests
    * `[ ]` test for execution part
* `[X]` help file
* `[X]` README
