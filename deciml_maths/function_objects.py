class function_as_dictionary:
    def __init__(self):
        self.axn_f=lambda __a,__n:{"*":{__a,{"**":('x',__n)}}}
        self.axn_df=lambda __a,__n:{"*":({"*":(__a,__n)},{"**":('x',{"-":(__n,"1")})})}
        self.poly_f=lambda __f:{"+":[self.axn_f(a,n) for a,n in __f]}
        self.poly_df=lambda __f:{"+":[self.axn_df(a,n) for a,n, in __f]}
        self.apolyn_f=lambda __a,__n,__f:{"*":{__a,{"**":(__f,__n)}}}
        self.apolyn_df=lambda __a,__n,__f,__df:{"+":({"*":({"*":{__a,{"**":(__f,__n)}}},__df)},{"*":({"*":{__a,{"**":(__f,__n)}}},__f)})}

__functions = function_as_dictionary()

class axn:
    '''
#### Object for a exponentiated variable.
- **__a**: The coefficient of variable
- **__n**: The power of variable
- **ret**: Exit type
    '''

    def __init__(self,__a:Decimal,__n:Decimal,ret:str='c')->None:
        try:
            self.__f=SolveEq(__functions.axn_f(__a,__n),'x')
            self.__df=SolveEq(__functions.axn_df(__a,__n),'x')
            self.f=lambda __a:self.__f.calculate(x=__a)[0];
            self.df=lambda __a:self.__df.calculate(x=__a)[0];
        except Exception as e:invalid_command('axn');retrn(ret,e);

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
    
    def __init__(self,*__f:tuple[Decimal,Decimal]|list[Decimal],ret:str='c')->None:
        try:
            self.__f=SolveEq(__functions.poly_f,'x');self.__df=SolveEq(__functions.poly_df,'x');
            self.f=lambda __x:self.__f.calculate(x=__x);
            self.df=lambda __x:self.__df.calculate(x=__x);
        except Exception as e:invalid_command("poly");retrn(ret,e);

    @property
    def getf(self)->tuple[tuple[Decimal,Decimal],...]:
        '''
#### Returns the coefficients and powers of polynomial as a tuple.
        '''
        return self.__f

    @property
    def getdf(self)->tuple[tuple[Decimal,Decimal],...]:
        '''
#### Returns the coefficients and powers of derivative of the polynomial as a tuple.
        '''
        return self.__df

class apolyn:
    '''
#### Object for a exponential of a polynomial.
- **__a**: Coefficient
- **__n**: Power
- **\*__f**: Coefficients and powers of polynomial.
- **ret**: Exit type
    '''

    def __init__(self,__a:Decimal,__n:Decimal,*__f:tuple[Decimal,Decimal]|list[Decimal],ret:str='a')->None:
        try:self.__f=SolveEq(__functions.apolyn_f(__a,__n,__functions.poly_f(__f)),'x');self.__df=SolveEq(__functions.apolyn_df(__a,__n,__functions.poly_f(__f),__functions.poly_df(__f)),'x');self.f=lambda __x:self.__f.calculate(__x);self.df=lambda __x:self.__df.calculate(__x);
        except Exception as e:invalid_command("apolyn");retrn(ret,e);

    @property
    def getf(self)->tuple[tuple[Decimal,Decimal],tuple[tuple[Decimal,Decimal],...]]:
        '''
#### Get all coefficients and powers of function.
        '''
        return self.__f

    @property
    def getdf(self)->tuple[tuple[Decimal,Decimal],tuple[tuple[Decimal,Decimal],...],tuple[tuple[Decimal,Decimal],...]]:
        '''
#### Get all coefficients and powers of function's derivative.
        '''
        return self.__df