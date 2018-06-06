import neovim

import TTL
import PAL
import PYL

from snp.src.parser import Parser

import LZL

snpѪ = PAL.ѫ͈('~/scr/snp')

@neovim.plugin
class ᗰ͈(metaclass=TTL.AllѵΣ):

    def __init__(𝚵, Ѵ):
        𝚵.Ѵ = Ѵ

    def loadSnp̲(𝚵):
        𝚵.snp̲ = {}
        𝚵.parser = Parser()
        for ѫ in PYL.file(snpѪ):
            if ѫ.ƨ.endswith('bak'):
                continue
            LZL.echom(𝚵.Ѵ, ѫ.ƨ)
            with open(ѫ.ƨ) as ӻ:
                𝚵.snp̲.update(𝚵.parser.parse(ӻ.read()))

        LZL.echo(𝚵.Ѵ, 𝚵.snp̲)
        #~ 𝚵.Ѵ.out_write(str(𝚵.snp̲))

    #~ @neovim.function('snp#r#initialize', sync=False)
    #~ def init_channel(self, args):
        #~ self._vim.vars['snp#_channel_id'] = self._vim.channel_id
        #~ self._snp = Deoppet(self._vim)

#~ from src.snp import Deoppet

#~ @neovim.plugin
#~ class DeoppetHandlers(object):

#~     @neovim.function('_snp_initialize', sync=False)
#~     def init_channel(self, args):
#~         self._vim.vars['snp#_channel_id'] = self._vim.channel_id
#~         self._snp = Deoppet(self._vim)

#~     @neovim.function('_snp_mapping', sync=True)
#~     def mapping(self, args):
#~         self._snp.mapping(args[0])

#~     @neovim.function('_snp_event', sync=True)
#~     def event(self, args):
#~         self._snp.event(args[0])
