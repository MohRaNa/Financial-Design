class ConsoleReporter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConsoleReporter, cls).__new__(cls)
            cls._instance.formatting_strategy = None
        return cls._instance

    def set_formatting_strategy(self, formatting_strategy):
        self.formatting_strategy = formatting_strategy

    def display_report(self, content):
        if self.formatting_strategy:
            formatted_content = self.formatting_strategy.format(content)
            lines = formatted_content.split('\n')
            for line in lines:
                print(line)
        else:
            print(content)

# Strategy pattern
class FormattingStrategy:
    def format(self, content):
        pass

class ParenthesesFormatting(FormattingStrategy):
    def format(self, content):
        return f"({content})"

class TabsFormatting(FormattingStrategy):
    def format(self, content):
        return content.replace("\t", "\t\t")


# Singleton pattern
console_reporter = ConsoleReporter()
