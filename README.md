# EGA

Community translation (French to English) of A. Grothendieck's EGA.
On est désolé, Grothendieck.

~~View online [here](https://ega.fppf.site/).~~

For discussion regarding this project, visit [#ega:matrix.org](https://matrix.to/#/#ega:matrix.org)!

To compile, `make book`, `make pdfs`, or `make all`.


## PDFs

(All the PDFs are auto-compliled every hour if any changes have been made since the last auto-compile, so will always be up to date with the latest commit --- if two versions have different autobuild times but the same git commit, then they are identical).

Individual volumes can be downloaded separately:

- [What this is](https://fppf.site/ega/what-auto.pdf)
- [Introduction](https://fppf.site/ega/intro-auto.pdf)
- [EGA 0](https://fppf.site/ega/ega0-auto.pdf)
- [EGA I](https://fppf.site/ega/ega1-auto.pdf)
- [EGA II](https://fppf.site/ega/ega2-auto.pdf)
- [EGA III](https://fppf.site/ega/ega3-auto.pdf)
- [EGA IV](https://fppf.site/ega/ega4-auto.pdf)
- [References](https://fppf.site/ega/ref-auto.pdf)

Alternatively, the full document can be downloaded:

- [Book](https://fppf.site/ega/book-auto.pdf)


## Current status

**Summary:**

- [x] EGA I preliminaries
- [x] EGA I
- [ ] EGA II
- [ ] EGA III preliminaries
- [ ] EGA III
- [ ] EGA IV preliminaries
- [ ] EGA IV


**Details:**
Here is the current status of the translation, along with who is currently working on/has worked on which sections. (Page counts and percentages are usually just rough estimates).

### Introduction (EGA I) _(proofread by @thosgood)_ ![introstatus](https://img.shields.io/badge/-5%2F5-brightgreen)

### Preliminaries (EGA 0_I) _(proofread by @thosgood)_ ![EGA0(I)status](https://img.shields.io/badge/-70%2F70-brightgreen)

1. Rings of fractions _(@ryankeleti)_
2. Irreducible spaces. Noetherian spaces _(@ryankeleti)_
3. Supplement on sheaves _(@ryankeleti)_
4. Ringed spaces _(@ryankeleti)_
5. Quasi-coherent sheaves and coherent sheaves _(@ryankeleti)_
6. Flatness _(@ryankeleti)_
7. Adic rings _(@ryankeleti)_

### Preliminaries (EGA 0_III) ![EGA0(III)status](https://img.shields.io/badge/-20%2F75-orange)

+ [x] 8. Representable functors _(@ryankeleti)_
+ [x] 9. Constructible sets _(@ryankeleti)_
+ [x] 10. Supplement on flat modules _(@thosgood)_
+ [ ] 11. Supplement on homological algebra _(@ryankeleti)_
+ [ ] 12. Supplement on sheaf cohomology (~25 pages)
+ [ ] 13. Projective limits in homological algebra (~10 pages)

### Preliminaries (EGA 0_IV) ![EGA0(IV)status](https://img.shields.io/badge/-5%2F215-red)

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

### The language of schemes (EGA I) _(proofread by @thosgood)_ ![EGAIstatus](https://img.shields.io/badge/-136%2F136-brightgreen)

0. Summary
1. Affine schemes _(@ryankeleti)_
2. Preschemes and their morphisms _(@thosgood)_
3. Products of preschemes _(@thosgood, @ryankeleti)_
4. Subpreschemes and immersions _(@ryankeleti)_
5. Reduced preschemes; separation condition _(@thosgood)_
6. Finiteness conditions _(@thosgood)_
7. Rational maps _(@thosgood)_
8. Chevalley schemes _(@thosgood)_
9. Supplement on quasi-coherent sheaves _(@thosgood)_
10. Formal schemes _(@thosgood, @ryankeleti)_

### Elementary global study of some classes of morphisms (EGA II) ![EGAIIstatus](https://img.shields.io/badge/-180%2F205-yellow)

+ [x] 0. Summary _(@ryankeleti / proofread by @thosgood)_
+ [x] 1. Affine morphisms _(@ryankeleti)_
+ [x] 2. Homogeneous prime spectra _(@thosgood)_
+ [x] 3. Homogeneous prime spectrum of a sheaf of graded algebras _(@thosgood)_
+ [x] 4. Projective bundles; Ample sheaves _(@thosgood)_
+ [x] 5. Quasi-affine morphisms; quasi-projective morphisms; proper morphisms; projective morphisms _(@thosgood)_
+ [ ] 6. Integral morphisms and finite morphisms _(@thosgood; https://github.com/ryankeleti/ega/pull/198)_
+ [x] 7. Valuative criteria _(@thosgood)_
+ [x] 8. Blowup schemes; based cones; projective closure _(@thosgood)_
+ [x] Errata and addenda (list 1) _(@thosgood)_

### Cohomological study of coherent sheaves (EGA III) ![EGAIIIstatus](https://img.shields.io/badge/-20%2F160-red)

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
+ [ ] Errata and addenda (list 2)

### Local study of schemes and their morphisms (EGA IV) ![EGAIVstatus](https://img.shields.io/badge/-53%2F825-red)

+ [x] 0. Summary _(@thosgood)_
+ [ ] 1. Relative finiteness conditions. Constructible sets of preschemes (~30 pages)
+ [ ] 2. Base change and flatness (~30 pages)
+ [ ] 3. Associated prime cycles and primary decomposition (~15 pages)
+ [ ] 4. Change of base field for algebraic preschemes (~35 pages)
+ [ ] 5. Dimension, depth, and regularity of locally Noetherian preschemes (~50 pages)
+ [ ] 6. Flat morphisms of locally Noetherian preschemes (~50 pages)
+ [ ] 7. Relations between a local Noetherian ring and its completion. Excellent rings (~40 pages)
+ [ ] 8. Projective limits of preschemes (~50 pages)
+ [ ] 9. Constructible properties (~40 pages)
+ [ ] 10. Jacobson preschemes (~20 pages)
+ [ ] 11. Topological properties of finitely presented flat morphisms. Flatness criteria (~60 pages)
+ [ ] 12. Fibres of finitely presented flat morphisms (~15 pages)
+ [ ] 13. Equidimensional morphisms (~15 pages)
+ [ ] 14. Universally open morphisms (~25 pages)
+ [ ] 15. Fibres of a universally open morphism (~25 pages)
+ [x] 16. Differential invariants. Differentially smooth morphisms _(@solov-t)_ (~50 pages)
+ [ ] 17. Smooth morphisms, unramified morphisms, and étale morphisms _(@tholzschuh)_ (~55 pages)
+ [ ] 18. Supplement on étale morphisms. Henselian local rings and strictly local rings (~75 pages)
+ [ ] 19. Regular immersions and normal flatness (~40 pages)
+ [ ] 20. Meromorphic functions and pseudo-morphisms (~30 pages)
+ [ ] 21. Divisors (~75 pages)
+ [ ] Errata and addenda (list 3)


## To-do (incomplete)

- check errata in EGA III and onwards
- more consistent use of Proposition/Theorem/Definition/whatever in front of `\sref`s
- lists of notation?
- terminology indices?
- hyperref links to equations (e.g. 3.3.9.1)
- check for any `\unsure` commands in the source
- check that all `\hyperref` references are found
- when this is finished (?!) we should [assign a DOI?](https://guides.github.com/activities/citable-code/)
- web version? (work in progress!)
- more detailed style guidelines? (e.g. language, sentence construction, etc.)
- link (M), (G), (T) references
