from src.ᗰ͈ import ᗰ͈

import neovim
from src.snp import Deoppet


@neovim.plugin
class DeoppetHandlers(object):

    def __init__(self, vim):
        self._vim = vim

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
