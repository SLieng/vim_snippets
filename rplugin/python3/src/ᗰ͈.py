import neovim

@neovim.plugin
class ᗰ͈():

    def __init__(𝚵, Ѵ):
        𝚵.Ѵ = Ѵ

from src.snp import Deoppet

@neovim.plugin
class DeoppetHandlers(object):

    @neovim.function('_snp_initialize', sync=False)
    def init_channel(self, args):
        self._vim.vars['snp#_channel_id'] = self._vim.channel_id
        self._snp = Deoppet(self._vim)

    @neovim.function('_snp_mapping', sync=True)
    def mapping(self, args):
        self._snp.mapping(args[0])

    @neovim.function('_snp_event', sync=True)
    def event(self, args):
        self._snp.event(args[0])
