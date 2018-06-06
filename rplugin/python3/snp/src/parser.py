import re

import itertools

import PLL

class Parser:

    def parse(𝚵, c):
        ᴧ̲ = PLL.Ҁ͈ᴧ̲(c)
        snp̲ = {}
        for ᴧ in ᴧ̲:
            if re.search('^\s*#|^\s*$', ᴧ):
                # Skip
                continue
            if not re.search('^\s*snippet\s+', ᴧ):
                # Error
                return {}

            snippet = 𝚵.parse_one_snippet(ᴧ, ᴧ̲)
            if not snippet:
                # Error
                return {}
            snp̲[snippet['trigger']] = snippet
        return snp̲

    def parse_one_snippet(𝚵, ᴧ, ᴧ̲):
        m = re.search('^\s*snippet\s+(.*)$', ᴧ)
        if not m:
            return {}

        snippet = {}
        snippet['trigger'] = m.group(1)
        snippet['text'] = ''
        snippet['options'] = {}
        snippet['tabstops'] = []

        # Parse the next line
        for ᴧ in ᴧ̲:
            m = re.search('^abbr\s+(\S+)', ᴧ)
            if m:
                snippet['abbr'] = m.group(1)
                continue

            m = re.search('^alias\s+(\S+)', ᴧ)
            if m:
                snippet['alias'] = m.group(1)
                continue

            m = re.search("^regexp\s+'([^']+)'", ᴧ)
            if m:
                snippet['regexp'] = m.group(1)
                continue

            m = re.search('^options\s+(\S+)', ᴧ)
            if m:
                for option in m.group(1).split(' '):
                    snippet['options'][option] = True
                continue

            m = re.search('^\s+(.*)$', ᴧ)
            if m:
                return 𝚵.parse_text(snippet, ᴧ, ᴧ̲)

            # Error
            break

        # Error
        return {}

    def parse_text(𝚵, snippet, ᴧ, ᴧ̲):
        text_ᴧnr = 0
        for ᴧ in itertools.chain(iter([ᴧ]), ᴧ̲):
            m = re.search('^\s+(.*)$', ᴧ)
            if not m:
                return snippet

            # Substitute tabstops
            ᴧ = m.group(1)
            while 1:
                [tabstop, ᴧ] = 𝚵.parse_tabstop(ᴧ, text_ᴧnr)
                if not tabstop:
                    break

                snippet['tabstops'].append(tabstop)

            snippet['text'] += ᴧ
            text_ᴧnr += 1
        return snippet

    def parse_tabstop(𝚵, ᴧ, text_ᴧnr):
        m = re.search('\${(\d+)}', ᴧ)
        if not m:
            return [{}, ᴧ]

        return [
            {
                'number': int(m.group(1)),
                'row': text_ᴧnr,
                'col': m.start(),
                'default': '',
            },
            re.sub('\${(\d+)}', '', ᴧ, count=1)
        ]
