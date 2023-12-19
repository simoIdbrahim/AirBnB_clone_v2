from sqlalchemy import ForeignKey

class Place(BaseModel, Base):
    """Place class for storing place information."""
    __tablename__ = "places"
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # Add other columns for Place class

class User(BaseModel, Base):
    """User class for storing user information."""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
