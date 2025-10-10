# deciml_maths

## pip install deciml_mathematics


### Note - *'ret'* argument is the *'r'* argument of *"retrn"* function in "terminate" library.

### Note - If *'chk'* argument is False,
- **Incorrect argument types (Below declaration snippets in README) result in error.**
- **Using List instead of Tuple can result in error.**

### If *'chk'* is True,
- **Decimal type can be replaced with float, int, or string.**

### Note - Detailed description of arguments is available in the *docstring*.

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
    
**(o) matx(li, chk=True, ret='a')**: Object that stores matrix properties

- ***li*** - *tuple[ tuple[Decimal, ...] ] | tuple[Decimal, ...]*

```python
>>> from deciml_maths.matrix import matx
Imported deciml...
>>> from deciml.deciml import setpr
>>> setpr(3)
>>> matrix = matx([[1.924,2.25452,3.35157],[2.2585441,3.35844,4.25841],[3.58425,4.365258,5.694222],[4.6945485,5.5875155,6.557885]],True,'w')
'''
    [[1.924,2.25452,3.35157],[2.2585441,3.35844,4.25841],[3.58425,4.365258,5.694222],[4.6945485,5.5875155,6.557885]] - 2-D matrix
    True: Check argument types
    'w': Wait and exit if error
'''
>>> print(matrix)
matx(
_____|___[0]___|___[1]___|___[2]___|
 (0) | '1.924' | '2.255' | '3.352' | 
 (1) | '2.259' | '3.358' | '4.258' | 
 (2) | '3.584' | '4.365' | '5.694' | 
 (3) | '4.695' | '5.588' | '6.558' | 
)
```

i. **(s) matx**: Assign a new 2-D matrix

```python
>>> matrix.matx = [1.5, 2.8257, 3.25541]
>>> matrix.pmatx
matx(
_____|__[0]__|___[1]___|___[2]___|
 (0) | '1.5' | '2.826' | '3.255' | 
)

```

ii. **(g) matx -> tuple**: Get the 2-D matrix as a tuple

```python
>>> mat = matrix.matx
>>> mat
((Decimal('1.5'), Decimal('2.826'), Decimal('3.255')),)
```

iii. **(g) rowlen -> int**: Get the length of rows

```python
>>> matrix.rowlen
3
```

iv. **(g) collen -> int**: Get the length of columns

```python
>>> matrix.collen
1
```

v. **(g) sqmatx -> bool**: Get if square matrix

```python
>>> matrix.sqmatx
False
```

vi. **(g) pmatx**: Print the matrix and return the matrix as a tuple
#### Note - Can be used to check for errors. :'/ *Change the matx to pmatx*

```python
matrix.pmatx
matx(
_____|__[0]__|___[1]___|___[2]___|
 (0) | '1.5' | '2.826' | '3.255' | 
)

```

v. **(f) dnant() -> Decimal**: Get the determinant of matrix

```python
>>> matrix = matx([[1,2,3,5],[2,4,4,5],[3,4,8,6],[7,5,6,7]])
>>> matrix.dnant()
Decimal('-155.000')
```

vi. **(f) invsednant() -> Decimal**: Get the determinant of the inverse matrix

```python
>>> matrix.invsednant()
Decimal('-0.006452')
```
vii. **(f) invse() -> matx**: Get the inverse matrix of the matrix

```python
>>> mat = matrix.invse()
>>> print(mat)
matx(
_____|____[0]_____|___[1]____|____[2]_____|____[3]_____|
 (0) | '-0.05161' | '-0.219' | '-0.04516' |    '0.232' | 
 (1) |   '-0.426' |  '0.690' |   '-0.123' | '-0.08387' | 
 (2) | '-0.09677' | '-0.161' |    '0.290' | '-0.06452' | 
 (3) |    '0.439' | '-0.135' |   '-0.116' |  '0.02581' | 
)

```

vii. **(f) adjnt() -> matx**: Get the adjoint matrix of the matrix

```python
>>> mat = matrix.adjnt()
>>> print(mat)
matx(
_____|___[0]___|___[1]____|___[2]___|___[3]___|
 (0) |   '8.0' |   '34.0' |   '7.0' | '-36.0' | 
 (1) |  '66.0' | '-107.0' |  '19.0' |  '13.0' | 
 (2) |  '15.0' |   '25.0' | '-45.0' |  '10.0' | 
 (3) | '-68.0' |   '21.0' |  '18.0' |  '-4.0' | 
)

```

viii. **(f) tpose() -> matx**: Get the transpose matrix of the matrix

```python
>>> mat = matrix.tpose()
>>> print(mat)
matx(
_____|__[0]__|__[1]__|__[2]__|__[3]__|
 (0) | '1.0' | '2.0' | '3.0' | '7.0' | 
 (1) | '2.0' | '4.0' | '4.0' | '5.0' | 
 (2) | '3.0' | '4.0' | '8.0' | '6.0' | 
 (3) | '5.0' | '5.0' | '6.0' | '7.0' | 
)

```

ix. **(f) cofacm() -> matx**: Get the matrix of cofactors for the matrix

```python
>>> mat = matrix.cofacm()
>>> print(mat)
matx(
_____|___[0]___|___[1]____|___[2]___|___[3]___|
 (0) |   '8.0' |   '66.0' |  '15.0' | '-68.0' | 
 (1) |  '34.0' | '-107.0' |  '25.0' |  '21.0' | 
 (2) |   '7.0' |   '19.0' | '-45.0' |  '18.0' | 
 (3) | '-36.0' |   '13.0' |  '10.0' |  '-4.0' | 
)

```

x. **(f) mele(i, j, chk=True, ret='a') -> Decimal**: Get an element of the matrix 

- **i** - *int*
- **j** - *int*

