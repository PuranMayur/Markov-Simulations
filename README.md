# Markov Chains for Betting and Stock Analysis

**Tags:** Markov Chains, Stochastic Modeling, Stationary Distributions, Finance, Game Theory

---

## Overview

This project explores the application of **finite-state Markov chains** in two stochastic domains:

1. **Stock Price Dynamics**  
   Stock prices are modeled as Markov processes to analyze:
   - Transition probabilities between price states
   - Stationary distributions (long-run price behavior)
   - Expected time to reach certain price thresholds

2. **Gambling & Betting Strategies**  
   Betting systems are simulated using biased coin tosses and wealth constraints, allowing exploration of:
   - Win/loss probabilities over time
   - Adaptive betting strategies
   - Expected game durations and wealth evolution

---

## Features

- **Markov Chain Construction**: User-defined state space and transition matrix for both applications.
- **Stationary Distribution Computation**: Solves for long-run behavior using linear algebra.
- **Expected Hitting Times**: Calculates time to reach key states (e.g., profit/loss thresholds).
- **Betting Strategy Simulations**: Models gambler’s ruin, Martingale, and bounded-risk strategies.
- **Modular Design**: Code is cleanly separated into stock models and gambling models for extensibility.

---

## Use Cases

- Academic modeling of stochastic systems  
- Financial simulations of price movements  
- Game theory and optimal betting policy research  
- Teaching Markov processes through practical applications

---

## Tech Stack

- Language: Python / MATLAB / C++ (depending on your actual implementation)  
- Libraries (Python): `numpy` (for matrix ops and visualization)  
- Input: CSV for transitions or simulated parameters  
- Output: Console results, graphs for equilibrium distributions and trajectories

---

## Getting Started

### Prerequisites

- Python
- Required libraries:
  ```bash
  pip install numpy
