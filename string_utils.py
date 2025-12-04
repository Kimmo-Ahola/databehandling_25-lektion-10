class StringUtils:

    @staticmethod
    def capitalize(text: str) -> str:
        """
        Returns the first letter capitalized.
        Rest of the letters are small

        input: kimmo
        result: Kimmo

        input: KIMMO
        result: Kimmo

        input: Kimmo kristian ahola
        result: Kimmo Kristian Ahola
        """
        if len(text) == 0:
            return text

        split_text = text.split()

        new_string = ""
        for s in split_text:
            first_character = s[0].upper()
            rest_of_characters = s[1::].lower()
            new_string = new_string + first_character + rest_of_characters + " "

        return new_string.strip()
