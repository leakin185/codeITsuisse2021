import logging
import json
from itertools import permutations, combinations
from flask import request, jsonify
import random

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def evaluateDecoder():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = data["history"][0]["result"]
    num_slots = data["num_slots"]
    possible_values = data["possible_values"]
    output_received = data["history"][0]["output_received"]
    result = [int(i) for i in str(result)]
    rswp = result[0]
    rsrp = result[1]

    if rswp + rsrp == num_slots:
        # no need for combinations
        perm = permutations(output_received)
    elif rswp + rsrp < num_slots:
        comb = combinations(possible_values, num_slots)
        perm = []
        for i in comb:
            perm1 = permutations(output_received)
            for x in perm1:
                perm.append(x)
    perm2 = []
    for i in perm:
        perm2.append(i)

    result1 = random.choice(perm2)
    result = {"answer": result1}

    logging.info("My result :{}".format(result))
    return json.dumps(result)


