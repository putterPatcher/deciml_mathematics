from deciml_maths import *
from terminate import retrn
from .__helpers import invalid_command
from deciml.deciml import SolveEq

class funcutils:
    
    @staticmethod
    def rearr(__a,__pos:int,ret:str='c')->apolyn:
        '''
#### Get the rearranged function (x as a function of x).
- **__a**: The function
- **__pos**: The position at which to rearrange
        '''
        try:
            ta=__a.__class__.__name__;a=__a.getf();
            match ta:
                case 'poly':p=(a:=list(a)).pop(__pos);return apolyn(alg.pwr(alg.div('1',p[0],getpr()+1),alg.div('1',p[1],getpr()+1)),alg.div('1',p[1]),*a);
                case _:return None;
        except Exception as e:invalid_command("funcutils.rearr");retrn(ret,e);

    @staticmethod
    def ndpoly(p:poly,n:int,ret='c')->poly|None:
        '''
#### Differentiate a polynomial n number of times.
- **p**: poly object
- **n**: Number of times to differentiate
        '''
        try:
            for _ in range(n):
                p = poly(*p.getdf())
                if p is None:return None;
            return p
        except Exception as e:invalid_command("funcutils.ndpoly");retrn('c',e);

class SolveFn:
    def __init__(self,fn:SolveEq|poly|apolyn,ret:str='c'):
        try:
            if (tf:=fn.__class__.__name__=='SolveEq') or tf=='poly' or tf=='apolyn':
                self.__fn=fn
        except Exception as e:invalid_command('SolveFn');retrn(ret,e);

    @property
    def fn():
        '''
#### Get the SolveFn object
        '''
        return self.__fn
    
    def rootrearr(self):pass

    def bchop(self):pass

    def lininter(self):pass

    def nrinter(self):pass

# a=poly((2,3),(1,-2))
# print(a.f(1),a.df(1),a.getdf())
# a=apolyn(2,1,(1,2),(2,1))
# print([a.f(1),a.df(1)],a.getf())
# print(a.getdf())
