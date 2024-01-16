# Создание переменных и присваивание им музыкальных композиций
define audio.normal = "audio/New-Composition-12.ogg"
define audio.death = "audio/New-Composition-17.ogg"

# Изменение курсора для игры
define config.mouse = {}

define config.mouse["default"] = [ ("gui/cursors/attackontitan.cur", 0,0) ]

# Определение персонажей игры
define p = Character('Петен', color="#1e90ff", image = "peten")
define g = Character('Хитлер', color="#696969", image = "hitler")
define h = Character('Гимлер', color="#969696", image = "himmler")

# Создание переменных отвечающих за расположение персонаей
init:
    $ leftPeten = Position(xalign = 0.1, yalign = 1.0)
    $ rightHitler = Position(xalign = 0.9, yalign = 1.0)

# Начало игры(улица):
label start:

    stop music fadeout 0.5

    play music normal

    scene bg train carriage

    "Встреча между главой маршалом Петеном и Гитлером в Монтуаре в октябре 1940 года явилась одним из ключевых событий французской истории времен Второй мировой войны. Гитлер намеревался склонить Францию к войне против Великобритании. Петен, напротив, стремился всеми силами избежать этого. Встреча в Монтуаре совпала с тайной миссией профессора Ружье в Лондон. Эмиссар Петена сообщил британскому руководству об обязательствах Франции не воевать со своим вчерашним союзником. Эти обязательства маршал Петен выполнил. Гитлеру не удалось втянуть Францию с ее сильным флотом в войну на стороне нацистской Германии."

    show peten hat normal at leftPeten
    with easeinleft

    p "Где этот чертов бош?"

    show hitler normal at rightHitler
    with easeinright

    g "Guten Tag mein lieber! Я только вернулся из Испании, где у меня была далеко не простая беседа с нашим общим знакомым, Генералом Франко, так что давайте подпишем вашу капитуляцию как можно быстрее."

    p "Для начала, нам следует обсудить ее условия."

    g "Ja ja, конечно. Давайте перейдем в вагон, где не так давно вы принудили мою страну на унизительный мир, а теперь сами подпишите его."

    p hat sad "Это мы еще посмотрим."

    # Меню выбора ответа:
    menu:
        "Это мы еще посмотрим."

        "Убить Хитлера":
            jump kill

        "Пойти в вагон":
            hide peten hat sad with moveoutleft
            hide hitler normal with easeoutleft

            jump trainCarriage

    return

# Попытка убийства:
label kill:

    play music death

    show hitler normal at rightHitler

    g "Ha! Наивный французишка. Великого фюрера так просто не убить. Если ты не готов подписать капитуляцию, я найду другого. Арестовать его!"

    hide peten hat sad with moveoutleft
    hide hitler normal with easeoutleft

    jump theEndingOne

    return

# Переход в вагон:
label trainCarriage:

    scene bg train carriage is inside
    with fade

    show peten serious at leftPeten
    with dissolve

    show hitler normal at rightHitler
    with dissolve

    p "И так, я ..."

    g "Ruhig, спокойно. Здесь я буду диктовать условия!"

    show peten evil

    g "Erstens, во первых, давайте обсудим экономическое сотрудничество. Ваши заводы будут работать на благо германии, они будут выпускать необходимые нам вещи, а ресурсами в ваших колониях теперь будем распоряжаться мы."

    menu:
        "Заводы франции будут работать на благо германии, а колониальными ресурсами теперь будем распоряжаться немцы."

        "Согласиться":
            p "Думаю у меня нет иного выбора кроме как согласиться."

            g "Wunderbar, замечательно!"

            jump agreeFirstRequirement

        "Не согласиться требованием":
            p "К сожалению, но я не могу согласиться. Как главе государства мне нужно позаботься чтобы мои граждани было обеспечаны всем необходимым."

            g "Verdammt, проклятый. Обсудим этот пункт позже."

            jump disagreeWithFirstRequirement

    return

# Не согласиться с первым требованием:
label disagreeWithFirstRequirement:

    return

# Согласиться с первым требованием:
label agreeFirstRequirement:

    return

# Не согласиться со вторым требованием:
label disagreeWithSecondRequirement:

    return

# Согласиться со вторым требованием:
label agreeSecondRequirement:

    return

# Не согласиться со вторым требованием:
label disagreeWithThirdRequirement:

    return

# Согласиться с первым требованием:
label agreeThirdRequirement:

    return

# Нахамить Гимлеру:
label toBeRudeHimmler:

    return

# Отстоять позицию:
label toDefendThePosition:

    return

# Прогнуться:
label bendOver:

    return

# Спорить №1:
label argue:

    return

# Спорить №2:
label argueSecondOption:

    return

# Концовка №1:
label theEndingOne:

    "После неудачного покушения на Хитлера, Филипп Петен был приговорен к расстрелу, а его место занял Пьер Лаваль, которому не удалось отстоять свободную францию хоть в каком то виде из-за чего третий по численности флот мира был почти полностью конфискован Третьим Рейхом, а сама Франция была полностью оккупирована."

    return

# Концовка №2:
label theEndingTwo:

    return

# Концовка №3:
label theEndingThree:

    return

# Концовка №4:
label theEndingFour:

    return