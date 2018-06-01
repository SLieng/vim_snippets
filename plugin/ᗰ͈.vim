"=============================================================================
" FILE: deoppet.vim
" AUTHOR:  Shougo Matsushita <Shougo.Matsu at gmail.com>
" License: MIT license
"=============================================================================
if exists('g:loaded_deoppet')
  finish
endif
let g:loaded_deoppet = 1

function! Nvim_init_mark_ns(plugin)
    return nvim_create_namespace(a:plugin)
endfunction

function! Nvim_buf_set_mark(bufnr, ns, idk, row, column)
    return nvim_buf_set_mark(a:bufnr, a:ns, a:idk, a:row, a:column)
endfunction

function! Nvim_buf_lookup_mark(bufnr, ns, id)
    return nvim_buf_lookup_mark(a:bufnr, a:ns, a:id)
endfunction

call deoppet#mapping#_init()