```python
>>> ele = matrix.mele(0,0,True,'e')
'''
  0 - Row index
  0 - Column index
  True - Check arguments
  'e' - Exit if error
'''
>>> ele
Decimal('1.0')
```

xi. **(f) mrow(i, chk=True, ret='a') -> tuple[Decimal, ...]**: Get a row of the matrix

- **i** - *int*

```python
>>> row = matrix.mrow(0, True, 'c')
'''
  0 - Row index
  True - Check arguments
  'c' - Continue if error
'''
>>> row
(Decimal('1.0'), Decimal('2.0'), Decimal('3.0'), Decimal('5.0'))
```

xii. **(f) mcol(j, chk=True, ret='a') -> tuple[Decimal, ...]**: Get a column of the matrix

- **j** - *int*

```python
>>> col = matrix.mcol(0, True, 'a')
'''
  0 - Column index
  True - Check arguments
  'a' - Ask to exit if error
'''
>>> col
(Decimal('1.0'), Decimal('2.0'), Decimal('3.0'), Decimal('7.0'))
```

xiii. **(f) gele(a, r=False, chk=True, ret='a') -> tuple[ tuple[Decimal, ...] ]**: Get the rows or columns of the matrix

- **a** - *list[ int ]*
- **r** - *bool*

```python
>>> cols = matrix.gele([0,2], False, False, 'e')
'''
  [0,2] - Column indexes
  False - Get columns
  False - Skip arguments check
  'e' - Exit if error
'''
>>> cols
((Decimal('1.0'), Decimal('2.0'), Decimal('3.0'), Decimal('7.0')), (Decimal('3.0'), Decimal('4.0'), Decimal('8.0'), Decimal('6.0')))
```

xiv. **(f) matxl() -> list[ list[ Decimal ] ]**: Get the matrix as a list of Decimal objects

```python
>>> matrix.matxl()
[[Decimal('1.0'), Decimal('2.0'), Decimal('3.0'), Decimal('5.0')], [Decimal('2.0'), Decimal('4.0'), Decimal('4.0'), Decimal('5.0')], [Decimal('3.0'), Decimal('4.0'), Decimal('8.0'), Decimal('6.0')], [Decimal('7.0'), Decimal('5.0'), Decimal('6.0'), Decimal('7.0')]]
```

xv. **(f) pop(i, r=True, chk=True, ret='a') -> tuple[Decimal, ...]**: Remove a row or column of the matrix

- **i** - *int*
- **r** - *bool*

```python
>>> matrix.pop(0, False, True, 'c')
>>> popped = matrix.pop(0, False, True, 'c')
'''
	0 - Column index
	False - Pop column
	True - Check arguments
	'c' - Continue if error
'''
>>> popped
(Decimal('1.0'), Decimal('2.0'), Decimal('3.0'), Decimal('7.0'))
>>> print(matrix)
matx(
_____|__[0]__|__[1]__|__[2]__|
 (0) | '2.0' | '3.0' | '5.0' | 
 (1) | '4.0' | '4.0' | '5.0' | 
 (2) | '4.0' | '8.0' | '6.0' | 
 (3) | '5.0' | '6.0' | '7.0' | 
)

```

  </p>
</details>
<details>
  <summary>matutils</summary>
  <p>

**(c) matutils**: Methods used with matx

```python
>>> from deciml_maths.matrix import matx, matutils
Imported deciml...
```

i. **(sm) sclrm(n, el, chk=True, ret='a') -> matx**: Get a matx object with a scalar matrix

- **n** - *int*
- **el** - *Decimal*

```python
>>> from deciml_maths import setpr                
>>> setpr(3)
>>> mat = matutils.sclrm(4, 12.12345, True, 'e')
'''
	4 - Nummber of rows of square matrix
	12.12345 - Diagonal values
	True - Check arguments
	'e' - Exit if error
'''
>>> print(mat)
matx(
_____|___[0]____|___[1]____|___[2]____|___[3]____|
 (0) | '12.123' |    '0.0' |    '0.0' |    '0.0' |
 (1) |    '0.0' | '12.123' |    '0.0' |    '0.0' |
 (2) |    '0.0' |    '0.0' | '12.123' |    '0.0' |
 (3) |    '0.0' |    '0.0' |    '0.0' | '12.123' |
)

```

ii. **(sm) eqelm(m, n, i, chk=True, ret='a') -> matx**: Get a matx object of matrix with equal elements

- **m** - *int*
- **n** - *int*
- **i** - *Decimal*

```python
>>> mat = matutils.eqelm(4, 3, 12.12345, True, 'e')
'''
	4 - Number of rows
	3 - Number of columns
	12.12345 - Element value
	True - Check arguments
	'e' - Exit if error
'''
>>> print(mat)
matx(
_____|___[0]____|___[1]____|___[2]____|
 (0) | '12.123' | '12.123' | '12.123' |
 (1) | '12.123' | '12.123' | '12.123' |
 (2) | '12.123' | '12.123' | '12.123' |
 (3) | '12.123' | '12.123' | '12.123' |
)

```

iii. **(sm) addmatx(a, *b, r=False, chk=True, ret='a') -> matx**: Get a matrix as a matx object for matrices of matx objects appended along row or column direction 

- **a** - *matx*
- **\*b** - *matx*
- **r** - *bool*

