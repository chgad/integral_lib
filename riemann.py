from .integral import Function, Integral


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


