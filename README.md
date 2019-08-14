# EGA

amateur translation (French to English) of A. Grothendieck's EGA, starting with EGA I.

S’il-vous plaît pardonnez-nous, Grothendieck.

to compile, `make book`, `make pdfs`, or `make all`.

please do not commit PDF files, instead put `book.pdf` in the `build` release.

click [here](https://github.com/ryankeleti/ega/releases/download/build/book.pdf) for a copy of the compiled version.

## current status

Here is the current status of the translation, along with who is currently working on/has worked on which sections

- [x] Introduction (proofread by @thosgood)
- [ ] Preliminaries
    + [x] 1. Rings of fractions (@ryankeleti) (proofread by @thosgood)
    + [x] 2. Irreducible spaces. Noetherian spaces (@ryankeleti)
    + [x] 3. Supplement on sheaves (@ryankeleti)
    + [x] 4. Ringed spaces (@ryankeleti)
    + [x] 5. Quasi-coherent sheaves and coherent sheaves (@ryankeleti)
    + [x] 6. Flatness (@ryankeleti)
    + [x] 7. Adic rings (@ryankeleti)
    + [ ] 8. Representable functors (@ryankeleti)
    + [ ] 9. Constructible sets
    + [ ] 10. Supplement on flat modules
    + [ ] 11. Supplement on homological algebra
    + [ ] 12. Supplement on sheaf cohomology
    + [ ] 13. Projective limits in homological algebra
    + [ ] 14. Combinatorial dimension of a topological space
    + [ ] 15. M-regular and F-regular sequences
    + [ ] 16. Dimension and depth of Noetherian local rings
    + [ ] 17. Regular rings
    + [ ] 18. Supplement on extensions of algebras
    + [ ] 19. Formally smooth algebras and Cohen rings
    + [ ] 20. Derivations and differentials
    + [ ] 21. Differentials in rings of characteristic p
    + [ ] 22. Differential criteria for smoothness and regularity
    + [ ] 23. Japanese rings
- [ ] The language of schemes
    + [x] 0. Summary
    + [x] 1. Affine schemes (@ryankeleti)
    + [x] 2. Preschemes and their morphisms (@thosgood)
    + [x] 3. Products of preschemes (@thosgood, @ryankeleti)
    + [ ] 4. Subpreschemes and immersions (@thosgood)
    + [ ] 5. Reduced preschemes; separation condition
    + [ ] 6. Finiteness conditions
    + [x] 7. Rational maps (@thosgood)
    + [x] 8. Chevalley schemes (@thosgood)
    + [x] 9. Supplement on quasi-coherent sheaves (@thosgood)
    + [ ] 10. Formal schemes (@thosgood, @ryankeleti)

## todo

- hyperref links to equations (e.g. 3.3.9.1)
- check for any `\unsure` commands in the source
- check that all `hyperref` references are found
- when this is finished (?!) we should [assign a DOI?](https://guides.github.com/activities/citable-code/)
- web version? work in progress
