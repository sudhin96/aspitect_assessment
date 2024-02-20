from flask import Flask, request
app = Flask(__name__)

@app.route('/api/v1/factorial', methods=['POST'])
def factorial():
    data = request.get_json()
    if "value" not in data.keys():
        return {"error": "value key missing"}
    if not isinstance(data.get("value"), int):
        return {"error": "value key not an integer"}
    return {"factorial": find_factorial(data.get("value"))}


def find_factorial(value):
    if value == 0:
        return 1
    return value * find_factorial(value - 1)


if __name__ == "__main__":
    app.run()
