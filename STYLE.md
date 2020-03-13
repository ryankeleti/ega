
# Style Guide (WIP)

## General conventions

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


### Oldpage

Use
```latex
\oldpage[R]{n}
```
to denote the page number in the original text.
Here `R` represents the current volume's Roman numeral (as above), and `n` is the page of the original text.

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

* `\sh` --- the sheaf font; use for general sheaves.
  - example: `\sh{F}` for a sheaf F
* `\bb` --- the bold font; use for "blackboard bold" type characters.
  - example: `\bb{Z}` for the ring of integers
* `\cat` --- the category font; use for general categories.
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

### Category names
