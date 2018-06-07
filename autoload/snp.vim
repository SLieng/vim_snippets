function! snp#init()
    call SNP_init()
    let g:snpInit = 1
endfunction

function! snp#preTrigger()
    let line = getline('.')
    return line
endfunction

function! snp#expand()
    if !exists('g:snpInit')
        call snp#init()
    endif
    let line = snp#preTrigger()
    let a = SNP_expand(line)
    echom a
    echom a
    echom a
endfunction
