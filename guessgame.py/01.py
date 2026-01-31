import random

LOW, HIGH = 1, 100
secret = random.randint(LOW, HIGH)
previous_distance = None

print(f"🎯 I picked a number between {LOW} and {HIGH}.")
print("Hot = closer than before | Cold = farther than before")

while True:
    try:
        guess = int(input("Your guess: "))

        if guess < LOW or guess > HIGH:
            print(f"⚠️ Enter a number between {LOW} and {HIGH}.")
            continue

        distance = abs(secret - guess)

        if distance == 0:
            print("🎉 Correct! You nailed it.")
            break

        if previous_distance is None:
            if distance <= 10:
                print("🔥 Hot")
            else:
                print("❄️ Cold")
        else:
            if distance < previous_distance:
                print("🔥 Hotter")
            else:
                print("❄️ Colder")

        previous_distance = distance

    except ValueError:
        print("❌ Invalid input. Enter an integer.")


