# 🗼 Tower of Hanoi Solver

Un risolutore algoritmico in **Python** per il classico rompicapo matematico della **Torre di Hanoi**, implementato tramite ricorsione.

Questo script non solo risolve il problema per un numero arbitrario di dischi, ma **fotografa e stampa lo stato reale dei tre pali ad ogni singola mossa**, rendendo facilissimo visualizzare lo scorrere dell'algoritmo.

## 📋 Indice
- [Descrizione del Problema](#-descrizione-del-problema)
- [Logica dell'Algoritmo](#-logica-dellalgoritmo)
- [Codice Sorgente](#-codice-sorgente)
- [Esempio di Output](#-esempio-di-output)

---

## 🧩 Descrizione del Problema
La Torre di Hanoi è un puzzle composto da tre pali e $N$ dischi di dimensioni decrescenti. L'obiettivo è spostare l'intera torre dal primo all'ultimo palo rispettando tre rigide regole:
1. Si può spostare **solo un disco alla volta**.
2. Si può prendere solo il disco che si trova in cima a un palo.
3. **Nessun disco può mai essere appoggiato sopra un disco più piccolo**.

---

## 🧠 Logica dell'Algoritmo
Il codice applica il principio ricorsivo del *Divide et Impera* (la metafora del "Capo Pigro"): per spostare $N$ dischi dalla Sorgente alla Destinazione usando un Appoggio:

1. **Subappalto 1:** Sposta i primi $N-1$ dischi dalla *Sorgente* all'*Appoggio*.
2. **Mossa del Capo:** Sposta l'unico disco gigante rimasto dalla *Sorgente* alla *Destinazione*.
3. **Subappalto 2:** Sposta i dischi $N-1$ parcheggiati sull'*Appoggio* sopra al disco gigante sulla *Destinazione*.

---

## 💻 Codice Sorgente

```python
def hanoi_solver(disks: int):
    # I 3 pali fisici fissi
    first_road = list(range(1, disks + 1))[::-1]
    second_road = []
    third_road = []
    moves = []
    
    # Core ricorsivo (i ruoli dei pali cambiano ad ogni livello)
    def hanoi(disks, source, destination, pivot):
        if disks == 1:
            destination.append(source.pop())
            moves.append(f"{first_road} {second_road} {third_road}")
            return

        hanoi(disks - 1, source, pivot, destination)
        
        destination.append(source.pop())
        moves.append(f"{first_road} {second_road} {third_road}")
        
        hanoi(disks - 1, pivot, destination, source)

    # Scatta la foto iniziale e avvia la ricorsione
    moves.append(f"{first_road} {second_road} {third_road}")
    hanoi(disks, first_road, third_road, second_road)
    
    return "\n".join(moves)

if __name__ == "__main__":
    print(hanoi_solver(3))
```

---

## 📊 Esempio di Output (3 dischi)

I numeri all'interno delle liste rappresentano la grandezza del disco (`3` è il più grande alla base, `1` è il più piccolo in cima):

```text
[3, 2, 1] [] []         <-- Stato Iniziale (Tutto sul Palo 1)
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]           <-- Il disco gigante 3 arriva a destinazione
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]         <-- Stato Finale (Risolto!)
```
