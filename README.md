# en.ega

amateur translation (fr->en) of A. Grothendieck's EGA.
S’il-vous plaît pardonnez-nous, Grothendieck.

to compile, `pdflatex en.ega.main.tex` or use `make all`.

click [here](https://ryankeleti.github.io/en.ega/en.ega.main.pdf) for a copy of the compiled version.

work in progress. see [here](https://github.com/ryankeleti/ega) for a French transciption project.

## todo

- search within the .tex files for any `TODO` comments
- when this is finished (?!) we should [assign a DOI ?](https://guides.github.com/activities/citable-code/)
- update the titles to agree with [this](https://stacky.net/wiki/index.php?title=EGA_contents) ? even if not, this is a good reference for potentially unfamiliar vocabulary
- the notes [here](https://math.berkeley.edu/~mhaiman/math256-fall18-spring19/) are extremely helpful
- an excellent reference for math terms in French [here](http://www-users.math.umn.edu/~kwlan/documents/french-glossary.pdf)
- another reference for math terms in French [here](https://ensiwiki.ensimag.fr/index.php?title=Lexique_scientifique_fran%C3%A7ais-anglais)
- web version? (this currently does not work, I've removed plastex parts for now)

## current status

Here is the current status of the translation, along with the main contributors to the respective sections.

- [x] Introduction
- [ ] Preliminaries
    + [x] 1. Rings of fractions (@ryankeleti)
    + [x] 2. Irreducible spaces. Noetherian spaces (@ryankeleti)
    + [x] 3. Supplement on sheaves (@ryankeleti)
    + [x] 4. Ringed spaces (@ryankeleti)
    + [x] 5. Quasi-coherent sheaves and coherent sheaves (@ryankeleti)
    + [x] 6. Flatness (@ryankeleti)
    + [ ] 7. Adic rings
- [ ] The language of schemes
    + [x] 0. Summary
    + [x] 1. Affine schemes (@ryankeleti)
    + [x] 2. Preschemes and their morphisms (@thosgood)
    + [ ] 3. Products of preschemes
    + [ ] 4. Subpreschemes and immersions
    + [ ] 5. Reduced preschemes; separation conditions
    + [ ] 6. Finiteness conditions
    + [ ] 7. Rational maps
    + [x] 8. Chevalley schemes (@thosgood)
    + [ ] 9. Supplement on quasi-coherent sheaves (@thosgood)
    + [ ] 10. Formal schemes


## LaTeX conventions
- `\sh` for sheaves, e.g. `\sh{F}` for a sheaf F; use `\OO` for the structure sheaf.
- `\bb` for bold letters, e.g. `\bb{Z}` for the ring of integers.
- `\cat` for categories, e.g. `\cat{C}` for a category C; use `\K` for a "default" category.
- `\dual` for the dual sheaf, e.g. `\dual{\sh{F}}` for `\sh{F}^\vee.
- `\isoto` for an isomorphism arrow.
- `\emp` for the empty set.
- `\kres` for the residue field.
- `\rad`/`\nilrad` for radical/nilradical.
- `\vphi` for `\varphi`. This is due to the font configuration swapping `\varphi` and `\phi`; if you want to use a different font, you could change this.
- `\HH` for cohomology.
- `\leqslant`/`\geqslant` for <=, >=.
- Use the operators defined in `preamble.sty`, such as `\Spec`, `\im`, `\shHom`, etc.
- Use `\oldpage{x}` to mark the original page number (x) at the current text position.


