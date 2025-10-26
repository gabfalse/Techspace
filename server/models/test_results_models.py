class Test_result :
    def __init__(self, id=None, user_id=None, test_name=None, result_summary=None, score=None, created_at=None ):

        self.id = id,
        self.user_id = user_id
        self.test_name = test_name
        self.result_summary = result_summary
        self.score = score
        self.created_at = created_at
        
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "test_name": self.test_name,
            "result_summary": self.result_summary,
            "score": self.score,
            "created_at": self.created_at,
            

            }