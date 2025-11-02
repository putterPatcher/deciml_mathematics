from deciml_maths import *
from terminate import retrn

class axn:
    '''
#### Object for a exponentiated variable.
- **__f1**: The coefficient of variable
- **__f2**: The power of variable
- **ret**: Exit type
    '''

    def __init__(self,__f1:Decimal,__f2:Decimal,ret:str='a')->None:
        try:
            __pr=getpr()+1
            self.__f=tuple(map(deciml,(__f1,__f2)));self.__df=(alg.mul(*self.__f,pr=__pr),alg.sub(self.__f[1],'1',pr=__pr));del __f1,__f2,__pr;
            self.f=lambda __a:alg.mul(self.__f[0],alg.pwr(__a,self.__f[1],getpr()+2),pr=getpr())
            self.df=lambda __a:alg.mul(self.__df[0],alg.pwr(__a,self.__df[1],getpr()+2),pr=getpr())
        except Exception as e:print("Invalid command: axn()");retrn(ret,e);

    @property
    def getf(self)->tuple[Decimal,Decimal]:
        '''
#### Get the coefficient and power of function.
        '''
        return self.__f;

    @property
    def getdf(self)->tuple[Decimal,Decimal]:
        '''
#### Get the coefficient and power of derivative.
        '''
        return self.__df;

class poly:
    '''
#### Object for a polynomial.
- **\*__f**: List of coefficients and powers
- **ret**: Exit type
    '''
    
    def __init__(self,*__f:tuple[Decimal,Decimal]|list[Decimal],ret:str='a')->None:
        try:
            self.__f=tuple(map(lambda x:axn(*x),__f));del __f;
        except Exception as e:print("Invalid command: poly()");retrn(ret,e);

    def f(self,__a:Decimal):setpr(getpr()+1);r=map(lambda i:i.f(__a),self.__f);setpr(getpr()-1);return alg.add(*r,pr=getpr());

    def df(self,__a:Decimal):setpr(getpr()+1);r=map(lambda i:i.df(__a),self.__f);setpr(getpr()-1);return alg.add(*r,pr=getpr());

    @property
    def getf(self)->tuple[tuple[Decimal,Decimal],...]:
        '''
#### Returns the coefficients and powers of polynomial as a tuple.
        '''
        return tuple(map(lambda i:i.getf,self.__f));

    @property
    def getdf(self)->tuple[tuple[Decimal,Decimal],...]:
        '''
#### Returns the coefficients and powers of derivative of the polynomial as a tuple.
        '''
        return tuple(map(lambda i:i.getdf,self.__f));

class apolyn:
    '''
#### Object for a exponential of a polynomial.
- **__a**: Coefficient
- **__n**: Power
- **\*__f**: Coefficients and powers of polynomial.
- **ret**: Exit type
    '''

    def __init__(self,__a:Decimal,__n:Decimal,*__f:tuple[Decimal,Decimal]|list[Decimal],ret:str='a')->None:
        try:
            pr=getpr()
            self.__an=axn(__a,__n,pr);self.__f=poly(*__f,pr=pr+1);del __a,__n,__f,pr;
            self.f=lambda __a,__pr=getpr():self.__an.f(self.__f.f(__a,__pr+1),__pr)
            self.df=lambda __a,__pr=getpr():alg.mul(self.__an.df(self.__f.f(__a,__pr+2),__pr+1),self.__f.df(__a,__pr+1),pr=__pr)
        except Exception as e:print("Invalid command: apolyn()");retrn(ret,e);

    @property
    def getf(self)->tuple[tuple[Decimal,Decimal],tuple[tuple[Decimal,Decimal],...]]:
        '''
#### Get all coefficients and powers of function.
        '''
        return self.__an.getf(),self.__f.getf();

    @property
    def getdf(self)->tuple[tuple[Decimal,Decimal],tuple[tuple[Decimal,Decimal],...],tuple[tuple[Decimal,Decimal],...]]:
        '''
#### Get all coefficients and powers of function's derivative.
        '''
        return self.__an.getdf(),self.__f.getf(),self.__f.getdf();

class funcutils:
    
    @staticmethod
    def rearr(__a,__pos:int,ret:str='a')->apolyn:
        '''
#### Get the rearranged function (x as a function of x).
- **__a**: The function
- **__pos**: The position at which to rearrange
        '''
        try:
            ta=__a.__class__.__name__;a=__a.getf();__pr=getpr();
            match ta:
                case 'poly':p=(a:=list(a)).pop(__pos);return apolyn(alg.pwr(alg.div('1',p[0],__pr+2),(pw:=alg.div('1',p[1],__pr+2)),__pr+1),pw,*a,pr=__pr);
                case _:return None;
        except Exception as e:print("Invalid command: funcutils.rearr()");retrn(ret,e);

    @staticmethod
    def ndpoly(p:poly,n:int)->poly|None:
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
        except Exception as e:print("Invalid command: funcutils.ndpoly()");retrn('c',e);


# a=poly((2,3),(1,-2))
# print(a.f(1),a.df(1),a.getdf())
# a=apolyn(2,1,(1,2),(2,1))
# print([a.f(1),a.df(1)],a.getf())
# print(a.getdf())
