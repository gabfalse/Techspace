class Learning:
    def __init__(self, id=None, title=None, category=None, level='beginner', content=None, video_url=None, thumbnail_url=None):
        self.id = id
        self.title = title
        self.category = category
        self.level = level
        self.content = content 
        self.video_url = video_url
        self.thumbnail_url =  thumbnail_url

    def to_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "level": self.level,
            "content": self.content,
            "video_url": self.video_url,
            "thumbnail_url": self.thumbnail_url,
   }

