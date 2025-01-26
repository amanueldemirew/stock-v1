from .connection import DatabaseConnection
from .models.models import Base, StockMetadata, StockData, AgentLogs

# Create a database instance
db = DatabaseConnection()

# Export commonly used components
__all__ = ['db', 'Base', 'StockMetadata', 'StockData', 'AgentLogs']