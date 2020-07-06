# EGA

Community translation (French to English) of A. Grothendieck's EGA.
S’il-vous plaît pardonnez-nous, Grothendieck.

View online [here](https://ega.fppf.site/).

For discussion regarding this project, visit [#ega:matrix.org](https://riot.im/app/#/room/#ega:matrix.org)!

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

## Current status

Here is the current status of the translation, along with who is currently working on/has worked on which sections. (Page counts and percentages are usually just rough estimates).

- **Introduction (EGA I)** _(proofread by @thosgood)_ ![introstatus](https://img.shields.io/badge/-5%2F5-brightgreen)
- **Preliminaries (EGA 0_I)** _(proofread by @thosgood)_ ![EGA0(I)status](https://img.shields.io/badge/-70%2F70-brightgreen)
    + [x] 1. Rings of fractions _(@ryankeleti)_
    + [x] 2. Irreducible spaces. Noetherian spaces _(@ryankeleti)_
    + [x] 3. Supplement on sheaves _(@ryankeleti)_
    + [x] 4. Ringed spaces _(@ryankeleti)_
    + [x] 5. Quasi-coherent sheaves and coherent sheaves _(@ryankeleti)_
    + [x] 6. Flatness _(@ryankeleti)_
    + [x] 7. Adic rings _(@ryankeleti)_
- **Preliminaries (EGA 0_III)** ![EGA0(III)status](https://img.shields.io/badge/-20%2F75-orange)
    + [x] 8. Representable functors _(@ryankeleti)_
    + [x] 9. Constructible sets _(@ryankeleti)_
    + [x] 10. Supplement on flat modules _(@thosgood)_
    + [ ] 11. Supplement on homological algebra _(@ryankeleti)_
    + [ ] 12. Supplement on sheaf cohomology (~25 pages)
    + [ ] 13. Projective limits in homological algebra (~10 pages)
- **Preliminaries (EGA 0_IV)** ![EGA0(IV)status](https://img.shields.io/badge/-5%2F215-red)
    + [x] (14-ε). Summary _(@thosgood)_
    + [x] 14. Combinatorial dimension of a topological space _(@thosgood)_
    + [ ] 15. M-regular and F-regular sequences (~10 pages)
    + [ ] 16. Dimension and depth of Noetherian local rings (~15 pages)
    + [ ] 17. Regular rings (~15 pages)
    + [ ] 18. Supplement on extensions of algebras (~20 pages)
    + [ ] 19. Formally smooth algebras and Cohen rings (~45 pages)
    + [ ] 20. Derivations and differentials (~35 pages)
    + [ ] 21. Differentials in rings of characteristic p (~30 pages)
    + [ ] 22. Differential criteria for smoothness and regularity (~30 pages)
    + [ ] 23. Japanese rings (~5 pages)
- **The language of schemes (EGA I)** _(proofread by @thosgood)_ ![EGAIstatus](https://img.shields.io/badge/-136%2F136-brightgreen)
    + [x] 0. Summary
    + [x] 1. Affine schemes _(@ryankeleti)_
    + [x] 2. Preschemes and their morphisms _(@thosgood)_
    + [x] 3. Products of preschemes _(@thosgood, @ryankeleti)_
    + [x] 4. Subpreschemes and immersions _(@ryankeleti)_
    + [x] 5. Reduced preschemes; separation condition _(@thosgood)_
    + [x] 6. Finiteness conditions _(@thosgood)_
    + [x] 7. Rational maps _(@thosgood)_
    + [x] 8. Chevalley schemes _(@thosgood)_
    + [x] 9. Supplement on quasi-coherent sheaves _(@thosgood)_
    + [x] 10. Formal schemes _(@thosgood, @ryankeleti)_
- **Elementary global study of some classes of morphisms (EGA II)** ![EGAIIstatus](https://img.shields.io/badge/-105%2F205-yellow)
    + [x] 0. Summary _(@ryankeleti / proofread by @thosgood)_
    + [x] 1. Affine morphisms _(@ryankeleti)_
    + [ ] 2. Homogeneous prime spectra (~30 pages)
    + [ ] 3. Homogeneous prime spectrum of a sheaf of graded algebras (~20 pages)
    + [ ] 4. Projective bundles; Ample sheaves (~20 pages) _(@thosgood)_
    + [x] 5. Quasi-affine morphisms; quasi-projective morphisms; proper morphisms; projective morphisms _(@thosgood)_
    + [ ] 6. Integral morphisms and finite morphisms (~25 pages)
    + [x] 7. Valuative criteria _(@thosgood)_
    + [x] 8. Blowup schemes; based cones; projective closure _(@thosgood)_
    + [x] _Errata and addenda (list 1)_
- **Cohomological study of coherent sheaves (EGA III)** ![EGAIIIstatus](https://img.shields.io/badge/-20%2F160-red)
    + [x] 0. Summary _(@thosgood / proofread by @thosgood)_
    + [x] 1. Cohomology of affine schemes _(@ryankeleti)_
    + [ ] 2. Cohomological study of projective morphisms (~15 pages)
    + [x] 3. Finiteness theorem for proper morphisms _(@ryankeleti)_
    + [ ] 4. The fundamental theorem of proper morphisms. Applications (~30 pages)
    + [ ] 5. An existence theorem for coherent algebraic sheaves (~10 pages)
    + [ ] 6. Local and global Tor functors; Künneth formula (~40 pages)
    + [ ] 7. Base change for homological functors of sheaves of modules (~30 pages)
    + [x] 8. ~~The duality theorem for projective bundles~~
    + [x] 9. ~~Relative cohomology and local cohomology; local duality~~
    + [x] 10. ~~Relations between projective cohomology and local cohomology. Formal completion technique along a divisor~~
    + [x] 11. ~~Global and local Picard groups~~
    + [ ] _Errata and addenda (list 2)_
- **Local study of schemes and their morphisms (EGA IV)** ![EGAIVstatus](https://img.shields.io/badge/-1%2F1100-red)
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
    + [ ] 16. Differential invariants. Differentially smooth morphisms _(@solov-t)_
    + [ ] 17. Smooth morphisms, unramified morphisms, and étale morphisms _(@tholzschuh)_
    + [ ] 18. Supplement on étale morphisms. Henselian local rings and strictly local rings
    + [ ] 19. Regular immersions and normal flatness
    + [ ] 20. Meromorphic functions and pseudo-morphisms
    + [ ] 21. Divisors
