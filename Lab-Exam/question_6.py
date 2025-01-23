class VacuumCleaner:
    def __init__(self):
        self.location = "A"
        self.environment = {"A": "Dirty", "B": "Dirty"}

    def clean(self):
        while "Dirty" in self.environment.values():
            if self.environment[self.location] == "Dirty":
                print(f"Cleaning {self.location}")
                self.environment[self.location] = "Clean"
            else:
                print(f"{self.location} is already clean.")
            self.location = "A" if self.location == "B" else "B"
        print("All locations are clean!")

vacuum = VacuumCleaner()
vacuum.clean()
