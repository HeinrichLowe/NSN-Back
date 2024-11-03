## Getting Started

1- You need to install the dependencies:

```bash
pip install -r requirements.txt
```

2- Now you need to configure the '.env' file. 

- Just rename the '.env.example' file to '.env' and fill the fields with necessary informations.

3- In this step, you need to choice and configure your database.

- For this project, it used the 'PostgreSQL'.

- After you choice your database, you need to install the 'uuid' extension (if necessary):

```bash
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

- Next you need to use the 'Alembic' to apply the database migrations.

```bash
alembic upgrade head
```

4- Finally, run the server:

```bash
python main.py
```

- Or just press 'F5' and select 'FastAPI' to launch and debug a FastAPI web application.

You can open [http://localhost:8000/ping](http://localhost:8000/ping) to verify if the server started correctly.

## Please note

It is within my knowledge that 'dead code' (commented-out, unnecessary code) exists; it is there solely to guide and assist me with future updates.

However, as the code is updated and that assistance is no longer needed, this 'dead code' will obviously be removed accordingly.

Due to the code refactoring, the tests have become outdated and will need to be updated in the future.

Thank you for your understanding.