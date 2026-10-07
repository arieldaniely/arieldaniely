# הפעלת דירוג הכולל מאגרים פרטיים

המנגנון משתמש ב־GitHub Readme Stats Action ומייצר כרטיס בהיר וכהה בתוך המאגר. הקוד הפרטי ושמות המאגרים אינם מוצגים בכרטיס; רק נתונים מצטברים.

## הגדרה חד־פעמית

1. צור [Personal Access Token מסוג classic](https://github.com/settings/tokens/new) עם הרשאות `repo` ו־`read:user`, כפי שנדרש בתיעוד כלי הדירוג. בחר תוקף מתאים. אם חלק מהמאגרים נמצאים בארגון הדורש SSO, יש לאשר את ההרשאה גם מול הארגון.
2. הוסף אותו כ־Repository secret בשם `PROFILE_STATS_TOKEN` תחת [Settings → Secrets and variables → Actions](https://github.com/arieldaniely/arieldaniely/settings/secrets/actions). אין לשמור אותו בקוד או לשלוח אותו בצ׳אט.
3. פתח [Actions](https://github.com/arieldaniely/arieldaniely/actions), בחר **Update private GitHub stats** ולחץ **Run workflow** על הענף `main`.

לאחר הרצה מוצלחת ה־README יעבור אוטומטית לכרטיסים החדשים. בהמשך העדכון יתבצע פעם ביום. אם ההרשאה חסרה, המנגנון יציג הודעה בריצה ולא יפרסם כרטיס שגוי. אם משיכת הנתונים נכשלת, הכרטיס הקודם יישמר.

הדירוג נשאר דירוג של ספריית הכרטיסים, ולא דירוג רשמי של GitHub. נשמרה הגדרת `include_all_commits=false`: מונה הקומיטים מתייחס לתקופת התרומות של GitHub, ולא לכל ההיסטוריה. הגישה למאגרים פרטיים נקבעת לפי ההרשאה; אין פרמטר URL שמחליף אותה.

## מקורות

- [תיעוד ה־Action וההרשאות למאגרים פרטיים](https://github.com/stats-organization/github-readme-stats-action#inputs)
- [הוראות התקנה והרשאות](https://github.com/stats-organization/github-stats-extended/blob/master/apps/frontend/src/content/docs/docs/deploy.md)
- [אפשרויות כרטיס הדירוג](https://github.com/stats-organization/github-stats-extended/blob/master/apps/frontend/src/content/docs/docs/cards/stats.md)
