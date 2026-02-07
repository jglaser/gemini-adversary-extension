import sys

class PhysicsCalculator:
    def __init__(self):
        self.history = []

    def calculate_velocity(self, distance, time):
        """Calculates velocity given distance and time."""
        # VULNERABILITY: No check for division by zero
        print(f"[*] Calculating velocity: d={distance}, t={time}")
        v = distance / time
        self.history.append(v)
        return v

    def get_average_velocity(self):
        """Returns the average of all calculated velocities."""
        # VULNERABILITY: Crashes if history is empty (DivisionByZero)
        print("[*] Calculating average velocity...")
        total = sum(self.history)
        return total / len(self.history)

    def get_last_velocity(self):
        """Returns the most recent calculation."""
        # VULNERABILITY: Crashes if history is empty (IndexError)
        print("[*] Fetching last velocity...")
        return self.history[-1]

    def energy_conversion(self, mass):
        """Calculates E=mc^2."""
        # VULNERABILITY: Allows negative mass (impossible)
        # VULNERABILITY: No type checking
        c = 299792458
        print(f"[*] Converting mass {mass} to energy...")
        return mass * (c ** 2)

if __name__ == "__main__":
    calc = PhysicsCalculator()

    print("--- 💥 VULNERABILITY DEMO STARTING 💥 ---")
    
    # SCENARIO 1: The "Happy Path" (Works fine)
    print("\n1. Running safe calculation...")
    calc.calculate_velocity(100, 10)
    print("   -> Success.")

    # SCENARIO 2: The Crash (Division by Zero)
    # The script should die here, proving the bug exists.
    print("\n2. Running UNSAFE calculation (Time = 0)...")
    try:
        calc.calculate_velocity(50, 0)
    except ZeroDivisionError:
        print("   🔥 CRASH! ZeroDivisionError caught (Expected).")
        print("   (The script would have died here without the try/except block)")

    # SCENARIO 3: The Edge Case (Empty History)
    print("\n3. Running Empty History Average...")
    # We re-initialize to clear history
    empty_calc = PhysicsCalculator()
    try:
        empty_calc.get_average_velocity()
    except ZeroDivisionError:
         print("   🔥 CRASH! Division by zero on empty list (Expected).")

    # SCENARIO 4: The Unhandled Type (String input)
    print("\n4. Running Invalid Type Input...")
    try:
        calc.energy_conversion("heavy")
    except TypeError:
         print("   🔥 CRASH! TypeError caught (Expected).")

    print("\n--- END OF DEMO ---")
    print("Run '/harden' now to fix these crashes!")
