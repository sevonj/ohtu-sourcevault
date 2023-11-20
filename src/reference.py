class Reference:
    def __init__(self, reference_type, **fields):
        self.reference_type = reference_type
        self.fields = fields
    
    def __str__(self):
        op = f"{self.reference_type}:\n"
        for k, v in self.fields.items():
            op += f"{k} = {v}\n"
        return op