| Student name             | Sayak Kundu    |
|-------------------------:|:--------------:|
| Student Roll No.         | 20161035       |
| Code Review of           | Bomberman      |
| lines of code reviewed   | 367            |
| Bugs identified          | 0              |  

* Extra Features that can be added:
  * Powerups
  * Different types of enemies(Enemies with different speeds, Enemies with different amount of lives, etc.)
  * Different types of bricks

```bash
************* Module Config
W:  5, 4: Global variable 'BOMBS' undefined at the module level (global-variable-undefined)
W:  5, 4: Global variable 'ENEMYPUT' undefined at the module level (global-variable-undefined)
W:  6, 4: Global variable 'ENEMIES' undefined at the module level (global-variable-undefined)
W:  6, 4: Global variable 'SCORE' undefined at the module level (global-variable-undefined)
W:  6, 4: Global variable 'CONSWALL' undefined at the module level (global-variable-undefined)
W:  6, 4: Global variable 'CONSBRICK' undefined at the module level (global-variable-undefined)
W:  6, 4: Global variable 'LEFTBTIME' undefined at the module level (global-variable-undefined)
W:  7, 4: Global variable 'ARR' undefined at the module level (global-variable-undefined)
W:  7, 4: Global variable 'LEVEL' undefined at the module level (global-variable-undefined)
W:  7, 4: Global variable 'ENEMYSET' undefined at the module level (global-variable-undefined)
W:  9,40: Unused variable 'y' (unused-variable)
W:  9,20: Unused variable 'x' (unused-variable)
************* Module Getch
C:  9, 0: Old-style class defined. (old-style-class)
R: 16,12: Redefinition of self.impl type from Getch.GetchWindows to Getch.GetchUnix (redefined-variable-type)
C: 28, 0: Old-style class defined. (old-style-class)
W: 42,23: Unused variable 'e_val' (unused-variable)
W: 42,16: Unused variable 'o_val' (unused-variable)
C: 59, 0: Old-style class defined. (old-style-class)
E: 63, 8: Unable to import 'msvcrt' (import-error)
W: 63, 8: Unused variable 'msvcrt' (unused-variable)
E: 66, 8: Unable to import 'msvcrt' (import-error)
************* Module Main
E: 36, 0: invalid syntax (syntax-error)
************* Module Walls
R:  1, 0: Similar lines in 2 files
==Bomb:14
==Bomberman:17
        [x_val, y_val] = self.getposition()
        i = 0
        while i < 4:
            Config.ARR[x_val][i + y_val] = self.shape[0][i]
            Config.ARR[x_val + 1][i + y_val] = self.shape[1][i]
            i = i + 1
 (duplicate-code)
```

Report
======
```bash
363 statements analysed.
```

Statistics by type
------------------
```bash
+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |9      |9          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |10     |10         |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|method   |47     |35         |+12.00     |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|function |1      |1          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
```


External dependencies
---------------------
```bash
::

    Bricks (Board)
    Config (Getch,Enemy,Bomb,Bricks,Bomberman,Person,Walls)
    Person
      \-Person (Enemy,Bomberman)

```

Raw metrics
-----------
```bash
+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |395    |73.97 |404      |-9.00      |
+----------+-------+------+---------+-----------+
|docstring |61     |11.42 |8        |+53.00     |
+----------+-------+------+---------+-----------+
|comment   |2      |0.37  |2        |=          |
+----------+-------+------+---------+-----------+
|empty     |76     |14.23 |69       |+7.00      |
+----------+-------+------+---------+-----------+
```


Duplication
-----------
```bash
+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |7     |30       |-23.00     |
+-------------------------+------+---------+-----------+
|percent duplicated lines |1.333 |6.329    |-5.00      |
+-------------------------+------+---------+-----------+
```


Messages by category
--------------------
```bash
+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |3      |148      |-145.00    |
+-----------+-------+---------+-----------+
|refactor   |2      |10       |-8.00      |
+-----------+-------+---------+-----------+
|warning    |15     |42       |-27.00     |
+-----------+-------+---------+-----------+
|error      |3      |3        |=          |
+-----------+-------+---------+-----------+
```


% errors / warnings by module
-----------------------------
```bash
+-------+------+--------+---------+-----------+
|module |error |warning |refactor |convention |
+=======+======+========+=========+===========+
|Getch  |66.67 |20.00   |50.00    |100.00     |
+-------+------+--------+---------+-----------+
|Main   |33.33 |0.00    |0.00     |0.00       |
+-------+------+--------+---------+-----------+
|Config |0.00  |80.00   |0.00     |0.00       |
+-------+------+--------+---------+-----------+
|Walls  |0.00  |0.00    |50.00    |0.00       |
+-------+------+--------+---------+-----------+
```


Messages
--------
```bash
+--------------------------+------------+
|message id                |occurrences |
+==========================+============+
|global-variable-undefined |10          |
+--------------------------+------------+
|unused-variable           |5           |
+--------------------------+------------+
|old-style-class           |3           |
+--------------------------+------------+
|import-error              |2           |
+--------------------------+------------+
|syntax-error              |1           |
+--------------------------+------------+
|redefined-variable-type   |1           |
+--------------------------+------------+
|duplicate-code            |1           |
+--------------------------+------------+
```


Global evaluation
-----------------
Your code has been rated at 9.04/10 (previous run: 4.14/10, +4.89)
