import numpy as np

def stationary_distribution(p, q, r, N):
    """
    Return a list of size N+1 containing the stationary distribution of the Markov chain.
    
    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    
    """
    # Construct the transition matrix P
    P = np.zeros((N+1, N+1))
    for k in range(1, N):
        P[k, k-1] = q[k]
        P[k, k] = r[k]
        P[k, k+1] = p[k]
    
    # Boundary conditions
    P[0, 0] = r[0]
    P[0, 1] = p[0]
    P[N, N] = r[N]
    P[N, N-1] = q[N]
    
    # Solve for the stationary distribution
    A = P.T - np.eye(N+1)
    A[N] = np.ones(N+1)  # Normalization condition
    b = np.zeros(N+1)
    b[N] = 1
    
    pi = np.linalg.solve(A, b)
    return pi
    pass

def expected_wealth(p, q, r, N):
    """
    Return the expected wealth of the gambler in the long run.

    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    """
    pi = stationary_distribution(p, q, r, N)
    return sum(k * pi[k] for k in range(N+1))
    
    
def expected_time(p, q, r, N, a, b):
    """
    Return the expected time for the price to reach b starting from a.

    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    a : int, the starting price
    b : int, the target price
    """
    if a == b:
        return 0

    # Set up system of linear equations for hitting times
    T = np.zeros(N+1)
    A = np.eye(N+1)  # Identity matrix for equation coefficients
    B = np.ones(N+1)  # Right-hand side vector, which is 1 for all T_k
    
    # Modify equations for each state
    for k in range(N+1):
        if k == b:
            # T_b = 0 (target state)
            A[k, k] = 1
            B[k] = 0
        else:
            # General case T_k = 1 + p_k * T_{k+1} + q_k * T_{k-1} + r_k * T_k
            A[k, k] = 1 - r[k]  # Coefficient for T_k
            if k > 0:
                A[k, k-1] = -q[k]  # Coefficient for T_{k-1}
            if k < N:
                A[k, k+1] = -p[k]  # Coefficient for T_{k+1}
    
    # Solve for T using linear algebra
    T = np.linalg.solve(A, B)
    return T[a]
    pass

if __name__ == "__main__":
    # Test case for expected_time function
    p = [0.3] * 101  # Probability of price increase
    q = [0.3] * 101  # Probability of price decrease
    r = [0.4] * 101  # Probability of price remaining the same
    N = 100  # Maximum price of the stock
    a = 50  # Starting price
    b = 75  # Target price

    result = expected_time(p, q, r, N, a, b)
    print(f"Expected time for the price to reach {b} starting from {a}: {result}")