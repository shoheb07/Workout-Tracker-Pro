import csv
import database


def export_csv():
    workouts = database.view_workouts()

    with open("workouts.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Exercise", "Sets", "Reps", "Weight"]
        )

        writer.writerows(workouts)

    print("CSV exported successfully")
