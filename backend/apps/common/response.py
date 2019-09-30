import time
import os
from flask import request, jsonify

class Serializer:
    """ Class to return response data """

    @classmethod
    def data(self,data = {}):
        """
            Return response data
            format :
            {
                "code": "",
                "status: "",
                "message": ""
            }
        """

        code = data['code'] if 'code' in data else 200
        status = 'success' if 200 <= code <= 202 else 'error'
        message = data['message'] if 'message' in data else ''

        info = {
            "code": code,
            "status": status,
            "message": message
        }

        return jsonify(info), code

