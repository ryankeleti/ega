# EGA

![EGA0status](https://img.shields.io/badge/EGA%200-46%25-yellow) ![EGA1status](https://img.shields.io/badge/EGA%20I-100%25-green) ![EGA2status](https://img.shields.io/badge/EGA%20II-20%25-red) ![EGA3status](https://img.shields.io/badge/EGA%20III-3%25-red) ![EGA4status](https://img.shields.io/badge/EGA%20IV-1%25-red)

Community translation (French to English) of A. Grothendieck's EGA.
S’il-vous plaît pardonnez-nous, Grothendieck.

To compile, `make book`, `make pdfs`, or `make all`.

## PDFs
There is the [**full document**](https://fppf.site/ega/book-auto.pdf), or individual sections can be downloaded separately:
- [What this is](https://fppf.site/ega/what-auto.pdf).
- [Introduction](https://fppf.site/ega/intro-auto.pdf).
- [EGA 0](https://fppf.site/ega/ega0-auto.pdf).
- [EGA I](https://fppf.site/ega/ega1-auto.pdf).
- [EGA II](https://fppf.site/ega/ega2-auto.pdf).
- [EGA III](https://fppf.site/ega/ega3-auto.pdf).
- [EGA IV](https://fppf.site/ega/ega4-auto.pdf).
- [References](https://fppf.site/ega/ref-auto.pdf).

All the PDFs are auto-compliled every hour if any changes have been made since the last auto-compile, so will always be up to date with the latest commit.

![lastupdate](https://img.shields.io/github/last-commit/ryankeleti/ega/master)

## Current status

| | First draft | Proofreading |
| ------ | ----------- | ------------ |
| ![EGA0](https://img.shields.io/badge/EGA-0-lightgrey) | ![EGA0fd](https://img.shields.io/badge/-46%25-yellow) | ![EGA0p](https://img.shields.io/badge/-7%25-red)|
| ![EGA1](https://img.shields.io/badge/EGA-1-lightgrey) | ![EGA1fd](https://img.shields.io/badge/-100%25-brightgreen) | ![EGA1p](https://img.shields.io/badge/-60%25-yellow)|
| ![EGA2](https://img.shields.io/badge/EGA-2-lightgrey) | ![EGA2fd](https://img.shields.io/badge/-20%25-red) | ![EGA2p](https://img.shields.io/badge/-0%25-red)|
| ![EGA3](https://img.shields.io/badge/EGA-3-lightgrey) | ![EGA3fd](https://img.shields.io/badge/-3%25-red) | ![EGA3p](https://img.shields.io/badge/-0%25-red)|
| ![EGA4](https://img.shields.io/badge/EGA-4-lightgrey) | ![EGA4fd](https://img.shields.io/badge/-1%25-red) | ![EGA4p](https://img.shields.io/badge/-0%25-red)|

Here is the current status of the translation, along with who is currently working on/has worked on which sections.

- [x] Introduction (EGA I) _(proofread by @thosgood)_
- [x] Preliminaries (EGA 0_I)
    + [x] 1. Rings of fractions _(@ryankeleti / proofread by @thosgood)_
    + [x] 2. Irreducible spaces. Noetherian spaces _(@ryankeleti / proofread by @thosgood)_
    + [x] 3. Supplement on sheaves _(@ryankeleti)_
    + [x] 4. Ringed spaces _(@ryankeleti)_
    + [x] 5. Quasi-coherent sheaves and coherent sheaves _(@ryankeleti)_
    + [x] 6. Flatness _(@ryankeleti)_
    + [x] 7. Adic rings _(@ryankeleti)_
- [ ] Preliminaries (EGA 0_III)
    + [x] 8. Representable functors _(@ryankeleti)_
    + [x] 9. Constructible sets _(@ryankeleti)_
    + [x] 10. Supplement on flat modules _(@thosgood)_
    + [ ] 11. Supplement on homological algebra _(@ryankeleti)_
    + [ ] 12. Supplement on sheaf cohomology
    + [ ] 13. Projective limits in homological algebra
- [ ] Preliminaries (EGA 0_IV)
    + [x] (14-ε). Summary _(@thosgood)_
    + [x] 14. Combinatorial dimension of a topological space _(@thosgood)_
    + [ ] 15. M-regular and F-regular sequences
    + [ ] 16. Dimension and depth of Noetherian local rings
    + [ ] 17. Regular rings
    + [ ] 18. Supplement on extensions of algebras
    + [ ] 19. Formally smooth algebras and Cohen rings
    + [ ] 20. Derivations and differentials
    + [ ] 21. Differentials in rings of characteristic p
    + [ ] 22. Differential criteria for smoothness and regularity
    + [ ] 23. Japanese rings
- [x] The language of schemes (EGA I)
    + [x] 0. Summary _(proofread by @thosgood)_
    + [x] 1. Affine schemes _(@ryankeleti / proofread by @thosgood)_
    + [x] 2. Preschemes and their morphisms _(@thosgood / proofread by @thosgood)_
    + [x] 3. Products of preschemes _(@thosgood, @ryankeleti / proofread by @thosgood)_
    + [x] 4. Subpreschemes and immersions _(@ryankeleti / proofread by @thosgood)_
    + [x] 5. Reduced preschemes; separation condition _(@thosgood)_
    + [x] 6. Finiteness conditions _(@thosgood)_
    + [x] 7. Rational maps _(@thosgood)_
    + [x] 8. Chevalley schemes _(@thosgood / proofread by @thosgood)_
    + [x] 9. Supplement on quasi-coherent sheaves _(@thosgood)_
    + [x] 10. Formal schemes _(@thosgood, @ryankeleti)_
- [ ] Elementary global study of some classes of morphisms (EGA II)
    + [x] 0. Summary _(@ryankeleti / proofread by @thosgood)_
    + [ ] 1. Affine morphisms _(@ryankeleti)_
    + [ ] 2. Homogeneous prime spectra
    + [ ] 3. Homogeneous prime spectrum of a sheaf of graded algebras
    + [ ] 4. Projective bundles; Ample sheaves
    + [x] 5. Quasi-affine morphisms; quasi-projective morphisms; proper morphisms; projective morphisms _(@thosgood)_
    + [ ] 6. Integral morphisms and finite morphisms
    + [ ] 7. Valuative criteria
    + [ ] 8. Blowup schemes; projective cones; projective closure
- [ ] Cohomological study of coherent sheaves (EGA III)
    + [x] 0. Summary _(@thosgood / proofread by @thosgood)_
    + [x] 1. Cohomology of affine schemes _(@ryankeleti)_
    + [ ] 2. Cohomological study of projective morphisms
    + [ ] 3. Finiteness theorem for proper morphisms
    + [ ] 4. The fundamental theorem of proper morphisms. Applications
    + [ ] 5. An existence theorem for coherent algebraic sheaves
    + [ ] 6. Local and global Tor functors; Künneth formula
    + [ ] 7. Base change for homological functors of sheaves of modules
    + [x] 8. ~~The duality theorem for projective bundles~~
    + [x] 9. ~~Relative cohomology and local cohomology; local duality~~
    + [x] 10. ~~Relations between projective cohomology and local cohomology. Formal completion technique along a divisor~~
    + [x] 11. ~~Global and local Picard groups~~
- [ ] Local study of schemes and their morphisms (EGA IV)
    + [x] 0. Summary _(@thosgood)_
    + [ ] 1. Relative finiteness conditions. Constructible sets of preschemes
    + [ ] 2. Base change and flatness
    + [ ] 3. Associated prime cycles and primary decomposition
    + [ ] 4. Change of base field for algebraic preschemes
    + [ ] 5. Dimension, depth, and regularity of locally Noetherian preschemes
    + [ ] 6. Flat morphisms of locally Noetherian preschemes
    + [ ] 7. Relations between a local Noetherian ring and its completion. Excellent rings
    + [ ] 8. Projective limits of preschemes
    + [ ] 9. Constructible properties
    + [ ] 10. Jacobson preschemes
    + [ ] 11. Topological properties of finitely presented flat morphisms. Flatness criteria
    + [ ] 12. Fibres of finitely presented flat morphisms
    + [ ] 13. Equidimensional morphisms
    + [ ] 14. Universally open morphisms
    + [ ] 15. Fibres of a universally open morphism
    + [ ] 16. Differential invariants. Differentially smooth morphisms
    + [ ] 17. Smooth morphisms, unramified morphisms, and étale morphisms
    + [ ] 18. Supplement on étale morphisms. Henselian local rings and strictly local rings
    + [ ] 19. Regular immersions and normal flatness
    + [ ] 20. Meromorphic functions and pseudo-morphisms
    + [ ] 21. Divisors
