from ml_bot.util import get_random_population
class AI():
    def __init__(self, model):
        self.model = model

    def predict(self, X):
        _, myDistribution =  self.model.predict(X)
        solution = get_random_population(myDistribution)
        return solution

