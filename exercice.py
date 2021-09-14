#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage**2 / resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
  return v1[0] * v2[0] + v1[1] * v2[1] == 0

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
  total = i = 0
  for v in values:
    if (v >= 0):
      total += v
      i += 1
  return total / i
      

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
  hundies = twenties = tens = fives = ones = 0
  while value != 0:
    if value >= 100:
      hundies = value // 100
      value = value % 100
    elif value >= 20:
      twenties = value // 20
      value = value % 20
    elif value >= 10:
      tens = value // 10
      value = value % 10
    elif value >= 5:
      fives = value // 5
      value = value % 5
    elif value >= 1:
      ones = value
      value = 0

  return (hundies, twenties, tens, fives, ones)

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(3265))
