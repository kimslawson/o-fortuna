# O Fortuna

Nano-NaNoGenMo22 entry that translates fortunes into Latin. 

The code weighs in at 239 bytes, by my count (though it could probably be shortened by a more experienced Pythonista) and the output is 50,062 words long.

## Code

```Python
from googletrans import Translator
import subprocess
w=0
while w<50000:
    f=subprocess.check_output(['fortune']).decode('utf-8')
    t=Translator()
    r=t.translate(f, dest='la')
    print(r.text, end='\n\n')
    w+=len(r.text.split())
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

## Ok, but why?

Fair question. It's an attempt at sizecoding to produce an interesting, non-trivial “novel” that's actually readable (if you can read Latin). There may be duplicate fortunes, depending on the whims of fortune's inherent randomness; if you ask me that's both outside of the scope of this exercise, and also a feature.

## NaNoWhatNow?

See other NaNoGenMo (National Novel Generation Month) entries at https://nanogenmo.github.io

The idea/blame for NanoNaNoGenMo (#NNNGM) lies with Nick Montfort: https://nickm.com/post/2019/11/nano-nanogenmo-or-nnngm/
