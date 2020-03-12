import time

def create_plan_anim():
    print("Creating Diet Plan", end="", flush=True)
    time.sleep(.3)
    for i in range(3):
        print(". ", end="", flush=True)
        time.sleep(.5)
    print("\nDone!")

def progress_bar():
    for i in range(3):
        print(". ", end="", flush=True)
        time.sleep(.15)
    print("")

if __name__ == "__main__":
    create_plan_anim()
    progress_bar()