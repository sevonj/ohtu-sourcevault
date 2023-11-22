class Reference:
    def __init__(self, reference_type, citation_key="", tags=[], **fields):
        self.reference_type = reference_type
        self.citation_key = citation_key
        self.fields = fields
        self.tags = tags
    
    def __str__(self):
        op = f"{self.reference_type}:\n"
        for k, v in self.fields.items():
            op += f"{k} = {v}\n"
        return op