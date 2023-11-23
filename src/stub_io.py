class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def read_input(self, text):
        return self.inputs.pop(0)

    def write_output(self, text):
        self.outputs.append(text)