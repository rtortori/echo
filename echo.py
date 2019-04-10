from flask import Flask, request, jsonify

# Flask app object
echo = Flask(__name__)


@echo.route('/echo', methods=['POST'])
def reply():
    return jsonify(request.json)


# Run Flask
if __name__ == "__main__":
    echo.run(debug=False, host='0.0.0.0', port=5000, threaded=True)


'''
POST example:
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"namespace":"dummynamespace","vendor":"cisco"}' \
  http://localhost:5000/echo
'''