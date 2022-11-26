# O Fortuna

NanoNaNoGenMo 2022 entry that translates fortunes into Latin. The first version had a dependency on a locally-installed version of fortune(1) but this version dispenses with that, instead using the fortune API documented at https://helloacm.com/fortune/.

The code weighs in at 233 bytes, by my count (thanks to pestis for helping with sizecoding). The output is 50,062 words long and took to run (HTTP is inefficient even over fast connections, especially with lots of tiny calls). Google Translate only allows small requests with the free tier, so I couldn't translate it all in one go.

## Code

```Python
import googletrans as g,requests as r
w=0
e='unicode_escape'
while w<5e4:t=g.Translator().translate(r.get('https://api.justyy.workers.dev/api/fortune').text.encode('raw_'+e).decode(e),'la').text.strip('"');print(t);w+=len(t.split())
```

## Sample output

```
Knucklehead: "Pulsate, pulsate";
Pee Wee: "Quis est?"
Knucklehead: "Parva ot domina."
Pee Wee: "Liddle ol' domina quae?"
Knucklehead: "Te non scio yodel"

Femina quam emisti - et minima est pretiosa - magnum accipit
multum pecuniae. Omne tempus tuum mulier quae se donat.
-- Balzac

Si parum astutus es, mitior esses.
-- Benjamin Disraeli

Homines sine ulla condicione praestantur ut vitiis sint pleni.

saccharum tata, n.
Aliquam quis aliquam lacus.

Ne sis pernecessarius, si reponi non potes, promoveri non potes.

QOTD:
"Nescio quid hoc est, sed "F" solum id dignissim.

Est enim moderatio rei fatalis. Nihil proficit sicut intemperantia.
-- Oscar Wilde

…
```

## The Great, er, Latin Novel

Here's the output: [50000 words, right here](o_fortuna.txt).

## Ok, but why?

Fair question. It's an attempt at sizecoding to produce an interesting, non-trivial “novel” that's actually readable (if you can read Latin). There may be duplicate fortunes, depending on the whims of fortune's inherent randomness; if you ask me that's both outside of the scope of this exercise, and also a feature.

## NaNoWhatNow?

See other NaNoGenMo (National Novel Generation Month) entries at https://nanogenmo.github.io

The idea/blame for NanoNaNoGenMo (#NNNGM) lies with Nick Montfort: https://nickm.com/post/2019/11/nano-nanogenmo-or-nnngm/
