# This program generates a random password for the user
from random import choice, randint


class PasswordGenerator:
    """ Overall class to manage the password generator """

    def __init__(self):
        """ Initiialize the PasswordGenerator class """
        self.alphabets = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        self.request_pass_length()
        self.request_amt_letters()
        self.generate()

    def request_pass_length(self):
        """ This requests how long the password should be """
        try:
            self.how_long = int(
                input(
                    "How long do you want the password to be? \nPassword must be a minimum of 6 characters and must include at least a number "
                )
            )

            if self.how_long < 6:
                print("\nSorry password must be a minimum of 6 characters.")
                self.request_pass_length()
            else:
                pass
        except ValueError:
            print("You can only input a digit!")
            self.run_generator()

    def request_amt_letters(self):
        """ This requests how many letters should be in the Password """
        try:
            self.how_letters = int(
                input("How many letters do you want in the password? ")
            )
            if self.how_letters >= self.how_long:
                print(
                    f"\nSorry letters must be a minimum of {self.how_long - 1} characters."
                )
                self.request_amt_letters()
            else:
                pass
        except ValueError:
            print("You can only input a digit!")
            self.request_amt_letters()

    def generate(self):
        """ This generates the password """
        how_long = self.how_long
        how_letters = self.how_letters
        how_numbers = how_long - how_letters
        password_draft = []
        letter_pick_list = []
        while how_long > 0:

            while how_numbers > 0:
                num_pick = randint(0, 9)
                password_draft.append(str(num_pick))
                how_numbers -= 1

            while how_letters > 0:
                letter_pick = choice(self.alphabets)

                # this places the random letters in a list to be capitalized or not
                letter_pick_list.append(letter_pick)
                how_letters -= 1
            # this are the lists for the uppercased and lowercased letters
            upper_letters = letter_pick_list[::2]
            lower_letters = letter_pick_list[1::2]

            how_long -= 1

        # This appends the lowercase and uppercase letters to the password draft list to be randomized
        for letter in upper_letters:
            password_draft.append(letter.upper())
        for letter in lower_letters:
            password_draft.append(letter.lower())

        print(f"This is the password draft => {password_draft}")
        password = ""

        # the password characters are randomized in this code
        while len(password_draft) > 0:
            n = choice(password_draft)
            password += n
            password_draft.remove(n)

        print(f"This is the final password => {password}")


if __name__ == "__main__":
    passgen = PasswordGenerator()
