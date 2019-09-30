from .views import todo_list_view

def todo_list_router(app):
    app.add_url_rule(
        '/api/v1/list',
        view_func=todo_list_view)