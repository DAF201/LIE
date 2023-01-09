class priority:
    def __init__(self, task_priority, **kwargs) -> None:
        self.task_priority = task_priority
        if kwargs != {}:
            self.start_with_in = kwargs['start_with_in']
            self.kwargs = kwargs.pop('start_with_in')
        else:
            self.start_with_in = 0

    def __call__(self):
        return self.task_priority
