from pyrogram.types import Message
from os import listdir


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


def down_progress(current, total, msg: Message):
    """ edit status-msg with progress of the downloading """
    msg.edit(f"**התקדמות ההורדה: {current * 100 / total:.1f}%**")


class Msg:

    def start(msg: Message) -> str:
        """ return start-message text """
        txt = f"היי {msg.from_user.mention}!\n"
        txt += "באמצעות בוט זה תוכלו לדחוס קבצים לארכיון. שלחו /zip, ופעלו על פי ההוראות."
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
