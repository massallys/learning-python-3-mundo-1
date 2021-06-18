#conversor de medidas

numMetros = float(input('Uma distância em metros: '))
numKM = numMetros / 1000
numHM = numMetros / 100
numDAM = numMetros / 10
numDM = numMetros * 10
numCM = numMetros * 100
numMM = numMetros * 1000

print('A medida de {} corresponde a:\n'
      '{:.3f} KM\n'
      '{:.2f} HM\n'
      '{:.1f} DAM\n'
      '{:.0f} DM\n'
      '{:.0f} CM\n'
      '{:.0f} MM\n'.format(
    numMetros, numKM, numHM, numDAM, numDM, numCM, numMM)
)
