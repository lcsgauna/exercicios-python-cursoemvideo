# Melhore o desafio 061, perguntando para o usuário se ele 
# quer mostrar mais alguns termos. O programa encerra quando ele
# disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-='*10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
contador=1
total = 0
continuar_progressao = 10
while continuar_progressao != 0:
    total =total + continuar_progressao
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    continuar_progressao = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))