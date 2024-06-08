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
Oh when the saints
go marching in
Now when the saints go marching in
Yes I want to be in that number
Oh when the saints go marching in
Oh when the saints
go marching in
Now when the saints go marching in
Yes I want to be in that number
Oh when the saints go marching in
Oh when the saints (oh when the saints)
Go marching in (go marching in)
Now when the saints go marching in (saints go marching in)
Yes I want to be in that number
Oh when the saints go marching in (saints go marching in)
Oh when the saints (oh when the saints)
Go marching in (go marching in)
Now when the saints go marching in (saints go marching in)
Yes, I want to be in that number
Oh when the saints go marching in (saints go marching in)
Oh when the saints Oh when the saints
Go marching in Go marching in 
Now when the saints go marching in 
A-N-A-D-O-L-U
A-N-A-D-O-L-U
A-N-A-D-O-L-U
A-N-A-D-O-L-U
"""

eklenen_sözler = eklenecek_br(sözler)
print(eklenen_sözler)