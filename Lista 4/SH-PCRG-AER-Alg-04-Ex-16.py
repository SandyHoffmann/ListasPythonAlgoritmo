from random import randint
soma = 0
for x in range(10):
    cara = 0
    coroa = 0
    total = 0
    result= ""

    while cara<3 and coroa<3:
        numeroaleatorio = randint(1,2)
        if numeroaleatorio == 1:
            result+=" A "
            cara += 1
            coroa = 0
        else:
            result+=" B "
            coroa+=1
            cara = 0
        total+=1
    print(f'{result} ({total} sorteios! )')
    soma+=total
print(f'Foram necessários na media {soma/10} sorteios.')