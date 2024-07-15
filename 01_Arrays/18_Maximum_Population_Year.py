class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Create an array to track changes in population for each year from 1950 to 2050
        population_changes = [0] * 101
        # It will create an array with 101 array size with all elements as 0

        for birth, death in logs:
            population_changes[birth - 1950] += 1
            population_changes[death - 1950] -= 1

        # Compute the population for each year using the cumulative sum
        max_population = 0
        max_year = 1950
        current_population = 0

        for year in range(101):
            current_population += population_changes[year]
            if current_population > max_population:
                max_population = current_population
                max_year = 1950 + year

        return max_year

"""
Explanation:
1.Initialization:
  We create an array population_changes with 101 elements (corresponding to years 1950 to 2050).

2.Population Changes:
  For each log entry [birth, death], we increment the birth year and decrement the death year in the      population_changes array.

3.Cumulative Population:
  We use a cumulative sum to calculate the population for each year based on the changes recorded.

4.Find Maximum Population Year:
  We iterate through the population_changes array to find the year with the highest population.
"""