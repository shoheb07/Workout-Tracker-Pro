import sqlite3


def connect():
    conn = sqlite3.connect("workout.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise TEXT,
            sets INTEGER,
            reps INTEGER,
            weight REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bodyweight(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            weight REAL
        )
    """)

    conn.commit()
    conn.close()


def add_workout(exercise, sets, reps, weight):
    conn = sqlite3.connect("workout.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO workouts(exercise, sets, reps, weight) VALUES(?,?,?,?)",
        (exercise, sets, reps, weight)
    )

    conn.commit()
    conn.close()


def view_workouts():
    conn = sqlite3.connect("workout.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM workouts")
    rows = cursor.fetchall()

    conn.close()
    return rows


def delete_workout(workout_id):
    conn = sqlite3.connect("workout.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM workouts WHERE id=?", (workout_id,))

    conn.commit()
    conn.close()


def add_bodyweight(weight):
    conn = sqlite3.connect("workout.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO bodyweight(weight) VALUES(?)",
        (weight,)
    )

    conn.commit()
    conn.close()


def get_bodyweights():
    conn = sqlite3.connect("workout.db")
    cursor = conn.cursor()

    cursor.execute("SELECT weight FROM bodyweight")
    rows = cursor.fetchall()

    conn.close()
    return rows


connect()
