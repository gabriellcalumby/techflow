# CÓDIGO LEGADO — EXERCÍCIO DE REFATORAÇÃO
# Este exemplo foi criado propositalmente com nomes ruins e formatação inadequada.

def c(a,b):
 x=0
 if a=="alta":
  x=3
 elif a=="media":
  x=2
 else:
  x=1
 if b<=1:
  x=x+2
 elif b<=3:
  x=x+1
 return x

p=input("Prioridade (alta/media/baixa): ")
d=int(input("Prazo em dias: "))
print("Pontuacao:",c(p,d))
