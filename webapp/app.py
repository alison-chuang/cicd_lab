from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/calculator")
def calculator():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")

    if num1 and num2:
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            return "Invalid input. Please provide valid numbers."

        operation = request.args.get("operation")

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return "Cannot divide by zero."
            result = num1 / num2
        else:
            return "Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."

        return f"The result of {num1} {operation} {num2} is {result}."
    return "Please provide both 'num1' and 'num2' parameters in the query string."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
