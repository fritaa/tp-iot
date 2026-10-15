in python variables are identifiers that act as pointers that bound to objects in memory
> in c writing `int x=10;` reserves a box in memory and puts 10 in it, when following it with `x=y` we create a brand new box and put 10 in it.
> in Python `x=10` creates an integer obj 10 in memory and makes the name *x* point to it. writing `x=y` makes *y* point to the **exact same obj** in memory

``` Python
x=[1,2,3]
y=x
print(f"memory address of x:{id(x)}")
print(f"memory address of y:{id(y)}")
print(f"do thet point to the same exact obj ?: {x is y}")
```

| class name | declare & assign | del | common op |
| :--------- | :--------------- | :-- | :-------- |
|bool|x=True<br>y=False|del x|and,or,not|
|int|x=0|del x||
|float|x=3.14|del x||
|list|x=[1,2,3]<br>x[0]=10(assign/update)|del x<br>del x[0]<br>x.pop()|x.==append(item)== *last*<br>x.==extend(item)==<br>x.==insert(index,item)==<br>x.==remove(item)== *first occurrence*<br>==len(list)==|
|tuple|x=(1,2,3)|del x|==len(tuple)==<br>x==[start:end]==<br>x.==count(item)==|
|str|x="hello"|del x|+ *(concat)*<br> len()<br>.upper()<br>.lower()<br>str.==split(sep,max sep)==|
|set|s={1,2,3}|del x<br>x.==remove(1)==|s.==add(item)== *last*<br>s.==update(iterable)==<br>s==.intersection({2,3,4})== $\rightarrow${2,3}<br>s.==union({2,3,4})== $\rightarrow$ {1,2,3,4}|
|dict|d={"a" :1}<br> d["b"]= 2 *(assign*|del x<br>del d["a"]<br>d.pop("a")|d.==key()== $\rightarrow$ ['a','b']<br>d.==values== $\rightarrow$ [1,2]<br>d.==items()== $\rightarrow$ [('a',1),('b',2)]<br>d.==get("a")== $\rightarrow$ 1|

| Catégorie / Structure | Opération / Méthode | Ce que ça fait | Exemple |
| :--- | :--- | :--- | :--- |
| **Général / Séquences** | `len(x)` | Renvoie le nombre total d'éléments ou de caractères | `len([10, 20])` $\rightarrow$ `2` |
| | `x[i]` | Accède à un élément par son index (négatif = fin) | `x[0]` $\rightarrow$ premier, `x[-1]` $\rightarrow$ dernier |
| | `x[start:end]` | Extrait une portion (`end` exclusif) | `x[1:]` $\rightarrow$ du 2e à la fin |
| | `x.count(item)` | Compte les occurrences d'une valeur | `[1, 2, 2].count(2)` $\rightarrow$ `2` |
| **Listes** | `append(item)` | Ajoute un élément à la fin | `x.append(3)` |
| | `extend(iterable)` | Ajoute plusieurs éléments d'une collection | `x.extend([3, 4])` |
| | `insert(idx, item)` | Insère un élément à un index précis | `x.insert(1, 2)` |
| | `remove(item)` | Supprime la première occurrence d'une valeur | `x.remove(2)` |
| | `pop(idx)` | Supprime et renvoie l'élément à l'index | `x.pop()` |
| | `sort()` | Trie la liste sur place | `x.sort()` |
| **Chaînes (`str`)** | `split(sep, max)"` | Découpe une chaîne en liste via séparateur | `"a,b".split(",")` $\rightarrow$ `['a', 'b']` |
| | `strip()` | Enlève les espaces inutiles aux extrémités | `" hello ".strip()` $\rightarrow$ `"hello"` |
| | `replace(o, n)` | Remplace du texte | `"cat".replace("c", "b")` $\rightarrow$ `"bat"` |
| **Sets** | `add(item)` | Ajoute un élément (sans doublon) | `s.add(3)` |
| | `update(iterable)` | Ajoute plusieurs éléments | `s.update([3, 4])` |
| | `intersection(oth)` | Éléments communs (`&`) | `{1, 2} & {2, 3}` $\rightarrow$ `{2}` |
| | `union(oth)` | Fusion unique (`\|`) | `{1, 2} \| {2, 3}` $\rightarrow$ `{1, 2, 3}` |
| | `discard(item)` | Supprime sans erreur si absent | `s.discard(2)` |
| **Dictionnaires** | `keys()` | Renvoie toutes les clés | `d.keys()` |
| | `values()` | Renvoie toutes les valeurs | `d.values()` |
| | `items()` | Renvoie les paires `(clé, valeur)` | `d.items()` |
| | `get(key, def)` | Récupère une valeur en évitant l'erreur | `d.get("z", 0)` $\rightarrow$ `0` |
| | `pop(key)` | Supprime une clé et renvoie sa valeur | `d.pop("a")` |

### exception handling flow
1. try:
	* *execute code operations
2. except:
	* *catch specific raised errors
3. else :
	* *run with zero errors occur
4. finalyy :
	* *always execute cleanup logic

```Python 
try :
	number= int(input("type a number"))
	result= number/10
	print(f"result is {result}")
except ZeroDivisionError :
	print("can't devide by zero")
except ValueError:
	print("enter a valid integer")
```
or we can catch multiple exceptions
```python
try:
	with open("non_existent_file.txt","r") as file:
		content = file.read()
except (FileNotFoundError, PermissionError) as err:
	print(f"file operation failed : {err}")
```
### file handeling
| Mode | Action | Behavior if file exists | Behavior if file missing |
| :--- | :--- | :--- | :--- |
| `"r"` | Read | Starts at beginning | FileNotFoundError |
| `"w"` | Write | Overwrites (clears content) | Creates new file |
| `"a"` | Append | Writes to the end | Creates new file |

### Basic Syntax
```python
# Reading
with open("note.txt", "r") as f:
    content = f.read()

# Writing
with open("note.txt", "w") as f:
    f.write("Hello Python")

# Appending
with open("note.txt", "a") as f:
    f.write("\nNew line")
```

|**Operation / Concept**|**Syntax / Code**|**Description**|
|---|---|---|
|**Opening a File**|`f = open("filename.txt", "mode")`|Opens a file and returns a file object. Always remember to close it (`f.close()`).|
|**Context Manager (Best Practice)**|`with open("file.txt", "r") as f:`<br><br>  <br><br>`content = f.read()`|Automatically closes the file when the `with` block exits, even if errors occur.|
|**Read Entire File**|`content = f.read()`|Reads the entire file content as a single string.|
|**Read Line by Line (List)**|`lines = f.readlines()`|Reads all lines into a list of strings (`['line1\n', 'line2\n']`).|
|**Read Single Line**|`line = f.readline()`|Reads a single line from the file (useful for looping or large files).|
|**Writing to a File**|`with open("file.txt", "w") as f:`<br><br>  <br><br>`f.write("Hello World\n")`|Opens in write mode (`"w"`). **Overwrites** the file if it exists, or creates it if it doesn't.|
|**Appending to a File**|`with open("file.txt", "a") as f:`<br><br>  <br><br>`f.write("New line\n")`|Opens in append mode (`"a"`). Adds text to the **end** of the file without deleting existing content.|

### raising and defining custom exceptions
we can intentionally raise exceptions using `raise` or create custom

```python
class InsufficientFundsError(Exception):
	"""raised when account balance is too low for withdrawal"""
	pass
def withdraw(balance, amount):
	if amount > balance:
		raise InsufficentFundsError(f"cannot withdraw ${amount}. current balance : ${balance}")
	return balance - amount
try:
	new_balance = withdraw(100,150)
except InsufficientFundsError as e:
	print(f"Transaction rejected :{e}")
```

