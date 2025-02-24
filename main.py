# rag_system/main.py


#This main.py script acts as the orchestration layer for the entire RAG system, coordinating the ingestion, retrieval, response generation, and evaluation. It ensures that each component works together seamlessly and provides logging for tracking the system’s behavior.



import logging
from ingestion import IngestionPipeline
from rag_pipeline import RagPipeline
from evaluation import DeepEval, Ragas, TrueLens, Galileo
from utils import setup_logger, log_metrics, load_config

# Setup logger
logger = setup_logger()

def main():
    try:
        # Load system configuration
        config = load_config("config.json")
        logger.info("Configuration loaded successfully.")

        # Step 1: Ingestion - Preprocess and ingest documents
        ingestion_pipeline = IngestionPipeline(config)
        logger.info("Starting document ingestion...")
        documents = ingestion_pipeline.run()
        logger.info(f"Successfully ingested {len(documents)} documents.")

        # Step 2: Retrieval and Response Generation - Perform RAG
        rag_pipeline = RagPipeline(config, documents)
        logger.info("Starting RAG pipeline...")
        query = "What is the capital of France?"
        response = rag_pipeline.run(query)
        logger.info(f"Generated response: {response}")

        # Step 3: Evaluate the generated response
        logger.info("Starting evaluation...")
        deeval = DeepEval()
        ragas = Ragas()
        truelens = TrueLens()
        galileo = Galileo()

        # Evaluate response accuracy (e.g., using DeepEval)
        accuracy = deeval.evaluate(response, "Paris")
        log_metrics(logger, "response_accuracy", accuracy['accuracy'])

        # Evaluate relevance with retrieved documents (e.g., using Ragas)
        relevance = ragas.evaluate(response, documents)
        log_metrics(logger, "response_relevance", relevance['relevance'])

        # Evaluate coherence (e.g., using TrueLens)
        coherence = truelens.evaluate(response, documents)
        log_metrics(logger, "response_coherence", coherence['coherence'])

        # Evaluate user satisfaction (e.g., using Galileo)
        user_feedback = {"rating": 4.5}  # Example user feedback
        user_satisfaction = galileo.evaluate(response, user_feedback)
        log_metrics(logger, "user_satisfaction", user_satisfaction['user_satisfaction'])

        # Output results
        logger.info("RAG system evaluation completed successfully.")
        logger.info(f"Final Generated Response: {response}")

    except Exception as e:
        logger.error(f"An error occurred during execution: {str(e)}")
        raise

if __name__ == "__main__":
    main()
