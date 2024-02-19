from flask import Flask

app = Flask(__name__)


LANG_TO_NUMBER_FUNC = {
    'roman': 'convert_from_roman',
    'hindi': 'convert_from_hindi'
}


ROMAN_VALUE_MAP = {
    'I': 1,
    'V': 5,
    'X': 10,
}


class Conversion:
    def convert_from_roman(self, value):
        total_value = 0
        prev_value = 0

        for val in reversed(value):
            current_value = ROMAN_VALUE_MAP.get(val)
            if current_value < prev_value:
                total_value -= current_value
            else:
                total_value += current_value
            prev_value = current_value

        return total_value


conversion = Conversion()


@app.route("/")
def index():
    return "<p>Go to /number/:value</p>"


@app.route("/number/<value>")
def convert_to_integer(value):
    data = {
        'original': 'roman',
        'value': value
    }
    conversion_func = getattr(conversion, LANG_TO_NUMBER_FUNC.get(data['original']))
    output = conversion_func(data['value'])
    return {
        'value': data['value'],
        'output': output
    }


if __name__ == '__main__':
    app.run(debug=True)
