import csv, math

set_sepal_length = []
set_sepal_width = []
set_petal_legnth = []
set_petal_width = []

vers_sepal_length = []
vers_sepal_width = []
vers_petal_legnth = []
vers_petal_width = []

verg_sepal_length = []
verg_sepal_width = []
verg_petal_legnth = []
verg_petal_width = []

with open('iris.csv.csv', 'r') as arquivo:
    dados = csv.reader(arquivo, delimiter=',')
    for linha in dados:
        if linha[4] == 'Setosa':
            set_sepal_length.append(float(linha[0]))
            set_sepal_width.append(float(linha[1]))
            set_petal_legnth.append(float(linha[2]))
            set_petal_width.append(float(linha[3]))
            
        elif linha[4] == 'Versicolor':
            vers_sepal_length.append(float(linha[0]))
            vers_sepal_width.append(float(linha[1]))
            vers_petal_legnth.append(float(linha[2]))
            vers_petal_width.append(float(linha[3]))

        elif linha[4] == 'Virginica':
            verg_sepal_length.append(float(linha[0]))
            verg_sepal_width.append(float(linha[1]))
            verg_petal_legnth.append(float(linha[2]))
            verg_petal_width.append(float(linha[3]))

print('Setosa:\n',
    'sepal.length: ', '{:.2f}'.format(sum(set_sepal_length)/len(set_sepal_length)), '\n',
    'sepal.width: ', '{:.2f}'.format(sum(set_sepal_width)/len(set_sepal_width)), '\n',
    'petal.length: ', '{:.2f}'.format(sum(set_petal_legnth)/len(set_petal_legnth)), '\n',
    'petal.width: ', '{:.2f}'.format(sum(set_petal_width)/len(set_petal_width)), '\n')

print('\nVersicolor:\n',
    'sepal.length: ', '{:.2f}'.format(sum(vers_sepal_length)/len(vers_sepal_length)), '\n',
    'sepal.width: ', '{:.2f}'.format(sum(vers_sepal_width)/len(vers_sepal_width)), '\n',
    'petal.length: ', '{:.2f}'.format(sum(vers_petal_legnth)/len(vers_petal_legnth)), '\n',
    'petal.width: ', '{:.2f}'.format(sum(vers_petal_legnth)/len(vers_petal_legnth)), '\n')

print('\nVirginica:\n',
    'sepal.length: ', '{:.2f}'.format(sum(verg_sepal_length)/len(verg_sepal_length)), '\n',
    'sepal.width: ', '{:.2f}'.format(sum(verg_sepal_width)/len(verg_sepal_width)), '\n',
    'petal.length: ', '{:.2f}'.format(sum(verg_petal_legnth)/len(verg_petal_legnth)), '\n',
    'petal.width: ', '{:.2f}'.format(sum(verg_petal_width)/len(verg_petal_width)), '\n')