```python
>>> mat1 = matx([[1,2,3,4],[12.1234, 1.2365, 3, 4]])
>>> mat2 = matx([[0.2365, 1.23641, 4.25631, 5],[5,6,7,8]])
>>> mat3 = matx([[1,2,3,4],[2,3,4,5]])
>>> mat = matutils.addmatx(mat1, mat2, mat3, r=True, chk=True, ret='w')
'''
	mat1, mat2, mat3 - matx objects
	True - Along row
	True - Check arguments
	'w' - Wait and exit if error
'''
>>> print(mat)
matx(
_____|___[0]____|___[1]___|___[2]___|__[3]__|
 (0) |    '1.0' |   '2.0' |   '3.0' | '4.0' |
 (1) | '12.123' | '1.237' |   '3.0' | '4.0' |
 (2) |  '0.237' | '1.236' | '4.256' | '5.0' |
 (3) |    '5.0' |   '6.0' |   '7.0' | '8.0' |
 (4) |    '1.0' |   '2.0' |   '3.0' | '4.0' |
 (5) |    '2.0' |   '3.0' |   '4.0' | '5.0' |
)

>>> mat = matutils.addmatx(mat1, mat2, mat3, r=False, chk=True, ret='w')
'''
	mat1, mat2, mat3 - matx objects
	False - Along columns
	True - Check arguments
	'w' - Wait and exit if error
'''
>>> print(mat)
matx(
_____|___[0]____|___[1]___|__[2]__|__[3]__|___[4]___|___[5]___|___[6]___|__[7]__|__[8]__|__[9]__|_[10]__|_[11]__|
 (0) |    '1.0' |   '2.0' | '3.0' | '4.0' | '0.237' | '1.236' | '4.256' | '5.0' | '1.0' | '2.0' | '3.0' | '4.0' |
 (1) | '12.123' | '1.237' | '3.0' | '4.0' |   '5.0' |   '6.0' |   '7.0' | '8.0' | '2.0' | '3.0' | '4.0' | '5.0' |
)

```

iv. **(cm) maddval(a, x, chk=True, ret='a') -> matx**: Get a matrix as a matx object with a number added to all the rows in the matrix of a matx object at the first index

- **a** - *matx*
- **x** - *Decimal*

```python
>>> mat = matutils.maddval(mat1, 10.1234, True, 'a')
'''
	mat1 - matx object
	10.1234 - Number
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat)
matx(
_____|___[0]____|___[1]____|___[2]___|__[3]__|__[4]__|
 (0) | '10.123' |    '1.0' |   '2.0' | '3.0' | '4.0' |
 (1) | '10.123' | '12.123' | '1.237' | '3.0' | '4.0' |
)

```

v. **(sm) matlxtox(a, chk=True, ret='a') -> tuple[matx, ...]**: Convert matx object to a tuple of matx objects with row matrix

- **a** - *matx*

```python
>>> a = matutils.matlxtox(mat1, True, 'a')
'''
	mat1 - matx objects
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> for i in a:
...     print(i)
... 
matx(
_____|__[0]__|__[1]__|__[2]__|__[3]__|
 (0) | '1.0' | '2.0' | '3.0' | '4.0' |
)

matx(
_____|___[0]____|___[1]___|__[2]__|__[3]__|
 (0) | '12.123' | '1.237' | '3.0' | '4.0' |
)

```

vi. **(sm) matxtolx(a, chk=True, ret='a') -> matx**: Convert a tuple of matx objects with row matrix to a matx object

- **a** - *matx*

```python
>>> mat = matutils.matxtolx(a, True, 'a')
'''
	a - Tuple of matx objects with row matrix
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat)
matx(
_____|___[0]____|___[1]___|__[2]__|__[3]__|
 (0) |    '1.0' |   '2.0' | '3.0' | '4.0' |
 (1) | '12.123' | '1.237' | '3.0' | '4.0' |
)

```

vii. **(sm) gele(a, b, r=False, chk=True, ret='a') -> matx**: Get the rows or columns of the matrix for a matx object as a matx object

- **a** - *matx*
- **b** - *list[ int ]*
- **r** - *bool*

```python
>>> cols = matutils.gele(mat, [0,3], False, True, 'a')
'''
	mat - matx objects
	[0,3] - column indexes
	False - Get columns
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(cols)
matx(
_____|__[0]__|___[1]____|
 (0) | '1.0' | '12.123' |
 (1) | '4.0' |    '4.0' |
)

>>> rows = matutils.gele(mat, [0], True, True, 'a')
'''
	mat - matx object
	[0] - Row indexes
	True - Get rows
	True - Check arguments
	'a' - Ask to exit if error
'''   
>>> print(rows)
matx(
_____|__[0]__|__[1]__|__[2]__|__[3]__|
 (0) | '1.0' | '2.0' | '3.0' | '4.0' |
)

```

viii. **(cm) tpose(a, chk=True, ret='a') -> matx**: Get the transpose matrix as a matx object for matrix of a matx object



```python
>>> tmat = matutils.tpose(mat, True, 'a')
'''
	mat - matx object
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(tmat)
matx(
_____|__[0]__|___[1]____|
 (0) | '1.0' | '12.123' |
 (1) | '2.0' |  '1.237' |
 (2) | '3.0' |    '3.0' |
 (3) | '4.0' |    '4.0' |
)

```

ix. **(cm) cofac(a, b, c, chk=True, ret='a') -> matx**: Get the matrix of cofactors as a matx object for matrix of a matx object

- **a** - *matx*
- **b** - *int*
- **c** - *int*

```python
>>> cofac = matutils.cofac(mat, 0, 0, True, 'a')
Invalid command: matutils.cofac()
Error: Not a square matrix 
 
exit? y/n
n
>>> mat = matx([[1,2,3],[2,4,4],[1,3,5]])
>>> cofac = matutils.cofac(mat, 0, 0, True, 'a')
'''
	mat - matx object
	0 - Row index
	0 - Column index
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> cofac
Decimal('8.0')
```

x. **(cm) dnant(a, chk=True, ret='a') -> Decimal**: Get the determinant of matrix for a matx object

- **a** - *matx*

```python
>>> det = matutils.dnant(mat, True, 'a')
'''
	mat - matx object
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> det
Decimal('2.0')
```

xi. **(cm) adjnt(a, chk=True, ret='a') -> matx**: Get the adjoint of matrix for a matx object

- **a** - *matx*

