import time

def speed_typing_test(text):
    print("Type the following text:")
    print(text)
    input("Press Enter when you are ready...")

    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    user_input = user_input.strip()
    correct_chars = sum(1 for i in range(min(len(text), len(user_input))) if text[i] == user_input[i])
    accuracy = (correct_chars / len(text)) * 100
    time_taken = end_time - start_time
    speed = len(user_input) / time_taken * 60

    print("\nYour typing accuracy: {:.2f}%".format(accuracy))
    print("Time taken: {:.2f} seconds".format(time_taken))
    print("Typing speed: {:.2f} characters per minute".format(speed))

if __name__ == "__main__":
    test_text = "The quick brown fox jumps over the lazy dog."
    speed_typing_test(test_text)

