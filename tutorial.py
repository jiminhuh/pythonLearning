lunch = "pie"

print(lunch + " is good!")

if lunch == "pie":
    print("You brought pie today? Nice!")
else:
    print("Why didn't you bring pie?!")


words = ["hello", "my", "name", "is", "Jimin"]

for word in words:
    print(word, len(word))

age_question = input("How old are you?")


if int(age_question) >= 0:
    print("Wow, you are", age_question, "years old!")

