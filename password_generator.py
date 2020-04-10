# This program generatesa random password for the user
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
        self.run_generator()

    def run_generator(self):
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
        """ This requests how many letters should be in the password """
        try:
            self.how_letters = int(input("How many letters do you want in it? "))
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

    # def generate(self):
    def generate(self):
        """ This generates the pass word """
        how_long = self.how_long
        how_letters = self.how_letters
        how_numbers = how_long - how_letters
        password_draft = []
        while how_long > 0:
            while how_numbers > 0:
                num_pick = randint(0, 9)
                password_draft.append(str(num_pick))
                how_numbers -= 1
            while how_letters > 0:
                letter_pick = choice(self.alphabets)
                password_draft.append(letter_pick)
                how_letters -= 1
            how_long -= 1

        print(f"This is the password draft => {password_draft}")
        password = ""
        while len(password_draft) > 0:
            n = choice(password_draft)
            password += n
            password_draft.remove(n)
        print(f"This is the final password => {password}")


if __name__ == "__main__":
    passgen = PasswordGenerator()
