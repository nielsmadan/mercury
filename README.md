# mercury

`mercury` allows you to take a fragment of code from some source (current line, selection, buffer), execute the code intelligently, and then write the result to some destination (message window, selection, register, new split).

Features include:

 * choose the correct interpreter with the correct switches, given the filetype.
 * execute it in a separate thread and terminate it after a timeout, so an
   endless loop will not freeze vim.
 * some language specific smartness (e.g. handling imports).

Currently supports python, ruby and javascript (using node) with more to come soon, hopefully.

## installation

`mercury` requires [venom](https://github.com/nielsmadan/venom), which in turn requires vim to be
compiled with python support (most vim distributions have are). Vundle or pathogen are highly
recommended for installation.

    Bundle 'nielsmadan/venom'
    Bundle 'nielsmadan/mercury'

For what it's worth, the order actually does not matter.

## mappings

Default mappings are mnemonic. All mappings start with some configurable start sequence (default: `<leader>r`), followed by one character that specifies the source, and a second character that specifies the destination.

### Sources:

* l = line
* s = selection
* b = buffer

### Destinations:

* r = register
* s = selection
* h = horizontal split
* v = vertical split
* m = message window

### Some examples:

    <leader>rlm - (r)un (l)ine into (m)essage window.
    <leader>rss - (r)un (s)election into (s)election.
    <leader>rbv - (r)un (b)uffer into (v)ertical split.

There are also two shortcuts: `<leader>rr` will run the current buffer in normal mode or the current selection in visual mode and send the result to the message window.

## use cases

Short version: mercury covers a large chunk of simple REPL use cases, only it's faster (don't have to transfer the code to the REPL or keep switching back and forth), you don't have to setup a REPL and mantain it, and it works the same way in any language. And you get easy text generation in a programming language you know thrown in for free.

### discovery

Come across some code, can't figure out what it does? Execute it and see. Trying to figure out what a function would return if you gave it argument x, y, z?

    def mystery_function(s):
        m = re.search('(?<=-)\w+', s)
        return m.group(0) if m is not None else None

    mystery_function('hyphenated-word')

Write down the call, select everything, execute it, find out.

### rapid iteration

All that good stuff REPL afficionados have been telling you about for ages, only instead of having to work on functions or expressions in the REPL, and then having to transfer them and piece them together in the source code, you can do everything right inside your buffer.

### text generation

Say you need to create a list of every 2 element combination of -1, 0, and 1.

    import itertools
    list(itertools.product([-1, 0, 1], repeat=2))

Select and execute into selection and you get:

    [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

Alright, maybe the example is a little bit contrived, but hopefully you get the idea.

[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/1edad31ead71e4ec07982c0dd7ac2dc8 "githalytics.com")](http://githalytics.com/nielsmadan/mercury)
