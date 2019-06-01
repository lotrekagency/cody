from huey.contrib.djhuey import db_task


@db_task()
def task_execute_action(project, actions):

    for action in actions:
        print (action.endpoint)
