from tkinter import *
from tkinter import messagebox
import database

window = Tk()
window.title("Workout Tracker Pro")
window.geometry("700x500")


def add_workout():
    if exercise_entry.get() == "":
        messagebox.showerror("Error", "Enter exercise name")
        return

    database.add_workout(
        exercise_entry.get(),
        int(sets_entry.get()),
        int(reps_entry.get()),
        float(weight_entry.get())
    )

    messagebox.showinfo("Success", "Workout Added")
    display_workouts()


def display_workouts():
    workout_list.delete(0, END)

    rows = database.view_workouts()

    for row in rows:
        workout_list.insert(
            END,
            f"{row[0]} | {row[1]} | Sets:{row[2]} | Reps:{row[3]} | Weight:{row[4]} kg"
        )


def delete_selected():
    selected = workout_list.get(ACTIVE)

    if selected:
        workout_id = int(selected.split("|")[0])
        database.delete_workout(workout_id)
        display_workouts()


Label(window, text="Exercise").pack()
exercise_entry = Entry(window, width=30)
exercise_entry.pack()

Label(window, text="Sets").pack()
sets_entry = Entry(window)
sets_entry.pack()

Label(window, text="Reps").pack()
reps_entry = Entry(window)
reps_entry.pack()

Label(window, text="Weight (kg)").pack()
weight_entry = Entry(window)
weight_entry.pack()

Button(window, text="Add Workout", command=add_workout).pack(pady=5)

Button(window, text="Delete Selected", command=delete_selected).pack(pady=5)

workout_list = Listbox(window, width=70, height=15)
workout_list.pack()

display_workouts()

window.mainloop()
