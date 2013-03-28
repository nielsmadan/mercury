import venom
import vim

from mercury import src, dst, execute

venom.py_fn_to_vim_command("MercuryLM", execute.build(src.line, dst.to_message))
venom.py_fn_to_vim_command("MercurySM", execute.build(src.selection, dst.to_message),
                           allow_range=True)
venom.py_fn_to_vim_command("MercuryBM", execute.build(src.buffer, dst.to_message))

venom.py_fn_to_vim_command("MercuryLV", execute.build(src.line, dst.to_vert_split))
venom.py_fn_to_vim_command("MercurySV", execute.build(src.selection, dst.to_vert_split),
                           allow_range=True)
venom.py_fn_to_vim_command("MercuryBV", execute.build(src.buffer, dst.to_vert_split))

venom.py_fn_to_vim_command("MercuryLH", execute.build(src.line, dst.to_hor_split))
venom.py_fn_to_vim_command("MercurySH", execute.build(src.selection, dst.to_hor_split),
                           allow_range=True)
venom.py_fn_to_vim_command("MercuryBH", execute.build(src.buffer, dst.to_hor_split))

venom.py_fn_to_vim_command("MercuryLR", execute.build(src.line, dst.to_register))
venom.py_fn_to_vim_command("MercurySR", execute.build(src.selection, dst.to_register),
                           allow_range=True)
venom.py_fn_to_vim_command("MercuryBR", execute.build(src.buffer, dst.to_register))

venom.py_fn_to_vim_command("MercuryLS", execute.build(src.line, dst.to_selection))
venom.py_fn_to_vim_command("MercurySS", execute.build(src.selection, dst.to_selection),
                           allow_range=True)
venom.py_fn_to_vim_command("MercuryBS", execute.build(src.buffer, dst.to_selection))

if "mercury_no_defaults" in vim.g and vim.g.mercury_no_defaults == "1":
    pass

else:
    if "mercury_leader_seq" in vim.g:
        leader_seq = vim.g.mercury_leader_seq
    else:
        leader_seq = "<leader>r"
        vim.map.vnoremap("%sr" % leader_seq, ":MercurySM<CR>")
        vim.map.nnoremap("%sr" % leader_seq, ":MercuryBM<CR>")

    vim.map.nnoremap("%slm" % leader_seq, ":MercuryLM<CR>")
    vim.map.vnoremap("%ssm" % leader_seq, ":MercurySM<CR>")
    vim.map.nnoremap("%sbm" % leader_seq, ":MercuryBM<CR>")

    vim.map.nnoremap("%slv" % leader_seq, ":MercuryLV<CR>")
    vim.map.vnoremap("%ssv" % leader_seq, ":MercurySV<CR>")
    vim.map.nnoremap("%sbv" % leader_seq, ":MercuryBV<CR>")

    vim.map.nnoremap("%slh" % leader_seq, ":MercuryLH<CR>")
    vim.map.vnoremap("%ssh" % leader_seq, ":MercurySH<CR>")
    vim.map.nnoremap("%sbh" % leader_seq, ":MercuryBH<CR>")

    vim.map.nnoremap("%slr" % leader_seq, ":MercuryLR<CR>")
    vim.map.vnoremap("%ssr" % leader_seq, ":MercurySR<CR>")
    vim.map.nnoremap("%sbr" % leader_seq, ":MercuryBR<CR>")

    vim.map.nnoremap("%sls" % leader_seq, ":MercuryLS<CR>")
    vim.map.vnoremap("%sss" % leader_seq, ":MercurySS<CR>")
    vim.map.nnoremap("%sbs" % leader_seq, ":MercuryBS<CR>")
