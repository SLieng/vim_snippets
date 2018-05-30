"=============================================================================
" FILE: mapping.vim
" AUTHOR:  Shougo Matsushita <Shougo.Matsu at gmail.com>
" License: MIT license
"=============================================================================

function! deoppet#mapping#_init() abort
  inoremap <silent><expr> <Plug>(deoppet_expand)
      \ <SID>trigger('expand')
  inoremap <silent><expr> <Plug>(deoppet_jump_forward)
      \ <SID>trigger('jump_forward')
  inoremap <silent><expr> <Plug>(deoppet_jump_backward)
      \ <SID>trigger('jump_backward')

  " Test
  imap <C-Q>  <Plug>(deoppet_expand)
  imap <C-T>  <Plug>(deoppet_jump_forward)
endfunction


imap <C-Q>  <Plug>(deoppet_expand)
imap <C-X>  <Plug>(deoppet_expand)
imap <C-Y>  <Plug>(deoppet_expand)
imap <C-T>  <Plug>(deoppet_jump_forward)

function! s:pre_trigger() abort
  let cur_text = deoppet#util#_get_cur_text()

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
        \ '_deoppet_mapping', string(a:function))

  return expr
endfunction

call _deoppet_initialize()
