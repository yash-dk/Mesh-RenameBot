from .base_db import DataBaseHandle
from ..config import Config
import psycopg2
import json
import os


class UserDB(DataBaseHandle):
    shared_users = {}

    def __init__(self, dburl: str = None):

        if dburl is None:
            dburl = os.environ.get("DB_URI", None)
            if dburl is None:
                dburl = Config.DB_URI

        super().__init__(dburl)
        cur = self.scur()

        table = """CREATE TABLE IF NOT EXISTS ttk_users(
            id SERIAL PRIMARY KEY NOT NULL,
            user_id VARCHAR(50) NOT NULL,
            json_data VARCHAR(1000) NOT NULL, --Keeping it as json so that it flexible to add stuff.
            thumbnail BYTEA DEFAULT NULL,
            is_premium SMALLINT NOT NULL DEFAULT 0,
            tasks_count INTEGER NOT NULL,
            file_choice SMALLINT NOT NULL DEFAULT 0
        )
        """

        """
            SCHEMA DOCS
            id = Uniques id for each entry.
            user_id = Unique ID of the user.
            json_data = If some additional settings required to store.
            thumbnail = Thumbnial will be stored here.
            is_premium = Kept for future.
            tasks_count = How many task has the user submitted till date.
            file_choice = It defines how the files will be uploaded.
                          0 = Upload as the same format as sent.
                          1 = Upload as Document every time.
                          2 = Upload as General Media.
        """

        try:
            # Sometimes multiple instance try to creat which may cause this error
            cur.execute(table)
        except psycopg2.errors.UniqueViolation:  # pylint: disable=no-member
            pass

        self.ccur(cur)

    def get_var(self, var, user_id):
        user_id = str(user_id)
        sql = "SELECT * FROM ttk_users WHERE user_id=%s"

        # search the cache
        user = self.shared_users.get(user_id)

        if user is not None:
            return user.get(var)
        else:
            cur = self.scur(dictcur=True)

            cur.execute(sql, (user_id,))
            if cur.rowcount > 0:
                user = cur.fetchone()
                jdata = user.get("json_data")
                jdata = json.loads(jdata)
                self.shared_users[user_id] = jdata
                return jdata.get(var)
            else:
                return None

            self.ccur(cur)

    def set_var(self, var, value, user_id):
        user_id = str(user_id)
        sql = "SELECT * FROM ttk_users WHERE user_id=%s"

        # search the cache
        cur = self.scur(dictcur=True)

        user = self.shared_users.get(user_id)
        if user is not None:
            self.shared_users[user_id][var] = value

        else:
            cur.execute(sql, (user_id,))
            if cur.rowcount > 0:
                user = cur.fetchone()
                jdata = user.get("json_data")
                jdata = json.loads(jdata)
                jdata[var] = value
                self.shared_users[user_id] = jdata
            else:
                self.shared_users[user_id] = {var: value}

        cur.execute(sql, (user_id,))
        if cur.rowcount > 0:
            insql = "UPDATE ttk_users SET json_data = %s where user_id=%s"
            cur.execute(insql, (json.dumps(self.shared_users.get(user_id)), user_id))

        else:
            insql = "INSERT INTO ttk_users(user_id, json_data) VALUES(%s, %s)"
            cur.execute(insql, (user_id, json.dumps(self.shared_users.get(user_id))))

        self.ccur(cur)

    def get_thumbnail(self, user_id):
        user_id = str(user_id)
        sql = "SELECT * FROM ttk_users WHERE user_id=%s"
        cur = self.scur(dictcur=True)

        cur.execute(sql, (user_id,))
        
        if cur.rowcount > 0:
            row = cur.fetchone()
            self.ccur(cur)
            if row["thumbnail"] is None:
                return False
            else:
                path = os.path.join(os.getcwd(), 'userdata')
                if not os.path.exists(path):
                    os.mkdir(path)
                
                path = os.path.join(path, user_id)
                if not os.path.exists(path):
                    os.mkdir(path)
                
                path = os.path.join(path, "thumbnail.jpg")
                with open(path, "wb") as rfile:
                    rfile.write(row["thumbnail"])
                
                return path
        else:
            return False

    def set_rclone(self, rclonefile, user_id):
        user_id = str(user_id)

        sql = "SELECT * FROM ttk_users WHERE user_id=%s"
        cur = self.scur(dictcur=True)

        cur.execute(sql, (user_id,))
        if cur.rowcount > 0:
            insql = "UPDATE ttk_users SET rclone_file=%s WHERE user_id=%s"
            cur.execute(insql, (rclonefile, user_id))

        else:
            insql = "INSERT INTO ttk_users(user_id, json_data, rclone_file) VALUES(%s, '{}', %s)"
            cur.execute(insql, (user_id, rclonefile))

        self.ccur(cur)
        return True

    def set_thumbnail(self, thumbnail, user_id):
        user_id = str(user_id)

        sql = "SELECT * FROM ttk_users WHERE user_id=%s"
        cur = self.scur(dictcur=True)

        cur.execute(sql, (user_id,))
        if cur.rowcount > 0:
            insql = "UPDATE ttk_users SET thumbnail=%s WHERE user_id=%s"
            cur.execute(insql, (thumbnail, user_id))

        else:
            insql = "INSERT INTO ttk_users(user_id, json_data, thumbnail) VALUES(%s, '{}', %s)"
            cur.execute(insql, (user_id, thumbnail))

        self.ccur(cur)
        return True
