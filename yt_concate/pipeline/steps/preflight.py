from .step import Step

class Preflight(step):
    def process(self, data, inputs, utils):
        utils.create_dir()