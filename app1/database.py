from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL (here using SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./my_first_database.db"
# For PostgreSQL use: "postgresql://user:password@postgresserver/db"

# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False}
)

# engine: Core interface to the database.

# check_same_thread=False: Specific to SQLite; allows SQLAlchemy to work across multiple threads.



# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# create a base class for model class to inherit from 
Base = declarative_base()


# 🔧 What engine Does:
# The engine is how SQLAlchemy communicates with your database.

# Think of it like:

# A database driver + connection manager.

# The central object that SQLAlchemy uses to:

# Connect to the database.

# Send SQL queries.

# Receive results.


# 🔄 How It Works in Practice:
# When you run:

# python
# Copy
# Edit
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# You’re:

# Creating a database connection pool.

# Defining how to talk to the database (what type, where it's located, what credentials to use, etc.).

# Analogy:
# The engine is like the delivery truck that knows how to reach your database.

# The session is like the package handler who loads and unloads data using that truck.

# 🔄 What is a Database Connection?
# Whenever your app talks to a database (e.g., to get or save data), it needs to open a connection.

# A connection is like a phone call between your app and the database.

# But opening and closing these connections every time is slow and resource-heavy.

# 🏊‍♂️ What is a Connection Pool?
# A connection pool is like a pool of pre-opened phone lines (connections) that your app can reuse.

# Instead of opening a new connection each time, your app just borrows one from the pool.

# When done, it returns it back to the pool — ready for the next use.

# ✅ Benefits of a Connection Pool
# Faster performance – No need to open a new connection every time.

# Better resource management – Avoids flooding the database with too many connections.

# Scalability – Can handle more users efficiently.

# 🔧 In SQLAlchemy
# When you run:

# python
# Copy
# Edit
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SQLAlchemy automatically creates a connection pool behind the scenes.

# The engine object manages this pool and handles borrowing/returning connections.

# You can even customize the pool size like this:

# python
# Copy
# Edit
# engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20)
# 🧠 Analogy:
# Imagine your app is a call center:

# Instead of dialing a customer every time (new connection),

# You have 10 active phone lines (connection pool),

# Agents (your app logic) pick up and use any available line,

# Once done, they put the phone back on the hook for the next person.

# Great! Let's fully explain this important line:

# python
# Copy
# Edit
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# This line creates a session factory—a callable you can use to get a database session whenever you need it.

# 🧠 What is a Session in SQLAlchemy?
# A Session in SQLAlchemy:

# Is the main way to interact with the database.

# Represents a "workspace" for doing things like:

# Adding or querying data

# Committing transactions

# Rolling back on errors

# Think of it like opening a tab or draft version of your database operations.

# 🧱 Breaking Down the Parameters:
# 1. autocommit=False
# ⚠️ This means you must call session.commit() manually.

# It ensures you have full control over when changes are saved.

# Safer: you can review or cancel before committing.

# 2. autoflush=False
# Prevents the session from automatically sending changes to the database before each query.

# Gives you control over when your changes are flushed (sent but not committed).

# You can manually call session.flush() when needed.

# 3. bind=engine
# This tells the session: "Use this engine to connect to the database."

# It connects this session to the database you configured earlier with create_engine().

# 🛠️ So what is SessionLocal?
# It’s a factory—you call it to get a new session:

# python
# Copy
# Edit
# db = SessionLocal()
# And use it like this:

# python
# Copy
# Edit
# try:
#     # do DB operations like db.query(...), db.add(...)
#     db.commit()
# except:
#     db.rollback()
# finally:
#     db.close()
# 🧠 Analogy:
# SessionLocal is like a session-making machine.

# Each time you call SessionLocal(), you get a new database session you can use for transactions.









