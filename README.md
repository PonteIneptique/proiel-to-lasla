# Proiel-to-lasla

## Source

> Dag T. T. Haug and Marius L. Jøhndal. 2008. 'Creating a Parallel Treebank of the Old Indo-European Bible Translations'. In Caroline Sporleder and Kiril Ribarov (eds.). Proceedings of the Second Workshop on Language Technology for Cultural Heritage Data (LaTeCH 2008) (2008), pp. 27-34.

## License

As people should, we respect and redistribute the data in the same licence as [Proiel](https://github.com/proiel/proiel-treebank/commit/f23108682d1d4d8f50d96014f886cf476811453a): [CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/)

## Explanation

I tried to align the Proiel Vulgate to LASLA/ENC format and lemma base.

All lemma that were not know to the [Forcellini Online Open Dictionary for lemmatization](https://lascivaroma.github.io/forcellini-lemmas/index.html) were carefully added after looking at Forcellini Onomasticon and Forcellini base dictionary.

Morphology and POS have been checked. There might remain issue, but according to the authorized form we can find on [Pyrrha](https://dh.chartes.psl.eu/pyrrha/) and [PyrrhaCI](https://github.com/hipster-philology/pyrrhaCI), no errors remains. It does not mean that some things were not agreeing with how LASLA tagged their own data.

Thanks to Simon Gabay for his hand on searching *new* lemma in the Forcellini. There was around 700 lemma to look for manually...

## Files

### Input

- dictionary.tsv : Forcellini Pyrrha dictionary at the time of compute

### Conversion 

- latin-nt.xml
- NT.ipynb : semi-manual conversion of data, based on the Forcellini data we had and the information I found in the LASLA corpora. Some disambiguation were clear, some were not.
	- This file was used to detect unknown lemmata.
- nt.convert.tsv is the direct output (except an edited token) from NT.ipynb


### Output

- nt-manual.tsv : Data fixed and checked manual on Pyrrha and with PyrrhaCI
- realign_token.py : File to realign and reinject token IDS, clitics information and citation information
- **nt-manual.aligned.tsv: Output of the alignement (CANON FILE)**


### New lemmata

- ProielToLaslaNouns.tsv contains proper names that were not in LASLA data
- ProielToLasla.tsv contains all the rest of the information. 