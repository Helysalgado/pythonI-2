## INTRODUCTION
This program is intended to be a "rock, peper, scissors"
In it you can play by choosing an option, then an npc randomly choose another option.
And acording to the rules you win, lose or you're tie.
After the result of the game it asks the user if wanna play again.

## RULES

The game "rock paper scissors" is a game in wich two oponents choose between the three options and the winner works according to a round hierarqui.

In the next representation '>' means 'wins to'
... Rock > Scissors > Paper > Rock ...
closing the loop, and is a tie if both choose the same.

## METODOLOGY
Here is explained the most importants parts of the code.

- First the ramdom library is imported to make the npc choice randomly
- The game show the instructions to play the game.
- Then the program set a falg to repeat the process in case it is asked for
```python
restart = 'y'
while restart == 'y':
	# Code
	print('¿Quieres volver a jugar?  y=si  n=no')
	restart = input()
```
- In that loop the user is asked to choose a number to indicate its option
- To ensure the user gives a valid option it is a loop that will only allow valid options (from 0 to 2)
```python
error = True
while error == True:
	print(f'ELIGE... ')
	choice = (int(input())) # The user choose
	if 0<=choice<=2: error = False
	else: print('no escogite un opcion valida, de nuevo...')
```
- npc randomly choose
```python
npc = random.choice([0,1,2])
```
- The selections are shoen to the user
- The resluts of the game are calculated in the next form
	The game process the options as numbers that represents a position in the list `moves` and for the rules of the game the winner is the one who choose the bigger number by one or smaller by two in the list
```python
moves = ['piedra', 'papel', 'tijeras']

if npc == choice+1 or npc == choice-2: print('Perdiste!')
if npc == choice-1 or npc == choice+2: print('Ganaste!')
if npc == choice: print('Empataron!')
```
- Finally the user choose to play again or not



## INSTALLATION




## EXAMPLES

The programs runs in command line interface (CLI).

**1. User give "0" for rock option
**

```
VAMOS A JUGAR PIEDRA PAPEL O TIJERAS!
Para mas inforacion de las reglas del juego se sugiere leer el archivo `README.md` en la documentación del programa
En este juego indicas tu movimiento con números de la siguiente manera

	piedra = 0	papel = 1	tijeras = 2

ELIGE... 
0

Elegiste piedra y el npc eligio piedra
Empataron!

```



