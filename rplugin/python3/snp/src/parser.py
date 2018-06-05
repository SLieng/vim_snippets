import re

class Parser:

    def __init__(𝚵):
        𝚵.lines = []
        𝚵.linenr = 0
        𝚵.line_max = 0

    def parse(𝚵, text):
        return {
                'xs': 'hello world'
                }
        𝚵.lines = text.splitlines()
        𝚵.linenr = 0
        𝚵.line_max = len(𝚵.lines)

        snippets = {}
        while 𝚵.linenr < 𝚵.line_max:
            line = 𝚵.lines[𝚵.linenr]
            if re.search('^\s*#|^\s*$', line):
                # Skip
                𝚵.linenr += 1
                continue
            if not re.search('^\s*snippet\s+', line):
                # Error
                return {}

            snippet = 𝚵.parse_one_snippet()
            if not snippet:
                # Error
                return {}
            snippets[snippet['trigger']] = snippet
        return snippets

    def parse_one_snippet(𝚵):
        line = 𝚵.lines[𝚵.linenr]
        m = re.search('^\s*snippet\s+(.*)$', line)
        if not m:
            return {}

        snippet = {}
        snippet['trigger'] = m.group(1)
        snippet['text'] = ''
        snippet['options'] = {}
        snippet['tabstops'] = []

        # Parse the next line
        while (𝚵.linenr + 1) < 𝚵.line_max:
            𝚵.linenr += 1

            line = 𝚵.lines[𝚵.linenr]
            m = re.search('^abbr\s+(\S+)', line)
            if m:
                snippet['abbr'] = m.group(1)
                continue

            m = re.search('^alias\s+(\S+)', line)
            if m:
                snippet['alias'] = m.group(1)
                continue

            m = re.search("^regexp\s+'([^']+)'", line)
            if m:
                snippet['regexp'] = m.group(1)
                continue

            m = re.search('^options\s+(\S+)', line)
            if m:
                for option in m.group(1).split(' '):
                    snippet['options'][option] = True
                continue

            m = re.search('^\s+(.*)$', line)
            if m:
                return 𝚵.parse_text(snippet)

            # Error
            break

        # Error
        return {}

    def parse_text(𝚵, snippet):
        text_linenr = 0
        while 𝚵.linenr < 𝚵.line_max:
            line = 𝚵.lines[𝚵.linenr]
            m = re.search('^\s+(.*)$', line)
            if not m:
                return snippet

            # Substitute tabstops
            line = m.group(1)
            while 1:
                [tabstop, line] = 𝚵.parse_tabstop(line, text_linenr)
                if not tabstop:
                    break

                snippet['tabstops'].append(tabstop)

            snippet['text'] += line
            𝚵.linenr += 1
            text_linenr += 1
        return snippet

    def parse_tabstop(𝚵, line, text_linenr):
        m = re.search('\${(\d+)}', line)
        if not m:
            return [{}, line]

        return [
            {
                'number': int(m.group(1)),
                'row': text_linenr,
                'col': m.start(),
                'default': '',
            },
            re.sub('\${(\d+)}', '', line, count=1)
        ]
