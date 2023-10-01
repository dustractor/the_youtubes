import pandas as pd
import pathlib
from xml.dom import minidom
import argparse

#{{{1 minidom setup

def _elem_inplace_addition(self,other):
    self.appendChild(other)
    return self

def _elem_textnode(self,text):
    textnode = self.ownerDocument.createTextNode(text)
    self.appendChild(textnode)
    return self

def _elem_set_attributes_from_tuple(self,*args):
    for k,v in args:
        self.setAttribute(k,str(v))
    return self

minidom.Element.__iadd__ = _elem_inplace_addition
minidom.Element.txt = _elem_textnode
minidom.Element.attrt = _elem_set_attributes_from_tuple
minidom.Element.__str__ = lambda s:s.toprettyxml().strip()

#}}}1
args = argparse.ArgumentParser()
args.add_argument("--input",type=pathlib.Path)
ns = args.parse_args()
df = pd.read_excel(ns.input)
doc = minidom.Document()
elem = doc.createElement
root = elem("html")
head = elem("head")
root += head
title = elem("title")
head += title
title.txt(f"{df.iat[0,1]}")
body = elem("body")
root += body
ul = elem("ol")
body += ul

for n in range(5,len(df)):
    ob = df.iloc[n]
    v_id = ob[0]
    v_desc = ob[1]
    v_chan = ob[2]
    li = elem("li")
    ul += li
    p = elem("p")
    li += p
    print("v_chan:",v_chan)
    p.txt(str(v_chan))
    a = elem("a")
    p += a
    a.attrt(("href",f"https://www.youtube.com/watch?v={v_id}"))
    a.txt(v_desc)

output = ns.input.with_suffix(".html")
with open(output,"w",encoding="utf8") as f:
    f.write(str(root))


