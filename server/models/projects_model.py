class Project:
    def __init__(self, id=None,owner_id=None,title=None, description=None, visibility="public", tech_stack=None, repo_link=None,live_demo=None,thumbnail_link=None, created_at=None):

        self.id = id
        self.title = title
        self.description = description
        self.owner_id = owner_id
        self.visibility = visibility
        self.tech_stack = tech_stack
        self.repo_link = repo_link
        self.live_demo = live_demo
        self.thumbnail_link = thumbnail_link
        self.created_at = created_at
    
    def to_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "descrition": self.description,
            "owner_id": self.owner_id,
            "visibility": self.visibility,
            "tech_stack": self.tech_stack,
            "repo_link": self.repo_link,
            "live_demo": self.live_demo,
            "thumbnail_link": self.thumbnail_link,
            "created_at": self.created_at,
        }
     
        