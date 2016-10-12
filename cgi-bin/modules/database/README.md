Database module
=========

De database module wordt hieronder uitgelegd aan de hand van voorbeelden. Om de queries uit te voeren op de database maakt deze modulen gebruik van de SQLite3 module in Python.

Voorbeelden
---------
De voorbeelden zullen gebaseerd worden op de volgende tabel:

#### Personen tabel

| id  |  naam   | achternaam  |   adres   |
|-----|---------|-------------|-----------|
| 1   |  Piet   | Jansen      | Straat 1  |
| 2   |  Bert   | Pieters     | Straat 2  |
| 3   |  Peter  | Geertsen    | Straat 3  |


#### Module importeren

```python
# Hoofd module van de database module
from modules.database import database as db
# Deze import is optioneel,
# In de queries file zijn constanten opgenomen met queries
from modules.database.queries import *
```

#### Fetch de hele tabel

```python
# Fetch de gehele tabel
db.query("SELECT * FROM personen")
```

#### Fetch een hele rij

```python
# Fetch an entire row
db.row("SELECT * FROM personen WHERE id = ?", (2,))
```

**Resultaat**

| id  |  naam   | achternaam  |   adres   |
|-----|---------|-------------|-----------|
| 2   |  Bert   | Pieters     | Straat 2  |

#### Fech één column

```python
# Fetch een enkele column
db.single("SELECT naam FROM personen WHERE achternaam = ? AND adres = ?", ("Jansen", "Straat 1"))
```

**Resultaat**

|  naam   |
|---------|
|  Piet   |

#### Updaten, Deleten of toevoegen

```python
# Updaten
db.query("UPDATE personen SET naam = ? WHERE id = ?", ("Gerrit", 1))

# Deleten
db.query("DELETE FROM personen WHERE id = ?", (3,))

# Toevoegen
db.query("INSERT INTO personen VALUES (?, ?, ?, ?)", (4, "Jan", "Martens", "Straat 4"))
```

**Resultaat**

In alle gevallen hierboven zal het Resultaat **1** zijn. Bij het updaten, toevoegen of deleten wordt namelijk het aantal aangepaste rijen geretourneerd.

#### Queries uit de queries file
De queries die in de queries file staan zijn allemaal gedefineerd al een constante. Deze kunnen op de volgende manier gebruikt worden.

*queries.py*
```python
# Selecteert alle personen uit de personen tabel
SQL_ALL_PERSONS = "SELECT * FROM personen"
```

*Project file*
```python
# Fetch alle resultaten
db.query(SQL_ALL_PERSONS)
```

**Resultaat**

| id  |  naam   | achternaam  |   adres   |
|-----|---------|-------------|-----------|
| 1   |  Gerrit | Jansen      | Straat 1  |
| 2   |  Bert   | Pieters     | Straat 2  |
| 4   |  Jan    | Martens     | Straat 4  |
