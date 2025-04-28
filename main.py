import random

class vythea:
    """
    vythea — /ˈvī-thē-ə/
    a relentless force of creation and precision; one who shapes the world with vision, structure, and unyielding execution.
    """

    def __init__(self):
        self.contacts = [
            'discord: vythea',
            'telegram: t.me/vythea'
        ]

        self.languages = [
            'python',
            'sql',
            'javascript'
        ]

        self.learning = [
            'javascript',
            'golang'
        ]

        self.tools = [
            'git',
            'excel',
            'figma',
            'postgreSQL',
            'vs code'
        ]

        self.libraries = [
            'numpy',
            'pandas',
            'matpotlib',
            'seaborn',
            'scikit-learn',
            'streamlit',
            'yfinance'
        ]

    def summon(self):
        print(f"contact: {random.choice(self.contacts)}")

        print("\nlanguages:")
        for lang in self.languages:
            print(f"- {lang}")

        print("\ncurrently learning:")
        for skill in self.learning:
            print(f"- {skill}")

        print("\ntools & platforms:")
        for tool in self.tools:
            print(f"- {tool}")

        print("\nlibraries & frameworks:")
        for lib in self.libraries:
            print(f"- {lib}")

if __name__ == "__main__":
    khaleed = vy()
    khaleed.summon()
