class Program:
    def __init__(self, id=None, title=None, description=None, start_date=None, end_date=None, status="upcoming", banner_url=None, created_at=None):
        self.id = id
        self.title = title
        self.descrption = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.banner_url = banner_url
        self.created_at = created_at

    def to_dict(self):
        """Ubah objek user jadi dictionary (berguna untuk response JSON)"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status,
            "banner_url": self.banner_url,
            "created_at": self.created_at
            }