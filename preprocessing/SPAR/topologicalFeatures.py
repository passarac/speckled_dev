import numpy as np
#from persim import PersistenceEntropy
from gtda.diagrams import PersistenceEntropy
from gtda.homology import VietorisRipsPersistence


def betti_numbers(ak: np.ndarray, bk: np.ndarray) -> tuple[int, int]:
    """
    Computes Betti numbers using Persistent Homology for the SPAR attractor projection.

    Parameters:
    -----------
    ak : np.ndarray
        1D array representing the `a_k` coordinate from the SPAR projection.
    bk : np.ndarray
        1D array representing the `b_k` coordinate from the SPAR projection.

    Returns:
    --------
    tuple[int, int]
        Betti numbers (β₀, β₁), where:
        - β₀ represents the number of connected components.
        - β₁ represents the number of loops in the attractor.
    """
    spar_data = np.vstack((ak, bk)).T  # Convert to 2D array
    VR = VietorisRipsPersistence(metric="euclidean", homology_dimensions=[0, 1])
    diagrams = VR.fit_transform([spar_data])

    β0 = len(diagrams[0][0])  # Number of connected components
    β1 = len(diagrams[0][1])  # Number of loops

    return β0, β1



def persistent_entropy(ak: np.ndarray, bk: np.ndarray) -> float:
    """
    Computes Persistent Homology Entropy for the SPAR attractor projection.

    Parameters:
    -----------
    ak : np.ndarray
        1D array representing the `a_k` coordinate from the SPAR projection.
    bk : np.ndarray
        1D array representing the `b_k` coordinate from the SPAR projection.

    Returns:
    --------
    float
        Persistent Homology Entropy, which quantifies the complexity of topological features.
        Higher values indicate more persistent and complex structures in the attractor.
    """
    spar_data = np.vstack((ak, bk)).T
    VR = VietorisRipsPersistence(metric="euclidean", homology_dimensions=[0, 1])
    diagrams = VR.fit_transform([spar_data])
    return PersistenceEntropy().fit_transform(diagrams)[0]