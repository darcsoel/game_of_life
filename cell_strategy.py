class MutationStrategy:
    """
    Abstract strategy class to define survival of cell
    """

    cell_alive = True

    def __init__(self, cell: bool, neighborhood_count: int):
        self._cell = cell
        self._neighborhood_count = neighborhood_count

    def _check_cell_alive_condition(self):
        return self._cell == self.cell_alive

    def check_if_should_survive(self):
        """
        Check if cell should be mutated
        If not - should raise ValueError
        """
        raise NotImplementedError

    def mutate(self):
        if not self._check_cell_alive_condition():
            raise ValueError('wrong alive status to mutate')

        return self.check_if_should_survive()


class IsolatedStrategy(MutationStrategy):
    def check_if_should_survive(self):
        if self._neighborhood_count <= 1:
            return False
        raise ValueError('wrong strategy to mutate')


class SurvivalStrategy(MutationStrategy):
    def check_if_should_survive(self):
        if self._neighborhood_count in (2, 3):
            return True
        raise ValueError('wrong strategy to mutate')


class OvercrowdingStrategy(MutationStrategy):
    def check_if_should_survive(self):
        if self._neighborhood_count >= 4:
            return False
        raise ValueError('wrong strategy to mutate')


class ReproductionStrategy(MutationStrategy):
    cell_alive = False

    def check_if_should_survive(self):
        if self._neighborhood_count == 3:
            return True
        raise ValueError('wrong strategy to mutate')


mutation_strategies = (IsolatedStrategy,
                       SurvivalStrategy,
                       OvercrowdingStrategy,
                       ReproductionStrategy)


def mutation_context(cell, neighborhood_count):
    """
    Select correct strategy for cell mutation

    :param cell: Bool
    :param neighborhood_count: int
    :return: int or none
    """

    for strategy in mutation_strategies:
        instance = strategy(cell, neighborhood_count)

        try:
            mutated_cell = instance.mutate()
        except ValueError:
            continue

        return mutated_cell