```python
>>> adjmat = matutils.adjnt(mat, True, 'a')
'''
	mat - matx object
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(adjmat)
matx(
_____|__[0]___|__[1]___|__[2]___|
 (0) |  '8.0' | '-1.0' | '-4.0' |
 (1) | '-6.0' |  '2.0' |  '2.0' |
 (2) |  '2.0' | '-1.0' |  '0.0' |
)

```

xii. **(cm) invse(a, chk=True, ret='a') -> matx**: Get the inverse matrix as a matx object for matrix of a matx object

- **a** - *matx*

```python
>>> invmat = matutils.invse(mat, True, 'a')
'''
	mat - matx object
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(invmat)
matx(
_____|__[0]___|___[1]___|__[2]___|
 (0) |  '4.0' | '-0.50' | '-2.0' |
 (1) | '-3.0' |   '1.0' |  '1.0' |
 (2) |  '1.0' | '-0.50' |  '0.0' |
)

```

xiii. **(cm) invsednant(a, chk=True, ret='a') -> Decimal**: Get the determinant of the inverse matrix for matrix of a matx object

- **a** - *matx*

```python
>>> mat = matx([[1,2,3],[2.256245,4,4],[1,3.2358,5.332526]])
>>> mat.invse().dnant()                                     
Decimal('0.449')
>>> invdet = matutils.invsednant(mat, True, 'a')
'''
	mat - matx object
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> invdet
Decimal('0.449')
```

xiv. **(cm) tform(a, b, c, d, r=False, chk=True, ret='a') -> matx**: Get a matx object with matrix for matrix of a matx object after a row or column transformation

- **a** - *matx*
- **b** - *int*
- **c** - *int*
- **d** - *Decimal*

***Note - Transformation is [b] -> [b] + c\*[d]***

```python
>>> mat = matx([[1,2,3],[2,4,4],[1,3,5]])
>>> mat = matutils.tform(mat, 1, 2, 1.2487, False, True, 'a')
'''
	mat - matx object
	1 - Index
	2 - Index
	1.2487 - Factor
	False - Column transformation
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat)
matx(
_____|__[0]__|___[1]___|__[2]__|
 (0) | '1.0' | '5.747' | '3.0' |
 (1) | '2.0' | '8.996' | '4.0' |
 (2) | '1.0' | '9.245' | '5.0' |
)

```

xv. **(sm) madd(a, b, sumr=None, chk=True, ret='a') -> matx | tuple[Decimal, ...]**: Get the matrix as a matx object after matrix addition for matrices of two matx objects

- **a** - *matx*
- **b** - *matx*
- **sumr** - *bool/None*

```python
>>> mat1 = matx([[5,6,7],[3,4,1],[5,4,1]])
>>> mat = matutils.madd(mat, mat1, chk=True, ret='a')
'''
	mat, mat1 - matx objects
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat)
matx(
_____|__[0]__|___[1]____|__[2]___|
 (0) | '6.0' | '11.747' | '10.0' |
 (1) | '5.0' | '12.996' |  '5.0' |
 (2) | '6.0' | '13.245' |  '6.0' |
)

>>> sum_of_rows = matutils.madd(mat, mat1, False, True, 'a')
'''
	mat, mat1 - matx objects
	False - Return sum of elements at a row index in each column
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> sum_of_rows
(Decimal('45.747'), Decimal('30.996'), Decimal('35.245'))
```

xvi. **(cm) saddcnst(a, b, r=False, sumr=None, chk=True, ret='a') -> matx | tuple[Decimal, ...]**: Get the matrix as matx object after addition of a constant to each row or column in matrix of a matx object

- **a** - *list[ Decimal ] | tuple[Decimal, ...] | Decimal*
- **b** - *matx*
- **r** - *bool/None*
- **sumr** - *bool/None*

```python
>>> mat = matutils.saddcnst(0.4826, mat, None, chk=True, ret='a')
'''
	0.4826 - Number
	mat - matx object
	None - Add to all elements
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat)
matx(
_____|___[0]___|___[1]____|___[2]____|
 (0) | '6.483' | '12.230' | '10.483' |
 (1) | '5.483' | '13.479' |  '5.483' |
 (2) | '6.483' | '13.728' |  '6.483' |
)
 
>>> mat = matutils.saddcnst([0.1,0.2,0.3], mat, True, chk=True, ret='a')
'''
	[0.1,0.2,0.3] - Numbers
	mat - matx object
	True - Add to rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat)
matx(
_____|___[0]___|___[1]____|___[2]____|
 (0) | '6.583' | '12.330' | '10.583' |
 (1) | '5.683' | '13.679' |  '5.683' |
 (2) | '6.783' | '14.028' |  '6.783' |
)

```

xvii. **(sm) msub(a, b, sumr=None, chk=True, ret='a') -> matx | tuple[Decimal, ...]**: Get the matrix as a matx object after matrix subtraction for matrices of two matx objects

- **a** - *matx*
- **b** - *matx*
- **sumr** - *bool/None*

```python
>>> mat1 = matx([[1.1234,2.2123,12.2541,3],[1,5,4,2],[3,1,2,2]])
>>> mat2 = matx([[2,3,1,1],[3,3,5,6],[2,3,1,1]])
>>> mat = matutils.msub(mat1, mat2, chk=True, ret='a')
'''
	mat1, mat2 - matx objects
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat)
matx(
_____|___[0]____|___[1]____|___[2]____|__[3]___|
 (0) | '-0.877' | '-0.788' | '11.254' |  '2.0' |
 (1) |   '-2.0' |    '2.0' |   '-1.0' | '-4.0' |
 (2) |    '1.0' |   '-2.0' |    '1.0' |  '1.0' |
)

```

xviii. **(sm) smult(a, b, sumr=None, chk=False, ret='a') -> matx | tuple[Decimal, ...]**: Get the matrix as matx object after multiplication of a number

