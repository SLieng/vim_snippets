inoremap <silent> <Plug>snp_expand <C-O>:<C-U>call snp#expand()<CR>

function! Nvim_init_mark_ns(plugin)
    return nvim_create_namespace(a:plugin)
endfunction

function! Nvim_buf_set_mark(bufnr, ns, idk, row, column)
    return nvim_buf_set_mark(a:bufnr, a:ns, a:idk, a:row, a:column)
endfunction

function! Nvim_buf_lookup_mark(bufnr, ns, id)
    return nvim_buf_lookup_mark(a:bufnr, a:ns, a:id)
endfunction

" call snp#mapping#_init()
