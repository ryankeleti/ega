
# Style Guide (WIP)

## General conventions

### Line break style

A translated sentence is put on its own line.
For example, if the source has a line like `Soient X un préschéma.`, write
```latex
 % ... text that came before this sentence ...
Let $X$ be a prescheme.
 % ... text that comes after this sentence ...
```

If the line has a semicolon, i.e., `Soient X un préschéma; soient A un anneau.`, write
```latex
% ... text that came before this sentence ...
Let $X$ be a prescheme;
let $A$ be a ring.
% ... text that comes after this sentence ...
```

Separate paragraphs with a single blank line.

Avoid using `\\` when possible. If necessary, for example inside an `align` environment, write
```latex
...\\
...
```
i.e., end the line with the `\\`.


### Indentation style

In the following, `␣` denotes a single blank space.

**Do not use tabs**; instead, use 2 spaces (`␣␣`). Many editors have a setting for tabs to be inserted as a number of spaces.

 Place `\begin` and `\end` pairs on new lines:
```latex
\begin{environment}
Text text text.
\end{environment}
```

If there is a nested environment, use the following format:
```latex
\begin{environment1}
␣␣\begin{environment2}
␣␣...
␣␣\end{environment2}
\end{environment1}
```

And so on:
```latex
\begin{environment1}
␣␣\begin{environment2}
␣␣␣␣\begin{environment3}
␣␣␣␣...
␣␣␣␣\end{environment3}
␣␣\end{environment2}
\end{environment1}
```

For `enumerate` environments, use the following format:
```latex
\begin{enumerate}
␣␣\item ...
␣␣\item ...
␣␣...
\end{enumerate}
```

If there is another sentence after an `\item`, use the following format:
```latex
\begin{enumerate}
␣␣\item This is a sentence.
␣␣␣␣This is another sentence.
␣␣␣␣Another one?
␣␣\item ...
␣␣...
\end{enumerate}
```

For equations, write
```latex
\[
␣␣equation
\]
```

If an equation needs a tag, write
```latex
\[
\label{R.x.y.z.n}
␣␣equation
␣␣\tag{x.y.z.n}
\]
```
where `x.y.z.n` is the tag, and `R` the volume number.

### Environment style

The custom environment styles are
* `env`
* `theorem`
* `proposition`
* `lemma`
* `corollary`
* `definition`
* `example`
* `remark`
* `notation`

Use `env` for the general environments labeled `(x.y.z)` in the text.

To write an environment, use the following format:
```latex
\begin{env}[x.y.z]
\label{R.x.y.z}
...
\end{env}
```
Here, `x.y.z` refers to the label in the text denoted `(x.y.z)`.
The `R` refers to the Roman numeral associated to the volume:
* `0` for EGA 0
* `I` for EGA I
* `II` for EGA II
* `III` for EGA III
* `IV` for EGA IV

Similarly for `theorem`, etc.:
```latex
\begin{theorem}[x.y.z]
\label{R.x.y.z}
...
\end{theorem}
```

### Proof enviroments

Use
```latex
\begin{proof}
...
\end{proof}
```
for a proof environment (no `\label` needed).

If a proof begins directly with an `enumerate` environment, then use
```latex
\begin{proof}
\medskip\noindent
\begin{enumerate}
  ...
\end{enumerate}
\end{proof}
```


### Oldpage

Use
```latex
\oldpage[R]{n}
```
to denote the page number in the original text.
Here `R` represents the current volume's Roman numeral (as above), and `n` is the page of the original text.
In the case of volumes with multiple parts (such as EGA IV, Part 1, etc.), use
```latex
\oldpage[R-m]{n}
```
where `m` is the part number of volume `R`.
Here `n` refers to the page numbering in part `m`, instead of the overall volume.

Insert an `\oldpage` whenever the original text has a page transition (even mid-sentence).
Always place `\oldpage` on a new line, and at the start of the line.

For example, write
```latex
Hi! Schemes
\oldpage[II]{42}
are cool.
```
if in EGA II, page 41 ends with `Hi! Schemes` and page 42 begins with `are cool.`.


## Available commands

### Font commands

* `\sh` --- the sheaf font; use for general sheaves
  - example: `\sh{F}` for a sheaf F
* `\bb` --- the bold font; use for "blackboard bold" type characters
  - example: `\bb{Z}` for the ring of integers
* `\cat` --- the category font; use for general categories
  - example: `\cat{D}` for a category D
  - example: `\C` is defined to be `\cat{C}` for a category C

### Operators

* `\rg`
* `\gr`
* `\Hom`
* `\Proj`
* `\Tor`
* `\Ext`
* `\Supp`
* `\Ker`
* `\Im`
* `\Coker`
* `\Spec`
* `\Spf`
* `\grad`
* `\dimc`
* `\codim`
* `\id`

#### Sheaf operators
* `\shHom`
* `\shProj`
* `\shExt`
* `\shGr`

### Category names
* `\Set` --- the category of sets
* `\CHom` --- a hom category, i.e. `\CHom(A, B)`

### Miscellaneous
* `\vphi` --- phi `φ`
* `\emp` --- empty set `∅`
* `\dual` --- for the dual sheaf, i.e. `\dual{\sh{F}}` for F<sup>v</sup>
* `\rad` --- radical
* `\nilrad` --- nilradical
* `\setmin` --- set minus/difference
* `\HH` --- cohomology H
* `\CHH` --- Čech cohomology H
* `\RR` --- right derived R
* `\LL` --- left derived L
* `\kres` --- residue field k
* `\op` --- opposite category, i.e. `\cat{C}\op` for C<sup>op</sup>
* `\red` --- reduced, i.e. `X_\red` for X<sub>red</sub>
* `\supertilde` --- for when `\widetilde{}` is used as a subscript, i.e. `\sh{F}\supertilde` instead of `\sh{F}^\sim` (note the lack of `^`)
* `\bullet` --- to be used instead of `*` when denoting a grading, e.g. `A_\bullet` instead of `A_*` for a graded module
* `\widehat` and `\widetilde` --- to be used instead of `\hat` and `\tilde` (which have been redefined to mean this anyway)

## References

Use `\sref` for references to other environments in the document.

For example, within EGA R, to reference environment `(x.y.z)` from EGA R, use
```latex
Here's a reference: \sref{R.x.y.z}...
```

Within EGA R, to reference environment `(x.y.z)` in a different volume EGA R', use
```latex
Here's a reference: \sref[R']{R'.x.y.z}...
```

If you want to reference a listed item within an environment, i.e. `(i)` of `(x.y.z)`, use
```latex
Here's a reference: \sref{R.x.y.z}[(i)]
```

The general syntax is
```latex
\sref[R]{R.x.y.z}[...]
```
where `[R]` and `[...]` are optional.
Here `R` denotes the Roman numeral corresponding to the EGA volume in which the reference is found.
Inside `[...]`, one can write anything, such as `(i) and (v)`.

Use `[R]` when referencing an environment outside the current volume.
If the reference is within the current volume, omit the `[R]`.

