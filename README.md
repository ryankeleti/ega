# EGA I

amateur translation (French to English) of A. Grothendieck's EGA I.
S’il-vous plaît pardonnez-nous, Grothendieck.

to compile, `make book`, `make pdfs`, or `make all`.

please do not commit PDF files, instead put `book.pdf` in the `build` release.

click [here](https://github.com/ryankeleti/ega/releases/download/build/book.pdf) for a copy of the compiled version.

## current status

Here is the current status of the translation, along with who is currently working on which sections

- [x] Introduction
- [ ] Preliminaries
    + [x] 1. Rings of fractions (@ryankeleti)
    + [x] 2. Irreducible spaces. Noetherian spaces (@ryankeleti)
    + [x] 3. Supplement on sheaves (@ryankeleti)
    + [x] 4. Ringed spaces (@ryankeleti)
    + [x] 5. Quasi-coherent sheaves and coherent sheaves (@ryankeleti)
    + [x] 6. Flatness (@ryankeleti)
    + [ ] 7. Adic rings
    + [ ] 8. Representable functors
- [ ] The language of schemes
    + [x] 0. Summary
    + [x] 1. Affine schemes (@ryankeleti)
    + [x] 2. Preschemes and their morphisms
    + [ ] 3. Products of preschemes (@thosgood)
    + [ ] 4. Subpreschemes and immersions
    + [ ] 5. Reduced preschemes; separation conditions
    + [ ] 6. Finiteness conditions
    + [ ] 7. Rational maps
    + [x] 8. Chevalley schemes
    + [x] 9. Supplement on quasi-coherent sheaves
    + [ ] 10. Formal schemes

## todo

- hyperref links to equations (e.g. 3.3.9.1)
- check for any `\unsure` commands in the source
- check that all `hyperref` references are found
- when this is finished (?!) we should [assign a DOI?](https://guides.github.com/activities/citable-code/)
- reference for section titles [this](https://stacky.net/wiki/index.php?title=EGA_contents)
- web version? work in progress

## resources for contributors

- the notes [here](https://math.berkeley.edu/~mhaiman/math256-fall18-spring19/) are extremely helpful
- an excellent reference for math terms in French [here](http://www-users.math.umn.edu/~kwlan/documents/french-glossary.pdf)
- another reference for math terms in French [here](https://ensiwiki.ensimag.fr/index.php?title=Lexique_scientifique_fran%C3%A7ais-anglais)

## LaTeX conventions
- `\sh` for sheaves, e.g. `\sh{F}` for a sheaf F; use `\OO` for the structure sheaf.
- `\bb` for bold letters, e.g. `\bb{Z}` for the ring of integers.
- `\cat` for categories, e.g. `\cat{Set}` for the category of sets; use `\C` for a "default" category, and `\op` for the opposite category.
- `\dual` for the dual sheaf, e.g. `\dual{\sh{F}}` for `\sh{F}^\vee`.
- `\isoto` for an isomorphism arrow.
- `\emp` for the empty set.
- `\kres` for the residue field.
- `\rad`/`\nilrad` for radical/nilradical.
- `\vphi` for `\varphi`. This is due to the font configuration swapping `\varphi` and `\phi`; if you want to use a different font, you could change this.
- `\HH` for cohomology.
- `\leqslant`/`\geqslant` for ≤, ≥.
- Use the operators defined in `preamble.tex`, such as `\Spec`, `\im`, `\shHom`, etc.
- Use `\oldpage{x}` to mark the original page number (x) at the current text position.

