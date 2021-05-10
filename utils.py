from pony.orm import *
from pyrogram.types import Message
from os import listdir

# ========= DB build =========
db = Database()


class User(db.Entity):
    uid = PrimaryKey(int, auto=True)
    status = Required(int)  # status-user: "INSERT"/"NOT-INSERT"


db.bind(provider='sqlite', filename='zipbot.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# ========= helping func =========
def dir_work(uid: int) -> str:
    """ static-user folder """
    return f"static/{uid}/"


def zip_work(uid: int) -> str:
    """ zip-archive file """
    return f'static/{uid}.zip'


def list_dir(uid: int) -> list:
    """ items in static-user folder """
    return listdir(dir_work(uid))


def up_progress(current, total, msg: Message):
    """ edit status-msg with progress of the uploading """
    msg.edit(f"**התקדמות ההעלאה: {current * 100 / total:.1f}%**")


# ========= MSG class =========
class Msg:

    def start(msg: Message) -> str:
        """ return start-message text """
        txt = f"[‏](https://github.com/M100achuz2/archive-bot.git)היי {msg.from_user.mention}!\n" \
              "באמצעות בוט זה תוכלו לדחוס קבצים לארכיון. שלחו /zip, ופעלו על פי ההוראות." \
              "\n\nרובוט זה נוצר על ידי [Yeuda-By](t.me/m100achuzBots) מצוות [רובוטריק](t.me/robottrick)." \
              "\nלקוד המקור [לחצו כאן](https://github.com/M100achuz2/archive-bot)."
        return txt

    zip = "שלחו את הקבצים שהנכם רוצים לדחוס, ובסיום שלחו /stopzip לאחר שכל הקבצים ירדו. \n`הבוט תומך בקבצים עד 20mb, " \
          "ועד 20 קבצים לארכיון אחד.` "
    too_big = "הקובץ גדול מידי ):"
    too_much = "ניתן לדחוס עד 20 קבצים בלבד."
    send_zip = "השתמשו בפקודת /zip בשביל לדחוס קבצים (:"
    zipping = "מתחיל בדחיסת {} קבצים..."
    uploading = "מעלה ארכיון..."
    unknow_error = "התרחשה שגיאה לא ידועה. \nשים לב לסדר הפעולות, ניתן להתחיל מחדש על ידי שליחת /start. \nבדוק אם " \
                   "שלחת קבצים לדחיסה, ואם חיכית שכולם ירדו. \nבבקשה שלח זה למפתח:\n ```{}``` "
    downloading = "מוריד קובץ:"
    zero_files = "לא נשלחו קבצים."
