# Base setup and basics

### Folder Structure

![image](https://github.com/user-attachments/assets/9c01aa86-aadb-4818-ba94-ab53839cea6d)

### Models (Like Spring @Entity)

![image](https://github.com/user-attachments/assets/fbfd4969-8942-414d-ad69-c7ec5a814fa0)

- SwiftCode inherits from Base, making it an SQLAlchemy model that will be mapped to a database table.

- relationship("SwiftCode", remote_side=[swift_code]) establishes a self-referential relationship, allowing an entry to be linked to its headquarters.

- remote_side=[swift_code] ensures that the headquarter_id refers to another row within the same table.

### Pydantic Schemas (Like Spring DTOs)

![image](https://github.com/user-attachments/assets/90a93429-87b4-4646-9d49-b07b8fb46e5b)

### Repositories

![image](https://github.com/user-attachments/assets/d1ca9aec-71d4-41cd-9d3a-a37b7efa9137)

### Service Layer

![image](https://github.com/user-attachments/assets/86f7bd12-81d1-4c0a-aabf-f45863cf82ff)

### Routes (Like Spring @RestController)

![image](https://github.com/user-attachments/assets/b126a423-c9e4-4d6c-bd35-3b6a08e27d32)

### Config file

![image](https://github.com/user-attachments/assets/ba9f8e9f-68a5-48fa-9e70-cc91cf617fb6)

- sqlalchemy.create_engine: Creates a connection to a database.

- sqlalchemy.orm.declarative_base: Provides a base class for defining ORM models.

- DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://dbuser:dbpass@localhost:5430/swift_db")
- Retrieves the database connection string from the DATABASE_URL environment variable. If the variable is not set then it sets default value

### Database file

![image](https://github.com/user-attachments/assets/20f20329-42ae-41b7-87f8-8dac74eda741)

- sessionmaker() produces new database session instances when called.
  
- Base = declarative_base() - This is the base class for ORM models in SQLAlchemy. All database tables/models should inherit from Base.

- get_db() - Dependency Injection for Database Sessions

- yield db → Pauses execution and provides the db session to the caller. Once the caller finishes using db, the function resumes execution and reaches finally: db.close(), ensuring the database session is close

### Entry Point (main.py)

![image](https://github.com/user-attachments/assets/088eeeae-6b1f-4fb5-ab3b-ecd6505db1f7)

- Uses lifespan to load SWIFT codes into the database before requests are processed.

- Creates all required database tables automatically.

- Registers API endpoints via app.include_router(router).

- Ensures a database session is available for data loading.

