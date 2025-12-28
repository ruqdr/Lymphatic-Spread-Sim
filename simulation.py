"""
Simplified simulation of lymphatic metastasis for educational purposes.
"""

class Node:
    """Represents a lymph node."""
    def __init__(self, size):
        self.size = size  # size in centimeters

class CancerCell:
    """Represents a cancer cell."""
    def __init__(self, phenotype):
        self.phenotype = phenotype

def calculate_entrapment_probability(node, cell):
    """
    Calculate the probability that a cancer cell is trapped (entrapped) in a lymph node.
    
    Args:
        node (Node): The lymph node object.
        cell (CancerCell): The cancer cell object.
    
    Returns:
        float: Probability of entrapment.
    """
    # Biologically plausible linear model: larger nodes have more complex sinus structure
    # leading to higher entrapment probability. Base probability 0.2 for smallest nodes,
    # with 0.1 increase per cm. Cap at 0.9 for realism.
    probability = 0.2 + (node.size * 0.1)
    return min(probability, 0.9)

def simulate_metastasis(nodes, cells):
    """
    Simulate the spread of cancer cells through a chain of lymph nodes.
    """
    results = []
    for cell in cells:
        trapped = False
        for node in nodes:
            prob = calculate_entrapment_probability(node, cell)
            # Simple random trapping (not implemented)
            # For demonstration, we just record probability
            results.append((node.size, prob))
    return results

if __name__ == "__main__":
    # Example usage
    nodes = [Node(1.0), Node(2.0), Node(0.5)]
    cells = [CancerCell("invasive")]
    results = simulate_metastasis(nodes, cells)
    print("Simulation results:", results)