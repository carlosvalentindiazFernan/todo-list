from flask import Blueprint, jsonify, make_response, request
from flask.views import MethodView
from apps.common.response import Serializer

class TodoListView(MethodView):
    """ Todo list View Classs """

    def get(self, *args, **kwargs):
        return Serializer.data({
            'code': 200,
            'message': 'ok'
        })


todo_list_view = TodoListView.as_view('todo_list_view')
