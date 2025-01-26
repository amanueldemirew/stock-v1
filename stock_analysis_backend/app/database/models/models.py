from sqlalchemy import (
    Column, String, Integer, Float, BigInteger,
    ForeignKey, TIMESTAMP, Text, UniqueConstraint,
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class StockMetadata(Base):
    __tablename__ = "stock_metadata"

    id = Column(Integer, primary_key=True)
    ticker = Column(String(10), nullable=False, unique=True)
    company_name = Column(String(255), nullable=False)
    market = Column(String(50))
    sector = Column(String(100))
    industry = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=func.now())

    # Relationships
    stock_data = relationship("StockData", back_populates="stock_metadata", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<StockMetadata(ticker={self.ticker}, company_name={self.company_name})>"

class StockData(Base):
    __tablename__ = "stock_data"

    id = Column(Integer, primary_key=True)
    ticker = Column(String(10), ForeignKey("stock_metadata.ticker", ondelete="CASCADE"), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(BigInteger, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # Unique constraint
    __table_args__ = (UniqueConstraint("ticker", "timestamp", name="uix_ticker_timestamp"),)

    # Relationships
    stock_metadata = relationship("StockMetadata", back_populates="stock_data")

    def __repr__(self):
        return f"<StockData(ticker={self.ticker}, timestamp={self.timestamp})>"

class AgentLogs(Base):
    __tablename__ = "agent_logs"

    id = Column(Integer, primary_key=True)
    agent_name = Column(String(100), nullable=False)
    ticker = Column(String(10))
    run_status = Column(String(50), nullable=False)
    message = Column(Text)
    run_time = Column(TIMESTAMP, server_default=func.now())

    def __repr__(self):
        return f"<AgentLogs(agent_name={self.agent_name}, ticker={self.ticker}, run_status={self.run_status})>"