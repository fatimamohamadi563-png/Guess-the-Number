import random

def guess_the_number():
    print("سلام! به بازی حدس عدد خوش اومدی 🎮")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("حدست چنده؟ (1 تا 100): ")

        if not guess.isdigit():
            print("لطفاً یه عدد وارد کن!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("عدد بزرگ‌تره!")
        elif guess > number:
            print("عدد کوچک‌تره!")
        else:
            print(f"تبریک! عدد درست بود. تو {attempts} تلاش درست حدس زدی 🎉")
            break

guess_the_number()