- **a** - *matx*
- **b** - *matx*
- **sumr** - *bool/None*

```python
>>> mat = matutils.smult(0.1595, mat)
'''
	0.1595 - Number
	mat - matx object
'''
>>> print(mat)
matx(
_____|___[0]____|___[1]____|___[2]___|___[3]____|
 (0) |  '-0.14' | '-0.126' | '1.795' |  '0.319' |
 (1) | '-0.319' |  '0.319' | '-0.16' | '-0.638' |
 (2) |   '0.16' | '-0.319' |  '0.16' |   '0.16' |
)

```

xix. **(cm) smultfac(a, b, r=True, sumr=None, chk=True, ret='a') -> matx | tuple[Decimal, ...]**: Get the matrix as a matx object after multiplication of a number to each row or column in matrix of a matx object

- **a** - *list[ Decimal ] | tuple[Decimal, ...]*
- **b** - *matx*
- **r** - *bool*
- **sumr** - *bool/None*

```python
>>> mat = matutils.smultfac([1,2,3,10], mat, False)
'''
	[1,2,3,10]
	mat
	False
'''
>>> print(mat)
matx(
_____|___[0]____|___[1]____|___[2]____|___[3]____|
 (0) | '-0.140' | '-0.252' |  '5.385' |  '3.190' |
 (1) | '-0.319' |  '0.638' | '-0.480' | '-6.380' |
 (2) |  '0.160' | '-0.638' |  '0.480' |  '1.600' |
)

```

xx. **(cm) mmult(a, b, t=(False, False), sumr=None, chk=True, ret='a') -> matx | tuple[Decimal, ...]**: Get the matrix as a matx object after matrix multiplication for matrices of two matx objects

- **a** - *matx*
- **b** - *matx*
- **t** - *tuple[bool, bool]*
- **sumr** - *bool/None*

```python
>>> mat = matutils.mmult(mat, mat1, (False, True))
'''
	mat, mat1 - matx objects
	(False, True) - Use transpose of 'mat1'
'''
>>> print(mat)
matx(
_____|____[0]____|____[1]____|____[2]____|
 (0) |  '74.843' |  '26.520' |  '16.478' |
 (1) | '-23.969' | '-11.809' | '-14.039' |
 (2) |   '9.450' |   '2.090' |   '4.002' |
)
>>> mat = matutils.mmult(mat1, mat2, (False, True), False)
>>> mat
(Decimal('137.5470'), Decimal('96.0'), Decimal('60.0'))
```

xxi. **(sm) melmult(a, b, t=(False, False), sumr=None, chk=True, ret='a') -> matx | tuple[Decimal, ...]**: Get the matrix as a matx object after multipling the elements at the same indexes of the matrices of two matx objects

- **a** - *matx*
- **b** - *matx*
- **t** - *tuple[bool, bool]*
- **sumr** - *bool/None*

```python
>>> mat = matutils.melmult(mat1, mat2)
'''
	mat1, mat2 - matx objects
'''
>>> print(mat)
matx(
_____|___[0]___|___[1]___|___[2]____|__[3]___|
 (0) | '2.246' | '6.636' | '12.254' |  '3.0' |
 (1) |   '3.0' |  '15.0' |   '20.0' | '12.0' |
 (2) |   '6.0' |   '3.0' |    '2.0' |  '2.0' |
)

```

xxii. **(sm) uldcompose(a, chk=True, ret='a') -> tuple[matx, matx, matx]**: Get a tuple with matx objects of upper triangular, diagonal, and lower triangular matrices for a matrix of a matx 

- **a** - *matx*

```python
>>> u,l,d = matutils.uldcompose(matutils.gele(mat, [0,1,2], False))
'''
	matutils.gele(mat, [0,1,2], False) - matx object to decompose
'''
>>> print("{}{}{}".format(u,l,d))
matx(
_____|__[0]__|__[1]__|__[2]__|
 (0) | '0.0' | '3.0' | '6.0' |
 (1) | '0.0' | '0.0' | '3.0' |
 (2) | '0.0' | '0.0' | '0.0' |
)
matx(
_____|___[0]____|__[1]___|__[2]__|
 (0) |    '0.0' |  '0.0' | '0.0' |
 (1) |  '6.636' |  '0.0' | '0.0' |
 (2) | '12.254' | '20.0' | '0.0' |
)
matx(
_____|___[0]___|__[1]___|__[2]__|
 (0) | '2.246' | '15.0' | '2.0' |
)

```

xxiii. **(cm) dpose(a, li, r=False, chk=True, ret='a') -> tuple[matx, ...]**: Get a tuple of matrices after decomposing a matrix of a matx object along the row or column direction

- **a** - *matx*
- **li** - *list[ int ] | tuple[int, ...]*
- **r** - *bool*

```python
>>> mats = matutils.dpose(mat, [2,2])
'''
	mat - matx object
	[2,2] - Number of columns to decompose
'''
>>> for i in mats:print(i, end="")
... 
matx(
_____|___[0]___|__[1]___|__[2]__|
 (0) | '2.246' |  '3.0' | '6.0' |
 (1) | '6.636' | '15.0' | '3.0' |
)
matx(
_____|___[0]____|__[1]___|__[2]__|
 (0) | '12.254' | '20.0' | '2.0' |
 (1) |    '3.0' | '12.0' | '2.0' |
)

```

xix. **(sm) moperate(a, chk=True, ret='a') -> matx | tuple[matx, ...]**: Returns the result after performing specified operations.

