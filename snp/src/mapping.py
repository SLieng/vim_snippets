from src.util import debug


class Mapping():

    def __init__(self, vim):
        self._vim = vim
        self.clear()

    def debug(self, expr):
        return debug(self._vim, expr)

    def clear(self):
        self._ns = self._vim.call('Nvim_init_mark_ns', 'snp')
        self._vim.current.buffer.vars['snp_marks'] = []

    def mapping(self, name):
        bvars = self._vim.current.buffer.vars
        if 'snp_marks' not in bvars:
            bvars['snp_marks'] = []
        if 'snp_snippets' not in bvars:
            return

        if name == 'clear':
            return self.clear()
        if name == 'expand':
            return self.expand()
        if name == 'jump_forward':
            return self.jump(True)
        if name == 'jump_backward':
            return self.jump(False)
        return

    def expand(self):
        bvars = self._vim.current.buffer.vars
        snippets = bvars['snp_snippets']
        cur_text = self._vim.call('snp#util#_get_cur_text')
        trigger = self._vim.call('snp#util#_get_cursor_snippet',
                                 snippets, cur_text)
        if not trigger:
            return

        # Expand trigger
        cursor = self._vim.current.window.cursor
        linenr = cursor[0]
        buf = self._vim.current.buffer
        snippet = snippets[trigger]
        cur_text = cur_text[: len(cur_text) - len(trigger)]
        next_text = self._vim.call('snp#util#_get_next_text')
        # debug(self._vim, cur_text)
        # debug(self._vim, snippet['trigger'])
        # debug(self._vim, next_text)
        buf[linenr-1] = cur_text + snippet['text'] + next_text
        col = self._vim.call('len', cur_text + snippet['text'])

        ids = []
        self._ns = self._vim.call('Nvim_init_mark_ns', 'snp')
        for tabstop in snippet['tabstops']:
            ids.append(self._vim.call('Nvim_buf_set_mark',
                                      buf.number, self._ns, 0,  # 0 for self._ns
                                      tabstop['row'] + linenr,
                                      tabstop['col'] + 1))
        bvars['snp_marks'] = ids + bvars['snp_marks']
        self.cursor(linenr, col, next_text)

    def jump(self, is_forward):
        bvars = self._vim.current.buffer.vars
        if not bvars['snp_marks']:
            self.nop()
            return
        buf = self._vim.current.buffer
        marks = bvars['snp_marks']
        mark = self._vim.call('Nvim_buf_lookup_mark',
                              buf.number, self._ns, marks[0])  # 0 for self._ns
        # Insert mode offset
        mark[2] -= 1
        next_text = buf[mark[1]-1][mark[2]:]
        self.cursor(mark[1], mark[2], next_text)
        bvars['snp_marks'] = marks[1:] + [marks[0]]

    def nop(self):
        return self.cursor(self._vim.current.window.cursor[0],
                           self._vim.current.window.cursor[1],
                           self._vim.call('snp#util#_get_next_text'))

    def cursor(self, linenr, col, next_text):
        # self.debug(next_text)
        if next_text:
            self._vim.call('cursor', [linenr, col + 1])
            self._vim.command('startinsert')
        else:
            self._vim.call('cursor', [linenr, col])
            self._vim.command('startinsert!')
