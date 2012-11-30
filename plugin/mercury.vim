call venom#Load()

let s:sfile = expand("<sfile>")

" call venom#Import(s:sfile, "mercury")

py << END_PY
import venom

# if venom.include_guard("mercury"):
venom.run(vim.eval("s:sfile"), "mercury")
END_PY
