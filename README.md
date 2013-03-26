# mercury

`mercury` allows you to take a fragment of code from some source (current line, selection, buffer), execute the code intelligently, and then write the result to some destination (message window, selection, register, new split).

Features include:

 * choose the correct interpreter with the correct switches, given the filetype.
 * execute it in a separate thread and terminate it after a timeout, so an
   endless loop will not freeze vim.
 * some language specific smartness (e.g. handling imports).

## installation

`mercury` requires [venom](https://github.com/nielsmadan/venom), which in turn requires vim to be
compiled with python support (most vim distributions have this). Vundle or pathogen are highly
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

## Languages supported

Currently supports python, ruby and javascript (using node). Adding more languages is easy, so if you'd like to see your language supported, have a look into contributing! I'm happy to help.

[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/1edad31ead71e4ec07982c0dd7ac2dc8 "githalytics.com")](http://githalytics.com/nielsmadan/mercury)
