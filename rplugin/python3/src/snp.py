# ============================================================================
# FILE: snp.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

from src.parser import Parser
from src.mapping import Mapping
from src.util import globruntime
#~ from snp.util import debug


class Deoppet():

    def __init__(self, vim):
        self._vim = vim
        self._parser = Parser()
        self._mapping = Mapping(self._vim)
        self._snippets = {}

        for filename in globruntime(self._vim.options['runtimepath'], 'snippets/*.snip'):
            #~ debug(self._vim, filename)
            with open(filename) as f:
                self._snippets.update(self._parser.parse(f.read()))
        self._vim.current.buffer.vars['snp_snippets'] = self._snippets

        self._vim.call('snp#mapping#_init')
        self._vim.call('snp#handler#_init')

    def mapping(self, name):
        return self._mapping.mapping(name)

    def event(self, name):
        return self._mapping.clear()
