people_images = {}
lst_of_cheers = [
    "לפעמים צריך להגיד לבן אדם את האמת בפנים: אתה אפס",
    "אווץ' זה כאב",
    "לך תנוח, תשתה קפה",
    "אם היית טוב לא היית עושה בוטקאמפ",
    "חוכמה זה לא הצד החזק שלך",
    "לא ברור איך התקבלת לתוכנית",
    "במקרה שלך ספציפית האשמה היא של ורד ומיכל",
    "אם כל טיפש היה עץ הקבוצה הזו הייתה פרדס" "נראה לי שרייכמן גדול עליך",
]
lst_names = [
    "אופירה אסייג",
    "אייל ברקוביץ",
    "איתמר בן גביר",
    "אליהו יוסיאן",
    "אמנון טיטינסקי",
    "בני גנץ",
    "בנימין נתניהו",
    "ברהנו טגניה",
    "ג'ו ביידן",
    "גולדה מאיר",
    "דודי אמסלם",
    "דונלד טראמפ",
    "דני קושמרו",
    "טל ברודי",
    "יאיר לפיד",
    "יוסף שילוח",
    "לוי אשכול",
    "מירי רגב",
    "מני ממטרה",
    "מרב מיכאלי",
    "משה כורסיה",
    "נירו לוי",
    "נפתלי בנט",
    "עמית סגל",
    "רחל אדרי",
    "שמעון פרס",
    "שרה נתניהו",
]
basic_url = r"C:\Users\97252\Documents\בוטקאמפ\botP\ "
basic_url = basic_url.rstrip()
for name in lst_names:
    people_images[name] = basic_url + name + ".jpg"
print(lst_of_cheers)


def hint_0(name: str):
    index = name.find(" ")
    output_str = (
        f"first name: {index} characters, last name: {len(name)- index-1} characters"
    )
    return output_str
