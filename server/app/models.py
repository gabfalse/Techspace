from config import get_db_connection

class UserModel:
    @staticmethod
    def create(data):
        conn = get_db_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                    INSERT INTO users (
                        username, email, password_hash, full_name, bio, 
                        role, position, profile_url, github_link, 
                        linkedin_link, portfolio_link
                    ) VALUES (
                        %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, 
                        %s, %s
                    )
                """
                
                params = (
                    data['username'], 
                    data['email'], 
                    data['password_hash'], 
                    data.get('full_name'), 
                    data.get('bio'),
                    data.get('role', 'member'), 
                    data.get('position', 'developer'), 
                    data.get('profile_url'),
                    data.get('github_link'),
                    data.get('linkedin_link'),
                    data.get('portfolio_link')
                )

                cursor.execute(sql, params)
                conn.commit()
                return cursor.lastrowid
        finally:
            conn.close()
    
    @staticmethod
    def get_all():
        conn = get_db_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM users"
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def get_by_id(user_id):
        conn = get_db_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM users WHERE id = %s"
                cursor.execute(sql, (user_id,))
                return cursor.fetchone()
        finally:
            conn.close()

    @staticmethod
    def update(user_id, data):
        conn = get_db_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                    UPDATE users SET 
                        username=%s, 
                        email=%s, 
                        full_name=%s, 
                        bio=%s, 
                        role=%s, 
                        position=%s, 
                        profile_url=%s, 
                        github_link=%s, 
                        linkedin_link=%s, 
                        portfolio_link=%s
                    WHERE id=%s
                """
                
                params = (
                    data['username'],
                    data['email'],
                    data.get('full_name'),
                    data.get('bio'),
                    data.get('role'),
                    data.get('position'),
                    data.get('profile_url'),
                    data.get('github_link'),
                    data.get('linkedin_link'),
                    data.get('portfolio_link'),
                    user_id
                )

                cursor.execute(sql, params)
                conn.commit()
                return cursor.rowcount
        finally:
            conn.close()

    @staticmethod
    def delete(user_id):
        conn = get_db_connection()
        try:
            with conn.cursor() as cursor:
                sql = "DELETE FROM users WHERE id=%s"
                cursor.execute(sql, (user_id,))
                conn.commit()
                return cursor.rowcount
        finally:
            conn.close()