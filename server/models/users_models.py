# models/user.py

class User:
    def __init__(self, id=None, username=None, email=None, password_hash=None,
                 full_name=None, bio=None, role='member', position='developer',
                 profile_url=None, github_link=None, linkedin_link=None,
                 portfolio_link=None, created_at=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.full_name = full_name
        self.bio = bio
        self.role = role
        self.position = position
        self.profile_url = profile_url
        self.github_link = github_link
        self.linkedin_link = linkedin_link
        self.portfolio_link = portfolio_link
        self.created_at = created_at

    def to_dict(self):
        """Ubah objek user jadi dictionary (berguna untuk response JSON)"""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "bio": self.bio,
            "role": self.role,
            "position": self.position,
            "profile_url": self.profile_url,
            "github_link": self.github_link,
            "linkedin_link": self.linkedin_link,
            "portfolio_link": self.portfolio_link,
            "created_at": self.created_at,
        }