- **a**: *tuple[str, tuple[matx|tuple, ...]]*
	- 1<sup>st</sup> element is the operation to perform
	- If no operation is to be performed then the elements are matx objects
	- Operations:
		- ***"add"***: Perform addition of matrices in matx objects
		- ***"sub"***: Perform subtraction of matrices in matx objects from matrix in first matx object
		- ***"mul"***: Perform multiplication of matrices in matx objects
		- ***"invse"***: Get the inverse matrices for the matrices in matx objects
		- ***"lxtox"***: Convert matrices into row matrices of rows of matrices in matx objects
		- ***"xtolx"***: Convert row matrices in matx objects into matrix with rows as the rows in row matrices
		- ***"tpose"***: Get the transpose matrix of matrices in matx objects

```python
>>> mat1=matx([1.2311,2.23514,3.2365])
>>> mat2=matx([2.3254,5.2364,3.2541])
>>> mat3=matx([2.3121,2.3214,5.3211])
>>> mat=matutils.moperate(('add', (('xtolx', (mat1, mat2, mat3)), ('invse', (('xtolx', (mat2, mat1, mat3)),)))), True, 'a')
'''
	('add', (('xtolx', (mat1, mat2, mat3)), ('invse', (('xtolx', (mat2, mat1, mat3)),)))) - Operation sequence
	True - Check arguments
	 'a' - Ask to exit if error
'''
>>> print(mat)
matx(
_____|___[0]___|___[1]____|___[2]___|
 (0) | '1.811' | '-0.453' | '4.518' |
 (1) | '2.449' |  '5.878' | '2.788' |
 (2) | '2.006' |  '3.209' | '5.156' |
)

```

  </p>
</details>
<details>
  <summary>melutils</summary>
  <p>

**(c) melutils**: Methods for operations on rows/columns in matrix of a matx object 
  
i. **(sm) add(a, li, r=False, chk=True, ret='a') -> matx**: Get a matx object with matrix of rows as sum of elements in rows or columns in a matrix of a matx object

- **a** - *matx*
- **li** - *tuple[tuple[int, ...]] | list[list[ int ]] | 'all'*
- **r** - *bool*

```python
>>> mat=matx([[1.0121, 2.3202, 5.3214], [2.3202, 4.2555, 6.3111], [5.3236, 3.5895, 4.2314]])
>>> mat1=melutils.add(mat, [[1,2],[0,2]], False, True, 'a')
'''
	mat - matx object
	[[1,2],[0,2]] - List of list of column indexes of columns to add
	False - For columns
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'7.641', '10.567', '7.821'|
|'6.333', '8.631', '9.555'|
)

>>> mat1=melutils.add(mat, [[1,2],[0,2]], True, True, 'a')
'''
	mat - matx object
	[[1,2],[0,2]] - List of list of row indexes of rows to add
	True - For rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'7.644', '7.846', '10.542'|
|'6.336', '5.910', '9.552'|
)

```

ii. **(sm) mult(a, li, r=False, chk=True, ret='a') -> matx**: Get a matx object with matrix of rows as multiplication of elements in rows or columns in a matrix of a matx object

- **a** - *matx*
- **li** - *tuple[tuple[int, ...]] | list[list[ int ]] | 'all'*
- **r** - *bool*

```python
>>> mat1=melutils.mult(mat, [[1,2],[0,2]], False, True, 'a')
'''
	mat - matx object
	[[1,2],[0,2]] - List of list of column indexes of columns to multiply
	False - For columns
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'12.345', '26.86', '15.189'|
|'5.385', '14.642', '22.526'|
)

>>> mat1=melutils.mult(mat, [[1,2],[0,2]], True, True, 'a')
'''
	mat - matx object
	[[1,2],[0,2]] - List of list of row indexes of rows to multiply
	True - For rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'12.352', '15.279', '26.702'|
|'5.388', '8.329', '22.513'|
)

```

iii. **(sm) pow(an, a, li, r=False, chk=True, ret='a') -> matx**: Get a matx object with matrix of rows as exponentiation of elements in rows or columns in a matrix of a matx object

- **an** - *tuple[Decimal, Decimal]*
- **a** - *matx*
- **li** - *tuple[int, ...] | list[ int ] | 'all'*
- **r** - *bool*

```python
>>> mat1=melutils.pow((2, 2), mat, [0,1], False, True, 'a')
'''
	(2, 2) - Factor to multiply and power
	mat - matx object
	[0,1] - List of column indexes of columns to exponentiate
	False - For columns
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'4.097', '21.53', '113.38'|
|'21.53', '72.454', '51.552'|
)

>>> mat1=melutils.pow((2, 2), mat, [0,1], True, True, 'a')
'''
	(2, 2) - Factor to multiply and power
	mat - matx object
	[0,1] - List of row indexes of rows to exponentiate
	True - For rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'4.097', '21.53', '113.252'|
|'21.53', '72.454', '159.315'|
)

```

iv. **(sm) log(an, a, li, r=False, chk=True, ret='a') -> matx**: Get a matx object with matrix of rows as logarithm of elements in rows or columns in a matrix of a matx object

- **an** - *tuple[Decimal, Decimal]*
- **a** - *matx*
- **li** - *tuple[int, ...] | list[ int ] | 'all'*
- **r** - *bool*

```python
>>> mat1=melutils.log((2, 2), mat, [0,1], True, True, 'a')
'''
	(2, 2) - Factor to multiply and base
	mat - matx object
	[0,1] - List of row indexes of rows for logarithm
	True - For rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'1.017', '2.214', '3.412'|
|'2.214', '3.089', '3.658'|
)

>>> mat1=melutils.log((2, 2), mat, [0,1], False, True, 'a')
'''
	(2, 2) - Factor to multiply and base
	mat - matx object
	[0,1] - List of column indexes of columns for logarithm
	False - For columns
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'1.017', '2.214', '3.413'|
|'2.214', '3.089', '2.844'|
)

```

v. **(sm) expo(an, a, li, r=False, chk=True, ret='a') -> matx**: Get a matx object with matrix of rows as exponentiation of a number by elements in rows or columns in a matrix of a matx object

