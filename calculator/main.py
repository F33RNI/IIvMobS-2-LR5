from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config


class CalculatorLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class Calculator(App):
    def build(self):
        return CalculatorLayout()


def main() -> None:
    Config.set("graphics", "resizable", 1)
    calculator = Calculator()
    calculator.run()


if __name__ == "__main__":
    main()
