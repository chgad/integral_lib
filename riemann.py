from integral import Funktion, Integral


class Riemann_left_sum(Integral):

    
    def make_integration_space(self):
        
        space = []
        i = self.lower

        while ( i <= self.upper - self.stepsize ):

            space.append(i)
            i+= self.stepsize


        return space
    
    def integrate(self):

        result = 0
        
        for step in self.space:
            result += self.stepsize * self.function(step)

        
        return result

class Riemann_right_sum(Riemann_left_sum):

     def make_integration_space(self):
        
        space = []
        i = self.lower + self.stepsize

        while ( i <= self.upper ):

            space.append(i)
            i+= self.stepsize


        return space

def x(x):
    return x


result_one = Riemann_left_sum(2.0,0.0,Funktion(x)).integrate()
result_two = Riemann_right_sum(2.0,0.0, Funktion(x)).integrate()

print(result_one, result_two)
