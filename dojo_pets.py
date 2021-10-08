from ninja import Ninja
from pets import Pet

Mo=Ninja('Mo', 'homie', 'gold fish', 'flakes', 'fish food')
King=Pet('king','dog','jumping',100, 100)

King.play().eat().sleep()
Mo.walk().feed().bathe()