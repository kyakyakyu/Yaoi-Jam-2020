# defining characters
# question: display full name/nickname?
define y = Character("Yoah Stillance")
define j = Character("Joschua Crimsonmane")
define v = Character("Veris Silentglow")
define a = Character("Armeria Estielart")
define s = Character("Silas Crimsonmane")
define o = Character("Ohla Pacifica")
define h = Character("Helen")
define n = Character("???")

label start:
    scene black with dissolve(1)
    $ renpy.pause(1)
    
    scene sky bright with dissolve

    "Since long time ago, people associated bright sky with happiness."
    "If the sky was bright, then surely the whole day would be better than another."
    
    scene village green with dissolve

    "Each new day was fulfilled by grace and hope for the small, unknown village."
    "The outside world only knew war and destruction, much to the villagers' belief."
    "In the small village, however, only peace and prosperity could be found."
    "The land still green, the fresh wind of nature still refreshed the breaths of the remaining humans."
    
    show yoah with dissolve
    "And that was the same for the young warrior."

     "Yoah! Helen is here!"
    y "Will be there, Mom!"
    y "Sigh..."

    hide yoah with dissolve
    "The small village yet again had another new blessing coming:"
    "The wedding day of the young man, Yoah Stillance, and his fiancée."
    "It still didn't become his biggest interest, though."
    
    "He looked again at the scrapes of papers that he loved to bring everywhere, full with drawings and notes of beasts and plants."
    "He had always been interested in the unique features of each and every species, even thought he only learnt much from the villagers' tales and the warriors' experience."
    "It was always his dream to wander around the world beyond the small village. Learning how to use his fighting skills, hunting and cooking for himself, and living out in the forest someday..."
    "...and possibly, although unrealistic to human's mind, ending all the bloodshed between humans and nonhumans."
    "Every human was taught that nonhumans were to be killed. At least that was what the empire in the South preached to the villagers."
    "His mark of life's change... probably could never prove what he felt about the nonhumans."
    "...as well as the prolonged war."
    
    show yoah with dissolve
    y "Wouldn't it be much better if I can set free..."
    y "...and meet them?"
    y "..."
    y "There's no time to think about it. I have to go meet her."
    y "My wife-to-be..."
    y "Such a loser I am, huh."
    hide yoah with dissolve

    "His heart beated a little bit faster than he supposed to be."
    "Perhaps the realization of his being an adult hit him a little bit too much."
    "Moreover, an adult without any freedom to own his own life."
    
    "Mom" "There you are."
    h "Yoah!"

    y "Hey."
    h "You're late, you know?"
    y "Well, sorry for that."
    y "Anyways, you look so... beautiful..."
    h "Of course! All brides need to be beautiful on their wedding day, after all."
    "Mom" "Come now, it's going to start."
    y "So I just have to stand there?"
    "Mom" "Yep."
    "Mom" "Don't forget to pray to the Gods, my son."
    "Mom" "It's a blessing day for you."
    y "Thanks, Mom."
    "Mom" "God bless-"

    n "Halt the wedding!"
    y "Huh?"
    h "Now what? After your being late, now this-"
    n "There are beasts just on the village borders! We need to evacuate to a safer place, quick!"

    y "Beasts...?"

    scene village fire with dissolve

    "It was too late."
    "Before the blink of an eye, the village suddenly scattered, covered in huge flame."
    "The wedding decorations was slashed into pieces by the sharp claws..."
    "...of the infamous enemy of humans."
    h "The werewolves, out of all...!"
    h "No! It's only a dream, right?!"

    "It was the first time Yoah felt an engulfing passion deep down from his heart."
    "It was the one and only chance to set things right...!"

    "Mom" "The wedding...!"
    y "The wedding isn't important for now!"
    y "Run away for now, Mom, Helen!"
    h "I can't just leave you here!"
    y "Just go away from this village and listen to me-"
    y "!"

    # flash

    scene black
    h "YOAH!!!"
    $ renpy.pause(1)

    scene village fire with dissolve #adjust the brightness; it should be dark
    y "Ugh..."
    
    show silas silhouette with dissolve
    y "We... do not want to fight..."
    y "...with you... beasts..."
    n "..."
    n "Huh."
    n "Looks like we got The One..."
    y "What...?"

    scene black with Dissolve(3)

    $ renpy.pause(1)
    "The sound of fire faded slowly within the distance."
    "There was nothing on Yoah's sight."
    "It was pitch black."
    "His body felt light, unaware of its whereabouts."

    scene union chamber with Dissolve(3)
    y "Urgh..."
    y "Where... is this...?"

    "Upon the eyes of the young man was a place he never visited."
    "The illuminated huge tank in front of him made him felt inferior."
    "There was a silent air of tension around this place, somehow."
    y "Am I... somewhere around the Empire...?"
    n "No, human."
    y "!"

    "He knew it. He wasn't lonely in the dark room."
    "His vision was now clearer than before, as he saw the crowds surrounding him."
    "How many people were near that tank, staring at him so sharply?"
    "For sure he knew that there was something in that tank."

    show ohla silhouette with dissolve
    "A giant octopus...!"

    n "We need you, human."
    y "Huh...?"
    "It was illogical... The octopus could talk!"
    n "First of all, you are not dreaming, human."
    n "Welcome to the academy of nonhumans, 2/22 Broadborough Academy."
    n "Our home... the creatures that you humans despise."
    y "!"
    "Did he just hear that right?"
    o "My name is Ohla Pacifica. I am trusted to rule this academy."
    o "One of my comrades stumbled across you in your hometown."
    "The octopus probably referred to the werewolves attacking his village."
    o "The villagers are all safe, don't worry."
    y "Thank God..."
    "For sure, the family and friends that he loved were safe."
    o "However, we bring you here for a purpose. A purpose that may also make your dreams come true."
    "His heartbeat raced even faster."
    y "That would be...?"
    
    show ohla with dissolve
    o "To end this war between us humans and nonhumans once and for all."
    o "Please lend us your hand... Umm..."

    hide ohla with dissolve
    "At last..."

    jump new_academy

label new_academy:
    # put more in here hehe