- **an** - *tuple[Decimal, Decimal]*
- **li** - *tuple[int, ...] | list[ int ] | 'all'*
- **r** - *bool*

```python
>>> mat1=melutils.expo((2, 2), mat, [0,1], False, True, 'a')
'''
	(2, 2) - Number to exponentiate and factor to multiply
	mat - matx object
	[0,1] - List of column indexes of columns for exponentiation
	False - For columns
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'4.067', '24.933', '1604.602'|
|'24.933', '365.063', '145.009'|
)

>>> mat1=melutils.expo((2, 2), mat, [0,1], True, True, 'a')
'''
	(2, 2) - Number to exponentiate and factor to multiply
	mat - matx object
	[0,1] - List of row indexes of rows for exponentiation
	True - For rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'4.067', '24.933', '1597.943'|
|'24.933', '365.063', '6303.774'|
)

```

vi. **(sm) trig(n, a, li, r=False, f='cos', chk=True, ret='a') -> matx**: Get a matx object with matrix of rows as trignometric function values for elements in rows or columns in a matrix of a matx object

- **n** - *Decimal*
- **a** - *matx*
- **li** - *tuple[int, ...] | list[ int ] | 'all'*
- **r** - *bool*
- **f** - *str*
	- 'sin', 'cos', 'tan', 'cosec', 'sec', 'cot', 'asin', 'acos', 'atan', 'asec', 'acosec', 'acot', 'sinh', 'cosh', 'tanh', 'sech', 'cosech', 'coth'

```python
>>> mat1=melutils.trig(2, mat, [0,1], False, 'tan', True, 'a')
'''
	2 - Factor to multiply
	mat - matx object
	[0,1] - List of column indexes of columns for trignometric operation
	False - For columns
	'tan' - Use the "tan" function
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'-2.053', '13.790', '2.760'|
|'13.790', '-1.294', '1.252'|
)

>>> mat1=melutils.trig(2, mat, [0,1], False, 'sinh', False, 'a')
'''
	2 - Factor to multiply
	mat - matx object
	[0,1] - List of column indexes of columns for trignometric operation
	False - For columns
	'sinh' - Use the "sinh" function
	False - Check arguments
	'a' - Ask to exit if error
'''
>>> print(mat1)
matx(
|'3.718', '51.767', '21054.143'|
|'51.767', '2487.050', '656.454'|
)

```

  </p>
</details>
<details>
  <summary>matstat</summary>
  <p>

**(c) matstat**: Methods for statistical analysis using matx object

```python
>>> from deciml_maths.matrix import matstat, matx
Imported deciml...
>>> from deciml_maths import setpr
>>> setpr(3)
```
  
i. **(sm) amean(a, el='row', chk=True, ret='a') -> tuple[Decimal, ...] | Decimal**: Get the arithmatic mean for all rows/columns/elements of matrix in matx object

- **a** - *matx*
- **el** - *str*
	- 'row'/'col'/'all'

```python
>>> mat=matx([[1.2312, 2.321, 5.3214, 3.23651, 5.2514, 5.3652, 4.32145],[12, 13.2642, 5.3251, 8.2569, 6.25412, 7.25631, 1.23651]])
>>> arith_mean_rows = matstat.amean(mat, 'row', True, 'a')
'''
	mat - matx object
	'row' - For all rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> arith_mean_rows
(Decimal('3.864'), Decimal('7.656'))
>>> arith_mean_cols = matstat.amean(mat, 'col', True, 'a')
'''
	mat - matx object
	'col' - For all columns
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> arith_mean_cols
(Decimal('6.616'), Decimal('7.793'), Decimal('5.323'), Decimal('5.747'), Decimal('5.753'), Decimal('6.311'), Decimal('2.779'))
>>> arith_mean = matstat.amean(mat, 'all', True, 'a')
'''
	mat - matx object
	'all' - For all elements in matrix
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> arith_mean
Decimal('5.760')
```

ii. **gmean(a, el='row', chk=True, ret='a') -> tuple[Decimal, ...] | Decimal**: Get the geometric mean for all rows/columns/elements of matrix in matx object

- **a** - *matx*
- **el** - *str*
	- 'row'/'col'/'all'

```python
>>> geo_mean_rows = matstat.gmean(mat, 'row', True, 'a')
'''
	mat - matx object
	'row' - For all rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> geo_mean_rows
(Decimal('3.466'), Decimal('6.301'))
>>> geo_mean_cols = matstat.gmean(mat, 'col', True, 'a')
'''
	mat - matx object
	'col' - For all columns
	True - Check arguments
	'a' - Ask to exit if error
'''       
>>> geo_mean_cols
(Decimal('3.843'), Decimal('5.549'), Decimal('5.323'), Decimal('5.17'), Decimal('5.731'), Decimal('6.239'), Decimal('2.312'))
>>> geo_mean = matstat.gmean(mat, 'all', True, 'a')
'''
	mat - matx object
	'all' - For all elements in matrix
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> geo_mean
Decimal('4.671')
```

iii. **hmean(a, el='row', chk=True, ret='a') -> tuple[Decimal, ...] | Decimal**: Get the harmonic mean for all rows/columns/elements of matrix in matx object

- **a** - *matx*
- **el** - *str*
	- 'row'/'col'/'all'

```python
>>> harm_mean_rows = matstat.hmean(mat, 'row', True, 'a')
'''
	mat - matx object
	'row' - For all rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> harm_mean_rows
(Decimal('0.426'), Decimal('0.635'))
>>> harm_mean = matstat.hmean(mat, 'all', True, 'a')
'''
	mat - matx object
	'all' - For all elements in matrix
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> harm_mean
Decimal('0.255')
```

iv. **qmean(a, el='row', chk=True, ret='a') -> tuple[Decimal, ...] | Decimal**: Get the quadratic mean of all rows/columns/elements of matrix in matx object

