# CollatzSequence


This repository contains the evaluation data and Python scripts for a novel approach to the Collatz conjecture. Instead of treating the problem as a sequence of random operations, this project analyzes the dynamics of the Collatz process through a newly introduced structural metric, Ω R.
The central hypothesis is that the Collatz dynamics are not chaotic but exhibit marginal stability with respect to the Ω R metric.

Key Findings
Boundedness: All analyzed sequences show a clear boundedness of the Ω R metric. The maximum values (max_omega_R) remain within a very narrow range, supporting the idea of a global upper bound on structural complexity.
Negative Drift: The Lyapunov exponent (λ) for the Ω R metric is predominantly negative or near zero. This provides strong statistical evidence against an uncontrolled increase in complexity and indicates a systematic drift towards simpler structures.
Complexity Reduction: The number of "downward" transitions in the Ω R metric consistently outweighs the number of "upward" transitions, confirming the complexity-reducing nature of the Collatz process on average.

Repository Contents
collatz_analysis_*.csv: CSV files containing the raw evaluation data for various ranges of starting numbers. Each row represents a starting number and its key metrics, such as max_omega_R and lyapunov_exponent.
analyze_collatz_sequence.py: The Python script used to generate the data, including the implementation of the Ω R metric and the calculation of the Lyapunov exponents.

