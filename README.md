# Portfolio-Optimization-Project
1. Abstract

This project explores the application of Genetic Algorithms (GAs) for optimizing investment portfolios. Portfolio optimization involves selecting the best combination of assets to achieve maximum returns with minimal risk. Traditional approaches often face difficulties with large datasets and non-linear constraints. Genetic Algorithms, inspired by natural selection, provide a robust alternative. In this project, real-valued encoding is used to represent portfolios, and the fitness function is based on the Sharpe Ratio. The algorithm evolves a population of portfolios over several generations using selection, crossover, and mutation to converge towards an optimal asset allocation. The results demonstrate the effectiveness of GAs in financial decision-making.

2. Introduction

Investment portfolio optimization is a critical aspect of financial management. It aims to allocate capital among different assets in a way that maximizes return and minimizes risk. Traditional models like the Markowitz Mean-Variance model require assumptions that may not hold in real markets. Moreover, these models are less effective with complex constraints or large datasets.

Genetic Algorithms (GAs) offer a flexible and powerful optimization technique inspired by the principles of evolution and natural selection. GAs do not require gradient information and are well-suited for multi-objective problems with multiple constraints. This project applies GA to optimize asset allocation in a portfolio using historical stock data.

3. Algorithm Used: Genetic Algorithm (GA)

3.1 Overview

Genetic Algorithm is a heuristic search method that mimics natural evolutionary processes. It starts with a randomly generated population and applies genetic operators like selection, crossover, and mutation to evolve better solutions over time.

3.2 Why GA for Portfolio Optimization

Handles non-linear and complex problems

No need for derivatives

Suitable for large search spaces

Can incorporate real-world constraints

Effectively optimizes non-linear objective functions like the Sharpe Ratio

3.3 GA Components in This Project

Chromosome: Represents a portfolio (asset weights)

Gene: Individual asset weight

Population: Group of portfolios

Fitness Function: Sharpe Ratio

Selection: Tournament Selection

Crossover: Arithmetic Crossover

Mutation: Random Mutation with Re-normalization

4. Methods Used from GA

4.1 Chromosome Representation

Real-valued encoding

Example: [0.2, 0.3, 0.1, 0.4] for 4 assets

Sum of weights = 1

4.2 Initialization Method

Random generation of weights

Normalization to ensure the sum is 1

4.3 Fitness Function

Based on Sharpe Ratio:


Measures risk-adjusted return

4.4 Selection Method

Tournament Selection

Random subset selection, choose best performer

4.5 Crossover Method

Arithmetic Crossover:


4.6 Mutation Method

Randomly alter a weight

Re-normalize to keep sum = 1

4.7 Termination Method

Fixed number of generations (e.g., 100)

Early stopping if no improvement in fitness

