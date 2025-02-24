# evaluation/__init__.py

# Import core evaluation components for easy access
from .deeval import DeepEval
from .ragas import Ragas
from .truelens import TrueLens
from .galileo import Galileo

# Define versioning or configuration related to the evaluation pipeline
__version__ = '1.0.0'

# Expose the essential classes/functions in the public API
__all__ = [
    'DeepEval',
    'Ragas',
    'TrueLens',
    'Galileo'
]

###########################################################################################################
# Example of how to use the evaluation module

from evaluation import DeepEval, Ragas, TrueLens, Galileo

# Example response and ground truth for evaluation
response = "The capital of France is Paris."
ground_truth = "Paris"

# Step 1: Evaluate response accuracy using DeepEval
deeval = DeepEval()
accuracy = deeval.evaluate(response, ground_truth)
print(f"Accuracy: {accuracy['accuracy']}")

# Example context and documents for relevance and coherence evaluation
retrieved_docs = ["Paris is known as the City of Light.", "It is the capital of France."]

# Step 2: Evaluate response relevance using Ragas
ragas = Ragas()
relevance = ragas.evaluate(response, retrieved_docs)
print(f"Relevance: {relevance['relevance']}")

# Step 3: Evaluate coherence with retrieved documents using TrueLens
truelens = TrueLens()
coherence = truelens.evaluate(response, retrieved_docs)
print(f"Coherence: {coherence['coherence']}")

# Step 4: Evaluate user satisfaction or general performance using Galileo
user_feedback = {"rating": 4.5}  # Example user feedback (e.g., rating out of 5)
galileo = Galileo()
user_satisfaction = galileo.evaluate(response, user_feedback)
print(f"User Satisfaction: {user_satisfaction['user_satisfaction']}")

