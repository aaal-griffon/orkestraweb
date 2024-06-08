def eklenecek_br(sözler):
  """
  Girdi olarak şarkı sözlerini alan ve her satırın sonuna <br> ekleyip aynı satırda birleştiren bir fonksiyon.
  Ayrıca " yerine ' koyar.

  Args:
    sözler: Şarkı sözleri metni.

  Returns:
    <br> eklenmiş, aynı satırda birleştirilmiş ve " yerine ' konmuş şarkı sözleri.
  """

  # " yerine ' koyma
  sözler = sözler.replace('"', "'")

  # Satırlara ayırma
  satırlar = sözler.splitlines()

  # Her satırın sonuna <br> ekleyip aynı satırda birleştirme
  eklenen_sözler = " ".join([satir + "<br>" for satir in satırlar])

  return eklenen_sözler


# Örnek kullanım:
sözler = """
Is this the real life? Is this just
fantasy? Caught in a landslide,
no escape from reality Open
your eyes, look up to the skies
and see I'm just a poor bo-oy, I
need no sympathy Because
I'm easy come, easy go, little
high, little low
Any way the wind blows doesn't
really matter to me, to me
Mama, just killed a man Put a
gun against his head, pulled
my trigger, now he's dead
Mama, life had just begun But
now I've gone and thrown it all
away Mama, ooh, (is this the
real life) didn't mean to make
you cry If I'm not back again
this time tomorrow Carry on,
carry on as if nothing really
matters
Too late, my time has come
Sends shivers down my spine,
body's aching all the time
Goodbye, everybody, I've got
to go Gotta leave you all
behind and face the truth
Mama, ooh (any way the wind
blows) I don't wanna die I
sometimes wish I'd never
been born at all -Gitar solosu-
I see a little silhouetto of a
man Scaramouche,
Scaramouche, will you do the
Fandango? Thunderbolt and
lightning, very, very
frightening me(burada normal
sesle devam ama heyya
grubu bi oktav inceden
söyleyecek) (Galileo) Galileo,
(Galileo) Galileo, Galileo
Figaro, magnifico-o--o-o -sus-
I'm just a poor boy, nobody
loves me He's just a poor boy
from a poor family Spare him
his life from this monstrosity
Easy come, easy go, will you let
me go? Bismillah No, we will not
let you go (let him go) Bismillah
We will not let you go
(let him go) Bismillah
We will not let you go (let me go)
Will not let you go (let me go)
Never, never, never, never let me
go
No, no, no, no, no, no, no
Oh, mamma mia, mamma mia
Mamma mia, let me go
Beelzebub has a devil put aside
for me, for me, for me(yine
heyya grubu bi oktav üstten
söylüyor)
So you think you can stone me
and spit in my eye? So you think
you can love me and leave me to
die? Oh, baby, can't do this to
me, baby Just gotta get out, just
gotta get right outta here
Ooh
Ooh, yeah, ooh, yeah
Nothing really matters,
anyone can see Nothing
really matters Nothing
really matters to me
"""

eklenen_sözler = eklenecek_br(sözler)
print(eklenen_sözler)