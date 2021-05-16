<div dir="rtl">

<a href="https://t.me/zipperTGbot"><img src="https://telegra.ph/file/f6cfbc3be97f92cd347e6.png" alt="logo icon" width="100" height="100"></a>

# רובוט דחיסת קבצים

רובוט זה מאפשר דחיסה של קבצים ובכך חוסך את הצורך בהורדה, דחיסה והעלאה מחדש.


### איך להריץ?
+ יש לשבט את המאגר עם הפקודה הבאה:
</div>

```
git clone https://github.com/M100achuz2/archive-bot.git
```
<div dir="rtl">
  
  
+ התקינו את [קובץ הדרישות](/requirements.txt) הנלווה:

</div>

```
pip3 install -r requirements.txt
```
<div dir="rtl">
  
+ ערכו את [קובץ התצורה](/config.ini) והכניסו בו את הפרטים הבאים:
</div>

```
[pyrogram]
api_id = 13214253252
api_hash = 342nlkdnvlksnvlsvs3cfcc77
bot_token = 57329872:AAdvnluxdVCbhlhvlsvhesovNUkwvA_MevqJc

[plugins]
root=bot
```
<div dir="rtl">
  
> - את מפתחות ממשק-תכנות-היישומים תוכלו להשיג בכתובת הבאה: [my.telegram.org](https://my.telegram.org)
> - את אסימון הרובוט תוכלו להשיג [מאבא-בוט](https://t.me/BotFather) בטלגרם
+ הריצו את הרובוט:
</div>

```
python3 main.py
```

<div dir="rtl">
  
> - רובוט זה נוצר על ידי [Yehuda-By](https://t.me/M100achuzBots)

</div>
<hr>

### TODO: 

- [ ] upload progress, only with file mor than 100mb. 
 
- [ ] Allow files of up to 50mb to channel subscribers. 

- [ ] zip with password. 

- [ ] extracting files (... even with a password). 

- [ ] Custom name, more than one word. 

