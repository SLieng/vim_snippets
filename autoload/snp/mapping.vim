"=============================================================================
" FILE: mapping.vim
" AUTHOR:  Shougo Matsushita <Shougo.Matsu at gmail.com>
" License: MIT license
"=============================================================================

function! snp#mapping#_init() abort
  inoremap <silent><expr> <Plug>(snp_expand)
      \ <SID>trigger('expand')
  inoremap <silent><expr> <Plug>(snp_jump_forward)
      \ <SID>trigger('jump_forward')
  inoremap <silent><expr> <Plug>(snp_jump_backward)
      \ <SID>trigger('jump_backward')

  " Test
  imap <C-Q>  <Plug>(snp_expand)
  imap <C-Z>  <Plug>(snp_jump_forward)
endfunction


imap <C-Q>  <Plug>(snp_expand)
imap <C-X>  <Plug>(snp_expand)
imap <C-Z>  <Plug>(snp_jump_forward)

function! s:pre_trigger() abort
  let cur_text = snp#util#_get_cur_text()

  let col = col('.')
  let expr = ''
  if mode() !=# 'i'
    " Fix column.
    let col += 2
  endif

  return [cur_text, col, expr]
endfunction

function! s:trigger(function) abort
  let [cur_text, col, expr] = s:pre_trigger()

  echo 'adfsafadsfasf'

  let expr .= printf("\<ESC>:call %s(%s)\<CR>",
        \ '_snp_mapping', string(a:function))

  return expr
endfunction

call snp#mapping#_init()
