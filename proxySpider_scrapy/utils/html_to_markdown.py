# -*- coding: utf-8 -*-

import html2text as ht  # pip install html2text
import os

text_maker = ht.HTML2Text()

'''
html 转 Markdown 工具
'''


class HTMLTOMARKDOWN:
    def acess(self, htmlpage):
        text = text_maker.handle(htmlpage)
        md = text.split('#')  # split post content
        markdown = ""
        for i in range(md.__len__()):
            markdown = markdown + md[i]
        return markdown
