import logging
import json
from collections import Counter
from itertools import permutations, combinations
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/fixedrace', methods=['POST'])
def evaluateFixedRace():
    data = request.get_data(as_text=True)
    logging.info("data sent for evaluation {}".format(data))
    data = data.split(",")
    perm = permutations(data)
    perm1 = []
    for i in perm:
        perm1.append(i)
    if 'Zada Zynda' in data:
        result1 = [k for k in perm1 if k[0] == 'Zada Zynda']
    if 'Fabian Fogel' in data:
        result1 = [k for k in perm1 if k[0] == 'Fabian Fogel']
    if 'Rebekah Regnier' in data:
        result1 = [k for k in perm1 if k[0] == 'Rebekah Regnier']
    if 'Franklin Filippi' in data:
        result1 = [k for k in perm1 if k[0] == 'Franklin Filippi']
    if "Tracie Temblador" in data:
        result1 = [k for k in perm1 if k[0] == 'Tracie Temblador']
    result = random.choice(result1)
    result = ','.join(result)
    logging.info("My result :{}".format(result))
    return json.dumps(result)
