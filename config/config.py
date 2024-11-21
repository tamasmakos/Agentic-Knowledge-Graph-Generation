"""Configuration settings for the knowledge graph application."""
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class LLMConfig:
    model_name: str = "llama3-8b-8192"
    temperature: float = 0.3
    max_tokens: int = 4096
    top_p: float = 0.9

@dataclass
class GraphConfig:
    min_community_size: int = 3
    max_communities: int = 10
    embedding_dim: int = 384
    embedding_batch_size: int = 32
    node_size: int = 1500
    font_size: int = 8
    edge_font_size: int = 6
    figure_size: tuple = (12, 8)

@dataclass
class RateLimiterConfig:
    requests_per_minute: int = 30
    max_retries: int = 3
    base_delay: float = 1.0

@dataclass
class RAGConfig:
    max_chunks: int = 10
    chunk_size: int = 300
    chunk_overlap: int = 50
    top_k_communities: int = 3
    similarity_threshold: float = 0.7
    min_chunk_words: int = 5

class Config:
    """Main application configuration"""
    def __init__(self):
        self.DEBUG = False
        self.LLM = LLMConfig()
        self.GRAPH = GraphConfig()
        self.RATE_LIMITER = RateLimiterConfig()
        self.RAG = RAGConfig()
        
        # File paths
        self.GRAPH_SAVE_PATH = "knowledge_graph.gml"
        self.VISUALIZATION_PATH = "knowledge_graph.png"
        
        # Basic logging config
        self.LOGGING_CONFIG = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'standard': {
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                },
            },
            'handlers': {
                'default': {
                    'level': 'INFO',
                    'formatter': 'standard',
                    'class': 'logging.StreamHandler',
                }
            },
            'root': {
                'handlers': ['default'],
                'level': 'INFO',
            },
        }

# Create a global config instance
config = Config() 