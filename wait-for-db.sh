until pg_isready -h "$DB_HOST" -U "$DB_USER"; do
    echo "Waiting for the database to be ready..."
    sleep 2
done

CURRENT_VERSION=$(alembic current | grep -o '[a-f0-9]\{12\}')

LATEST_VERSION=$(alembic heads | grep -o '[a-f0-9]\{12\}')

if [ "$CURRENT_VERSION" == "$LATEST_VERSION" ]; then
    echo "Database updated ($LATEST_VERSION)."
else
    echo "Running migrations..."
    alembic upgrade head
fi

exec python3 main.py