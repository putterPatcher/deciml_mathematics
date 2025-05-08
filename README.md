# deciml_maths

## pip install deciml_mathematics

### Note - *ret* argument is the *r* argument of *"retrn"* function in "terminate" library

**Use the *"setpr"* function to set the precision for a calculation (*"getpr"* to check the precision).**
```python
>>> from deciml_maths import setpr, getpr
>>> setpr(29)
>>> getpr()
29
```


## *Abbrevations*
- c: class
- o: object
- sm: staticmethod
- cm: classmethod
- f: function
- s: setter
- g: getter

<details>
<summary>Matrix</summary>
<p>
<details>
  <summary>matx</summary>
  <p>
    
**(o) matx**: Object that stores matrix properties

```python
>>> from deciml_maths.matrix import matx
>>> from deciml.deciml import setpr
>>> setpr(3)
>>> matrix = matx([[1.924,2.25452,3.35157],[2.2585441,3.35844,4.25841],[3.58425,4.365258,5.694222],[4.6945485,5.5875155,6.557885]],True,'w')
'''
    [[1.924,2.25452,3.35157],[2.2585441,3.35844,4.25841],[3.58425,4.365258,5.694222],[4.6945485,5.5875155,6.557885]] - 2-D matrix
    True: Check argument types
    'w': wait and exit
'''
>>> matrix.pmatx
matx(
|'1.924', '2.255', '3.352'|
|'2.259', '3.358', '4.258'|
|'3.584', '4.365', '5.694'|
|'4.695', '5.588', '6.558'|
)
```

i. **(s) matx**: Assign a new 2-D matrix

```python
>>> matrix.matx = [1.5, 2.8257, 3.25541]
>>> matx.pmatx
matx(
|'1.5', '2.826', '3.255'|
)

```

ii. **(g) matx**: Get the 2-D matrix as a tuple

```python
>>> mat = matrix.matx
>>> mat
((Decimal('1.5'), Decimal('2.826'), Decimal('3.255')),)
```

iii. **(g) rowlen**: Get the length of rows

```python
>>> matrix.rowlen
3
```

iv. **(g) collen**: Get the length of columns

```python
>>> matrix.collen
1
```

v. **(g) sqmatx**: Get if square matrix

```python
>>> matrix.sqmatx
False
```

vi. **(g) pmatx**: Print the matrix and return the matrix as a tuple

```python
>>> mat = matrix.pmatx
matx(
|'1.5', '2.826', '3.255'|
)

>>> mat
((Decimal('1.5'), Decimal('2.826'), Decimal('3.255')),)
```

v. **(f) dnant**: Get the determinant of matrix

```python
>>> matrix = matx([[1,2,3,5],[2,4,4,5],[3,4,8,6],[7,5,6,7]])
>>> matrix.dnant()

```

  </p>
</details>
<details>
  <summary>matutils</summary>
  <p>
  </p>
</details>
<details>
  <summary>melutils</summary>
  <p>
  </p>
</details>
<details>
  <summary>matstat</summary>
  <p>
  </p>
</details>
</p>
</details>

