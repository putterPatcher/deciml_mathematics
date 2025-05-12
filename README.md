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
#### Note - Can be used to check for errors :'/ *change the matx to pmatx*

```python
>>> matrix.pmatx
matx(
|'1.5', '2.826', '3.255'|
)

```

v. **(f) dnant**: Get the determinant of matrix

```python
>>> matrix = matx([[1,2,3,5],[2,4,4,5],[3,4,8,6],[7,5,6,7]])
>>> matrix.dnant()
Decimal('-155.000')
```

vi. **(f) invsednant**: Get the determinant of the inverse matrix

```python
>>> matrix.invsednant()
Decimal('-0.006452')
```
vii. **(f) invse**: Get the inverse matrix of the matrix

```python
>>> mat = matrix.invse()
>>> mat.pmatx
matx(
|'-0.051613', '-0.2194', '-0.045161', '0.2323'|
|'-0.4258', '0.6903', '-0.1226', '-0.083871'|
|'-0.096774', '-0.1613', '0.2903', '-0.064516'|
|'0.4387', '-0.1355', '-0.1161', '0.025806'|
)

```

vii. **(f) adjnt**: Get the adjoint matrix of the matrix

```python
>>> mat = matrix.adjnt()
>>> mat.pmatx
matx(
|'8.0', '34.0', '7.0', '-36.0'|
|'66.0', '-107.0', '19.0', '13.0'|
|'15.0', '25.0', '-45.0', '10.0'|
|'-68.0', '21.0', '18.0', '-4.0'|
)

```

viii. **(f) tpose**: Get the transpose matrix of the matrix

```python
>>> mat = matrix.tpose()
>>> mat.pmatx
matx(
|'1.0', '2.0', '3.0', '7.0'|
|'2.0', '4.0', '4.0', '5.0'|
|'3.0', '4.0', '8.0', '6.0'|
|'5.0', '5.0', '6.0', '7.0'|
)

```

ix. **(f) cofacm**: Get the matrix of cofactors for the matrix

```python
>>> mat = matrix.cofacm()
>>> mat.pmatx
matx(
|'8.0', '66.0', '15.0', '-68.0'|
|'34.0', '-107.0', '25.0', '21.0'|
|'7.0', '19.0', '-45.0', '18.0'|
|'-36.0', '13.0', '10.0', '-4.0'|
)

```

x. **(f) mele(i, j, chk, ret)**: Get an element of the matrix 

```python
>>> matrix.mele(0,0,True,'e')
'''
  0 - Row index
  0 - Column index
  True - Check arguments
  'e' - exit if error
'''
Decimal('1.0')
```

xi. **(f) mrow(i, chk, ret)**: Get a row of the matrix

```python
>>> matrix.mrow(0, True, 'c')
'''
  0 - Row index
  True - Check arguments
  'c' - continue if error
'''
(Decimal('1.0'), Decimal('2.0'), Decimal('3.0'), Decimal('5.0'))
```

xii. **(f) mcol(j, chk, ret)**: Get a column of the matrix

```python
>>> matrix.mcol(0, True, 'a')
'''
  0 - Column index
  True - Check arguments
  'a' - Ask to exit if error
'''
(Decimal('1.0'), Decimal('2.0'), Decimal('3.0'), Decimal('7.0'))
```

xiii. **(f) gele(a, r, chk, ret)**: Get the rows or columns of the matrix

```python
>>> matrix.gele([0,2], False, False, 'e')
'''
  [0,2] - Row or column indexes
  False - Get columns
  False - Skip arguments check
  'e' - exit if error
'''
((Decimal('1.0'), Decimal('2.0'), Decimal('3.0'), Decimal('7.0')), (Decimal('3.0'), Decimal('4.0'), Decimal('8.0'), Decimal('6.0')))
```

xiv. **(f) matxl()**: Get the matrix as a list of Decimal objects

```python
>>> matrix.matxl()
[[Decimal('1.0'), Decimal('2.0'), Decimal('3.0'), Decimal('5.0')], [Decimal('2.0'), Decimal('4.0'), Decimal('4.0'), Decimal('5.0')], [Decimal('3.0'), Decimal('4.0'), Decimal('8.0'), Decimal('6.0')], [Decimal('7.0'), Decimal('5.0'), Decimal('6.0'), Decimal('7.0')]]
```

xv. **(f) pop(i, r, chk, ret)**: Remove a row or column of the matrix

```python
>>> matrix.pop(0, False, True, 'c')
(Decimal('1.0'), Decimal('2.0'), Decimal('3.0'), Decimal('7.0'))
>>> matrix.pmatx
matx(
|'2.0', '3.0', '5.0'|
|'4.0', '4.0', '5.0'|
|'4.0', '8.0', '6.0'|
|'5.0', '6.0', '7.0'|
)

```

  </p>
</details>
<details>
  <summary>matutils</summary>
  <p>

**(c) matutils**: Methods used with matx

i. **(sm) sclrm(n, el, chk, ret)**: Get a matx object with a scalar matrix

ii. **(sm) eqelm(m, n, i, chk, ret)**: Get a matx object of matrix with equal elements

iii. **(sm) addmatx(a, *b, r, chk, ret)**: Get a matrix as a matx object for matrices of matx objects appended along row or column direction 

iv. **(cm) maddval(a, x, chk, ret)**: Add a number to all elements of the matrix for a matx object

v. **(sm) matlxtox(a, chk, ret)**: Convert matx object to a tuple of matx objects with column matrix

vi. **(sm) matxtolx(a, chk, ret)**: Convert a tuple of matx objects with column matrix to a matx object

vii. **(sm) gele(a, b, r, chk, ret)**: Get the rows or columns of the matrix for a matx object as a matx object

viii. **(cm) tpose(a, chk, ret)**: Get the transpose matrix as a matx object for matrix of a matx object

ix. **(cm) cofac(a, b, c, chk, ret)**: Get the matrix of cofactors as a matx object for matrix of a matx object

x. **(cm) dnant(a, chk, ret)**: Get the determinant of matrix for a matx object

xi. **(cm) adjnt(a, chk, ret)**: Get the adjoint of matrix for a matx object

xii. **(cm) invse(a, chk, ret)**: Get the inverse matrix as a matx object for matrix of a matx object

xiii. **(cm) invsednant(a, chk, ret)**: Get the determinant of the inverse matrix for matrix of a matx object

xiv. **(cm) tform(a, b, c, d, r, chk, ret)**: Get a matx object with matrix for matrix of a matx object after a row or column transformation

xv. **(sm) madd(a, b, sumr, chk, ret)**: Get the matrix as a matx object after matrix addition for matrices of two matx objects

xvi. **(cm) saddcnst(a, b, r, sumr, chk, ret)**: Get the matrix as matx object after addition of a constant to each row or column in matrix of a matx object

xvii. **(sm) msub(a, b, sumr, chk, ret)**: Get the matrix as a matx object after matrix subtraction for matrices of two matx objects

xviii. **(sm) smult(a, b, sumr, chk, ret)**: Get the matrix as matx object after multiplication of a number 

xix. **(cm) smultfac(a, b, r, sumr, chk, ret)**: Get the matrix as a matx object after multiplication of a number to each row or column in matrix of a matx object

xx. **(cm) mmult(a, b, t, sumr, chk, ret)**: Get the matrix as a matx object after matrix multiplication for matrices of two matx objects

xxi. **(sm) melmult(a, b, t, sumr, chk, ret)**: 

xxii. **(sm) uldcompose(a, chk, ret)**: 

xxiii. **(cm) dpose(a, li, r, chk, ret)**:

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

