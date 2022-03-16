from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self,input):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, input)
            except StepException:
                break
