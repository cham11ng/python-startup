# Love Calculator


class LoveCalculate:
    lover_name = "Hello"
    partner_name = "World"

    def __init__(self, lover_name, partner_name):
        self.lover_name = lover_name
        self.partner_name = partner_name

    @staticmethod
    def remove_space(sentence):
        return sentence.replace(" ", "").lower()

    @staticmethod
    def generate_lists(sentence):
        lists = []

        while len(sentence):
            first_letter = sentence[0]
            first_letter_count = sentence.count(first_letter)
            lists.append(first_letter_count)
            sentence = sentence.replace(first_letter, "")

        return lists

    def generate_sentence(self):
        return self.lover_name + ' loves ' + self.partner_name

    def calculate(self):
        sentence = self.generate_sentence()
        computing_sentence = self.remove_space(sentence)

        computing_lists = self.generate_lists(computing_sentence)
        return computing_lists


lover_name = input("Your Name: ")
partner_name = input("Partner Name: ")
love_calculator = LoveCalculate(lover_name, partner_name)
print(love_calculator.calculate())