- **a** - *matx*
- **el** - *str*
	- 'row'/'col'/'all'

```python
>>> quad_mean_rows = matstat.qmean(mat, 'row', True, 'a')
'''
	mat - matx object
	'row' - For all rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> quad_mean_rows
(Decimal('3.466'), Decimal('6.301'))
>>> quad_mean = matstat.qmean(mat, 'all', True, 'a')
'''
	mat - matx object
	'all' - For all elements in matrix
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> quad_mean
Decimal('4.671')
```

v. **var(a, el='row', samp=True, chk=True, ret='a') -> tuple[Decimal, ...] | Decimal**: Get the sample or population variance of all rows/columns/elements of matrix in matx object

- **a** - *matx*
- **el** - *str*
	- 'row'/'col'/'all'
- **samp** - *bool*

```python
>>> samp_var_rows = matstat.var(mat, 'row', True, True, 'a')
'''
	mat - matx object
	'row' - For all rows
	True - Sample variance
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> samp_var_rows
(Decimal('2.703'), Decimal('16.574'))
>>> popul_var = matstat.var(mat, 'all', False, True, 'a')
'''
	mat - matx object
	'all' - For all elements in matrix
	False - Population variance
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> popul_var
Decimal('11.857')
```

vi. **sd(a, el='row', samp=True, chk=True, ret='a') -> tuple[Decimal, ...] | Decimal**: Get the sample or population standard deviation for all rows/columns/elements of matrix in matx object

- **a** - *matx*
- **el** - *str*
	- 'row'/'col'/'all'
- **samp** - *bool*

```python
>>> std_dev_rows = matstat.sd(mat, 'row', True, True, 'a')
'''
	mat - matx object
	'row' - For all rows
	True - Sample standard deviation
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> std_dev_rows
(Decimal('1.644'), Decimal('4.071'))
>>> popul_std_dev = matstat.sd(mat, 'all', False, True, 'a')
'''
	mat - matx object
	'all' - For all elements in matrix
	False - Population standard deviation
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> popul_std_dev
Decimal('3.443')
```

vii. **median(a, el='row', chk=True, ret='a') -> tuple[Decimal, ...] | Decimal**

- **a** - *matx*
- **el** - *str*
	- 'row'/'col'/'all'

```python
>>> median_rows = matstat.median(mat, 'row', True, 'a')
'''
	mat - matx object
	'row' - For all rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> median_rows
(Decimal('4.321'), Decimal('7.256'))
>>> median = matstat.median(mat, 'all', True, 'a')
'''
	mat - matx object
	'all' - For all elements in matrix
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> median
Decimal('5.323')
```

viii. **mode(a, el='row', chk=True, ret='a') -> tuple[dict, ...] | dict**

- **a** - *matx*
- **el** - *str*
	- 'row'/'col'/'all'

```python
>>> mat = matx([[1,2,4,6,4,3,4,5,6,4,3,4,5,6,4,4,4],[4,5,6,23,4,65,7,4,23,4,5,6,8,6,4,2,5]])
>>> mode_rows = matstat.mode(mat, 'row', True, 'a')
'''
	mat - matx object
	'row' - For all rows
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> mode_rows
({'values': (Decimal('4.0'),), 'mode': 8}, {'values': (Decimal('4.0'),), 'mode': 5})
>>> mode = matstat.mode(mat, 'all', True, 'a')
'''
	mat - matx object
	'all' - For all elements in matrix
	True - Check arguments
	'a' - Ask to exit if error
'''
>>> mode
{'values': (Decimal('4.0'),), 'mode': 13}
```

  </p>
</details>
</p>
</details>

<details>
<summary>Data</summary>
<p>
<details>
<summary>data</summary>
<p>

**(o) data**: Data object to store data values for independent (x) and dependent (y) variables

```python

```

i. **(g) data -> tuple[matx, tuple[Decimal, ...]]**: Get the data as a tuple with matx object of *x values* and tuple of *y values*

ii. **(g) datalen -> int**: Get the length of data

iii. **(g) xvars -> int**: Get the number of *x variables*

iv. **(g) pdata**: Print the data

v. **(f) getax() -> matx**: Get all *x values* as a matx object

vi. **(f) getay() -> tuple[Decimal, ...]**: Get all *y values* as a tuple

vii. **(f) getx(li, chk=True, ret='a') -> matx**: Get the *x values* at indexes

viii. **(f) gety(li, chk=True, ret='a') -> tuple[Decimal, ...]**: Get the *y values* at indexes

ix. **(f) getd(li, chk=True, ret='a') -> tuple[matx, tuple[Decimal, ...]]**: Get a tuple with matx object of *x values* and tuple of *y values* for indexes

x. **(f) getlx(li, chk=True, ret='a') -> matx**: Get the *x values* as a matx object for *x variable* at indexes

</p>
</details>
<details>
<summary>datautils</summary>
<p>

**(c) datautils**: Methods to use with data object

i. **dataval -> data**: Add a *x variable* with constant value to data

ii. **addata -> data**: Add *x variables* to data object

iii. **datalx -> data**: Get a data object with *x variables* at indexes

iv. **multlx -> data**: Get a data object with multiplication of *x variables* at indexes as added *x variables*

v. **addlx -> data**: Get a data object with addition of *x variables* at indexes as added *x variables* 

vi. **powlx -> data**: Get a data object with exponentiated *x variables* as added *x variables*

vii. **loglx -> data**: Get a data object with logarithm of *x variables* as added *x variables*

viii. **expolx -> data**: Get a data object with exponentiation using *x variables* as added *x variables*

ix. **triglx -> data**: Ge a data object with *x variables* after operation with a trignometric function as added *x variables*

</p>
</details>
</p>
</details>

<details>
<summary>Functions</summary>
<p>
</p>
</details>

