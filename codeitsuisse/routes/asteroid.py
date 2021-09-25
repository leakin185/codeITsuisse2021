import logging
import json
from collections import Counter

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluateAsteroid():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputList = data.get("test_cases")
    result = [dict() for number in range(len(inputList))]
    for i in range(0, len(inputList)):
        result[i]['input'] = inputList[i]
        inp = inputList[i]
        result1 = []
        for x in range(0, len(inp)):
            result1.append(pointCount(x, inp))
        max_score = max(result1)
        origin = result1.index(max_score)
        result[i]['origin'] = origin
        result[i]['score'] = max_score

    logging.info("My result :{}".format(result))
    return json.dumps(result)



