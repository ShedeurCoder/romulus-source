import discord
import random
import time
#from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
flags = ["Afghanistan", "Albania","Algeria","Andorra","Angola","Antigua and Barbuda", "Argentina","Armenia","Australia","Austria","Azerbaijan","The Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde", "Cambodia","Cameroon","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo","Costa Rica", "Cote D'Ivoire", "Croatia", "Cuba","Cyprus","Czechia","North Korea","Democratic Republic of the Congo","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Fiji","Finland","France","Gabon","The Gambia", "Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia",'Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan',"Jordan",'Kazakhstan','Kenya','Kiribati','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritania','Mauritius','Mexico','Micronesia','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','North Macedonia','Norway','Oman','Pakistan','Palau','Palestine','Panama',"Papua New Guinea",'Paraguay','Peru','Philippines','Poland','Portugal','Qatar','South Korea','Moldova','Romania','Russia','Rwanda',"Saint Kitts and Nevis",'Saint Lucia','Saint Vincent and the Grenadines','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Sudan','Spain','Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Syria','Tajikistan','Thailand','Timor-Leste','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','Tanzania','United States of America','Uruguay','Uzbekistan','Vanuatu','Venezuela','Vatican City','Vietnam','Yemen','Zambia','Zimbabwe']

gwen = ['1.png', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.png', '9.jpg', '10.jpg', '11.jpg', '12.png', '13.jpg', '14.png', '15.png']

words = ["Ababsbasbibasadadidasdidas","Romulus","CharlieBrown","Dulluh","Chibib","Chiboo","SteveJobless", 'hampter', 'Chicken','Gort','TimCookware', 'Chibroody', 'BigOunce', 'QuandaleDingle', 'Dababy', 'ElChapo', 'Romulus', 'Donkah', 'MangInasal', 'BurgerKing', 'TheChatterbox', 'Chachachombor', 'CarMechanic', 'PatrickBateman', 'Javascript', 'WalterWhite', 'VladimirGwenin', 'JorgenWurtz', 'GwenStacy', 'Bnuuy', 'CharlesDeMarcs', 'NeverGonnaGiveYouUp', 'ChooksToGo', 'KingPin', 'PhantasticGus', 'RahanTrahan', 'Spock', 'LinusTechTips', 'TuriIpIpIp', 'NoCopyrightSounds', 'VisualStudioCode', 'HalfAsInteresting']

hangman = False
countryguesson = False
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.fish'):
        await message.channel.send('<*))><')
    if message.content.startswith('.communism'):
        await message.channel.send('<:communism:882589233792053298>')
    if message.content.startswith('.say '):
        await message.channel.send(message.content[5:])
    if message.content.startswith('T H A N O S'):
        await message.channel.send("T H A N O S")
    if message.content.startswith('.chachacha'):
        await message.channel.send("CHACHACHA")
    if message.content.startswith(".edandem"):
        await message.channel.send("<:em2:901002321947938837><:ed2:901002437492621332> <:edtomato:886971021561835581><:em:888146061875626034> <:edric:892710685392371722><:emira:892710996613922886>")
    if message.content == (".dice"):
        await message.channel.send("Your die rolled " + str(random.randint(1,6)))
    if message.content.startswith(".dice "):
        count = 0
        dice = message.content[6:]
        try:
            dice = int(dice)
        except:
            await message.channel.send("Please input an integer from 1 to 100")
            return
        if dice > 100 or dice < 1:
            await message.channel.send("Please input a number from 1 to 100")
            return
        while dice > 0:
            num = random.randint(1, 6)
            count = count + num
            dice = dice - 1
        await message.channel.send("Your dice rolled a total of " + str(count))
    if message.content.startswith(".steve"):
        yesno = random.randint(0,1)
        if yesno == 0:
            await message.channel.send("Yes")
            return
        await message.channel.send("No")
    if message.content == ".timer":
        await message.channel.send("Please specify the number of seconds")
    if message.content.startswith(".timer "):
        seconds = message.content[7:]
        try:
            seconds = int(seconds)
        except:
            await message.channel.send("Please input an integer with no decimal places")
            return
        s = await message.channel.send(seconds)
        while seconds > 0:
            time.sleep(1)
            seconds = seconds - 1
            await s.edit(content=seconds)
        await s.edit(content="TIMER FINISHED")
    if message.content.startswith(".help"):
        await message.channel.send("# COMMAND LIST\n\n**.help** - *Shows this message*\n**.chachacha** - *Chachacha your way into heaven* \n**.fish** - *fish go blub blub*\n**.communism** - *SHOWS NO ONE'S FAVORITE IDEOLOGY*\n**.say** - *Says anything you want it to say* \n**.edandem** - *Best characters ever* \n**.gwen** - *my love* \n**.dice** (dice number) - *Rolls a number of dice specified* \n**.steve** - *Yes or No answered by STEVE*\n**.timer** (seconds) - *Timer for seconds specified*\n**.hangman** - *Do da hangman*\n**.country** - *Guess da countryflag*\n**THATS ALL THE COMMANDS FOR ROMULUS**")

    if message.content.lower().startswith('.gwen'):
        gwenPic = gwen[random.randint(0, len(gwen) - 1)]
        await message.channel.send(file=discord.File("gwen/" + gwenPic))

    #MAKE THE HANGMAN
    if message.content.startswith(".hangman"):
        global userhangman
        userhangman = message.author.id
        global hangmantries
        hangmantries = 15
        global hangmanLetters
        hangmanLetters = []
        #pick a word
        global word
        word = words[random.randint(0,len(words) - 1)]
        global tempword
        tempword = ""
        for char in word:
            tempword = tempword + "—"
        await message.channel.send(tempword)
        global hangman
        hangman = True

    if hangman == True and len(message.content) == 1:
        if userhangman == message.author.id:
            if hangmantries > 0:
                hangmanLetters.append(message.content.lower())
                letters = ''
                for letter in hangmanLetters:
                    if len(letters) == 0: 
                        letters = '**' + letter + '**'
                        continue
                    letters = letters + ', **' + letter + '**'
                global charnumber
                charnumber = 0


                prevtemp = tempword

                for char in word:
                    if message.content.lower() == char.lower():
                        tempword = tempword[:charnumber] + word[charnumber] + tempword[charnumber + 1:]
                    charnumber = charnumber + 1
                if tempword == prevtemp:
                    hangmantries = hangmantries - 1
                
                await message.channel.send(tempword + "\nYou have " + str(hangmantries).lower() + " tries left.\nAttempted letters: " + letters)

                if tempword == word:
                    await message.channel.send("Congratulations! You solved it")
                    hangman = False
            else:
                await message.channel.send("No tries left! You lost.")
                hangman = False
        else:
            return

    #MAKE DA COUNTRY
    if message.content.startswith(".country"):
        global userflags
        userflags = message.author.id
        global country
        country = flags[random.randint(0, len(flags) - 1)]
        global flagsinarow
        flagsinarow = 0
        global countryfile
        countryfile = country.replace(" ", "")
        await message.channel.send(file=discord.File("flags/" + countryfile + ".png"))
        global countryguesson
        countryguesson = True
        return
    if countryguesson == True:
        if message.author.id == userflags:
            if message.content.lower() == country.lower():
                flagsinarow = flagsinarow + 1
                country = flags[random.randint(0, len(flags))]
                countryfile = country.replace(" ", "")
                await message.channel.send(file=discord.File("flags/" + countryfile + ".png"))
            else:
                await message.channel.send("Wrong, it was **" + country + "**. You got " + str(flagsinarow) + " flags in a row.")
                countryguesson = False 
        else:
            return

#keep_alive()
client.run('***')
