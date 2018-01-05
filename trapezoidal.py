from integral import Integral, Funktion

class Trapezoidal_integral(Integral):

    def make_integration_space(self):
        
        space = []
        i = self.lower + self.stepsize

        while ( i <= self.upper - self.stepsize ):

            space.append(i)
            i += self.stepsize

        return space

    def integrate(self):
        result = (self.function(self.lower)+ self.function(self.upper))*0.5
        for step in self.space :
            result += self.function(step)

        return self.stepsize * result


def x(x):
    return x


result = Trapezoidal_integral(2.0,0.0,Funktion(x)).integrate()

print(result)
