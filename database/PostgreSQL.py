```python
import psycopg2
from psycopg2 import sql

def create_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="baseball_agent_assistant",
        user="username",
        password="password"
    )
    return conn

def create_tables():
    commands = (
        """
        CREATE TABLE Players (
            PlayerID SERIAL PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            ContactInfo VARCHAR(255),
            TeamAffiliation VARCHAR(255),
            ContractDetails VARCHAR(255),
            PerformanceStatistics VARCHAR(255)
        )
        """,
        """
        CREATE TABLE Teams (
            TeamID SERIAL PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            ContactInfo VARCHAR(255),
            CommunicationHistory VARCHAR(255)
        )
        """,
        """
        CREATE TABLE Contracts (
            ContractID SERIAL PRIMARY KEY,
            PlayerID INTEGER,
            TeamID INTEGER,
            Details VARCHAR(255),
            NegotiationProgress VARCHAR(255),
            DealTerms VARCHAR(255),
            FOREIGN KEY (PlayerID)
                REFERENCES Players (PlayerID)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (TeamID)
                REFERENCES Teams (TeamID)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE ScoutingReports (
            ReportID SERIAL PRIMARY KEY,
            PlayerID INTEGER,
            ReportDetails VARCHAR(255),
            FOREIGN KEY (PlayerID)
                REFERENCES Players (PlayerID)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )
    conn = None
    try:
        conn = create_connection()
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
```