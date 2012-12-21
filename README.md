# mercury

**DISCLAIMER: THIS IS STILL WORK IN PROGRESS. NOT EVERYTHING WORKS (SEE TODO.md).**

`mercury` allows you to take code from some source (current line, selection, buffer), execute the code intelligently
(for example taking care of imports), and then write the result to some destination (message window, selection, register,
new split).

## mappings

Mappings are mnemonic. All mappings start with some configurable start sequence (default: `<leader>r`), followed by one
character that specifies the source, and a second mapping that specifies the destination.

###Sources:

* l = line
* s = selection
* b = buffer

###Destinations:

* r = register
* s = selection
* h = horizontal split
* v = vertical split
* m = message window

###Some examples:

    <leader>rlm - (r)un (l)ine into (m)essage window.
    <leader>rss - (r)un (s)election into (s)election.
    <leader>rbv - (r)un (b)uffer into (v)ertical split.

## Languages supported

Currently only supports python, but adding other languages should be easy, so if you'd like to see your language
supported, have a look into contributing! I'm happy to help.

[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/1edad31ead71e4ec07982c0dd7ac2dc8 "githalytics.com")](http://githalytics.com/nielsmadan/mercury)
