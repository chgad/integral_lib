import abc


class Funktion():
    
    def __init__(self, function):
        self.func = function
        self.name = function.__name__
    
    def get_function(self):
        return self.function


class Integral(abc.ABC):
    

    def __init__(self, upper, lower, function=None, integral_form=None):
        
        if not isinstance(upper, float):
            raise ValueError("Upperbound must be of type float")

        if not isinstance(lower, float):
             raise ValueError("Lowerbound must be of type float")

        if not isinstance(function, Funktion):
            raise ValueError("The given function must be a sub class of Function")
        
        if upper == lower:
            raise ValueError("Integralintervall must have a lenght > 0 .")

        self.upper = upper
        self.lower = lower
        self.function = function.func
        self.N = 100000.0
        self.stepsize = self.calc_stepsize()
        self.space = self.make_integration_space()

    def print_func_name(self):
        print("The function's name, to integrate , is  {}".format(self.function.name))
    
    @abc.abstractmethod
    def make_integration_space(self):
        pass
    
    @abc.abstractmethod
    def integrate(self):
        pass

    def calc_stepsize(self):
        return (self.upper - self.lower)/self.N


