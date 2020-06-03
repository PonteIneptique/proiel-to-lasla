import lxml.etree as ET
import regex as re
toks = {}


#def condition(token):
#	if token.getnext() is None and token.getparent().getnext() is not None:#
#		return token.getparent().getnext().get("presentation-after")
#	elif token.getnext() is not None and int(token.getnext().get("id")) != int(token.get("id"))+1:
#				print(ET.tostring(token))
#	else:
#		toks[token] = "#ENCL#"

cite = {}
with open("latin-nt.xml") as f2:
	xml = ET.parse(f2)
	text = " "
	last_cite = None
	for sentence in xml.xpath("//sentence"):
		if sentence.get("presentation-after"):
			text += " "
		for token in sentence.xpath("./token[@form]"):
			cite[token.get("id")] = token.get("citation-part", "")
			if token.get("citation-part") != last_cite:
				text += " "
				last_cite = token.get("citation-part")
			text += f"{token.get('form')}[{token.get('id')}]"+token.get("presentation-after", "")

matches = list(re.findall(r"(\w+)\[(\d+)\](\w+)\[(\d+)\]", text))
clitics = {}
for match in matches:
	if match[0] not in {"ne"} and match[2] not in {"cum", "met", "que", "ve", "ne"}:
		print(match)
	else:
		clitics[match[3]] = "#Enclitic"

# Need a real check for these
	#for token in xml.xpath("//token[@form]"):
	#	if token.get("presentation-after"):
	#		toks[token.get("id")] = token.get("presentation-after")
	#	else:
	#		if token.getnext() is None and token.getparent().getnext() is not None:
	#			toks[token.get("id")] = token.getparent().getnext().get("presentation-after")
	#		elif token.getnext() is not None and int(token.getnext().get("id")) != int(token.get("id"))+1:
	#			print(ET.tostring(token))
	#		else:
	#			toks[token] = "#ENCL#"

#print(len([k.get("form") for k, v in toks.items() if v == "#ENCL#" or v == ""]))
#print(list(set([k.get("id") for k, v in toks.items() if v == "#ENCL#" or v == ""])))
#raise

import re
with open("outputtext.txt", "w") as f:
	f.write(text)
with open("nt-manual.aligned.tsv", "w") as f:
	f.write("form	lemma	POS	morph	id	encl	Cite\n")
	with open("nt-manual.tsv") as f1:
		with open("nt.convert.tsv") as f2:
			lines1 = [
				(nb_line, *line.strip().split("\t"))
				for nb_line, line in enumerate(f1)
				if not line.startswith("$") and nb_line != 0
			]
			lines2 = [
				(nb_line, *line.strip().split("\t"))
				for nb_line, line in enumerate(f2)
				if not line.startswith("$") and nb_line != 0
			]
			for ((nb1, t1, l1, p1, m1), (nb2, t2, l2, p2, m2, i2)) in zip(lines1, lines2):
				if t1 != t2:
					print(nb1, nb2)
					print(t1, t2)
					break
				f.write(f"{t1}\t{l1}\t{p1}\t{m1}\t{i2}\t{clitics.get(i2, '')}\t{cite.get(i2, '')}\n")