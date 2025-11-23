#student academic productivity tracker Bot
def add_study():
    date = input("Date (DD-MM-YYYY):")
    subject = input("Subject:")
    hours = input("Hours studied:")

    with open("study.txt","a")as f:
        f.write(f"{date},{subject},{hours}\n")

    print("Study log saved!\n")


def add_taskdone():
    task = input("Enter task done:")
    with open("task.txt","a") as f:
        f.write(task + "\n")
    print("Task saved!\n")


def view_score():
    total_hours = 0
    total_task = 0
    
    try:
        with open("study.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                total_hours += float(parts[2])
    except:
        pass
    try:
        with open("task.txt","r") as f:
            for line in f:
                if line.strip()!="":
                    total_task += 1
    except:
        pass

    score = (total_hours * 10) + (total_task* 20)

    print(f"\nHours: {total_hours}")
    print(f"Taskdone: {total_task}")
    print(f"Productivity Score: {score}\n")

def main():
    while True:
        print("1. Add Study Entry")
        print("2. Add Taskdone")
        print("3. View productivity score")
        print("4. Exit")

        ch = input("choose:")
        if ch == "1":
            add_study()
        elif ch == "2":
            add_taskdone()
        elif ch == "3":
            view_score()
        elif ch == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid!\n")


main()