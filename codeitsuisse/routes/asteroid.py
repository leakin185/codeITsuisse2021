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

    from collections import Counter

    def pointCount(origin, array, count=1):

        original_count = count

        if origin == 0:
            return count

        left = origin - 1
        right = origin + 1

        while left >= 0 and right < len(array):
            if len(set(array)) <= 1:
                count += len(array) - 1
                left = -1
            elif array[left] == array[origin] and array[right] == array[origin]:
                while right < len(array) and array[right] == array[origin]:
                    count += 1
                    right += 1
                while left != -1 and array[left] == array[origin]:
                    count += 1
                    left -= 1
            else:
                break

        if original_count != 1:
            new_count = count - original_count

            if 7 <= new_count < 10:
                count = new_count * 1.5 + original_count
            elif new_count >= 10:
                count = new_count * 2 + original_count

        else:
            new_count = count
            if 7 <= new_count < 10:
                count = new_count * 1.5
            elif new_count >= 10:
                count = new_count * 2

        if left != -1 and right < len(array):
            if array[left] == array[right]:
                string = array[left + 1:right]
                array = array.replace(string, array[left])
                return pointCount(left + 1, array, count)
            else:
                return count

        else:
            return count

    for i in range(0, len(inputList)):
        result[i]['input'] = inputList[i]
        inp = inputList[i]
        result1 = []
        for x in range(0, len(inp)):
            result1.append(pointCount(x, inp))
        max_score = max(result1)
        origin = result1.index(max_score)
        result[i]['score'] = int(max_score)
        result[i]['origin'] = origin

    logging.info("My result :{}".format(result))
    return json.dumps(result)
