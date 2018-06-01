"=============================================================================
" FILE: handler.vim
" AUTHOR:  Shougo Matsushita <Shougo.Matsu at gmail.com>
" License: MIT license
"=============================================================================

function! snp#handler#_init() abort
  augroup snp
    autocmd!
    autocmd BufWritePost * call _snp_event('BufWritePost')
  augroup END
endfunction
