class TestShortPhrase:

    def test_short_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"This is not a short phrase, must be less than 15"