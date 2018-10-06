# en.ega.i

amateur translation (fr->en) of A. Grothendieck's EGA I.
S’il te plaît pardonne-moi, Grothendieck.

work in progress.

to compile, `pdflatex main.tex` or use `make all`

see `CONTRIBUTING.md` if you want to contribute

## todo

- add original page numbers in the margins here? might make it easier for people to find references if they were originally give by page number [done, use
`\oldpage{x}`]
- search within the .tex files for any `TODO` comments
- examples should _not_ be italicised
- when this is finished (?!) we should [assign a DOI ?](https://guides.github.com/activities/citable-code/)
- make a list of the commands defined in `commands.tex` and give examples of where they are found in the original text, so that people can check this whenever translating, to ensure consistency of notation
- update the titles to agree with [this](https://stacky.net/wiki/index.php?title=EGA_contents) ? even if not, this is a good reference for potentially unfamiliar vocabulary

## current status

See `CONTRIBUTING.md` for what people are currently working on.

- [x] Introduction
- [ ] Preliminaries
    + [x] 1. Rings of fractions
    + [x] 2. Irreducible spaces. Noetherian spaces
    + [ ] 3. Supplement on sheaves
    + [ ] 4. Ringed spaces
    + [ ] 5. Quasi-coherent sheaves and coherent sheaves
    + [ ] 6. Flatness
    + [ ] 7. Adic rings
- [ ] The language of schemes
    + [x] 0. Summary
    + [ ] 1. Affine schemes
    + [x] 2. Preschemes and their morphisms
    + [ ] 3. Products of preschemes
    + [ ] 4. Sub preschemes and immersions
    + [ ] 5. Reduced preschemes; separation conditions
    + [ ] 6. Finiteness conditions
    + [ ] 7. Rational maps
    + [x] 8. Chevalley schemes
    + [ ] 9. Supplement on quasi-coherent sheaves (@thosgood)
    + [ ] 10. Formal schemes

