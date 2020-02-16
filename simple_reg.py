#SimpleReg v1.0.0
#By Ratushnyak A.E.

#----Init----#

print("///////////////////////////////////////")
print("//                                   //")
print("//          Simple Register          //")
print("//         By Ratushnyak A.E         //")
print("//                                   //")
print("///////////////////////////////////////")
print("//                                   //")
print("//              Github               //")
print("//                                   //")
print("// github.com/GrozniyMent/SimpleReg  //")
print("//                                   //")
print("///////////////////////////////////////")

#----Script----#

ls = list()

LANG = 0

def chooseLang():
    global LANG
    LANG = input("Please enter your language(UA or EN). Будь ласка оберіть свою мову(UA або EN):")

    if LANG == "UA" or "EN":
        if LANG == "EN":
            LANG = 0
            LANG = int(LANG)
        elif LANG == "UA":
            LANG = 1
            LANG = int(LANG)
    else:
        print("Incorrect language. Неправілна відповідь.")
        chooseLang()

chooseLang()

LANG = int(LANG)

lng = {
    "hlp" : ["Enter append to add new element to your registry",
      "Введіть append для того щоб додати оцінки та їх кількість"],
    "cnt" : ["Enter count of marks:",
             "Введіть кількість оцінок"],
    "mrk" : ["Enter mark:",
             "Введіть оцінку:"]
        }

print(lng["hlp"][LANG])

def writeData():
    count = input(lng["cnt"][LANG])
    count = int(count)

    i = 0
    while i < count:
        mark = input(lng["mrk"][LANG])
        ls.append(mark)
        i = i + 1
    print(ls)

def cmd():
    con = input("mydict@admin ~$ ")
    if con == "append":
        writeData()
    else:
        cmd()

cmd()
