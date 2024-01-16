# Создание переменных и присваивание им музыкальных композиций
define audio.normal = "audio/New-Composition-12.ogg"
define audio.death = "audio/New-Composition-17.ogg"

# Изменение курсора для игры
define config.mouse = {}

define config.mouse["default"] = [ ("gui/cursors/attackontitan.cur", 0,0) ]

# Определение персонажей игры
define p = Character('Петен', color="#1E90FF", image = "peten")
define g = Character('Хитлер', color="#696969", image = "hitler")

# Создание переменных отвечающих за расположение персонаей
init:
    $ leftPeten = Position(xalign = 0.1, yalign = 1.0)
    $ rightHitler = Position(xalign = 0.9, yalign = 1.0)

# Начало игры:
label start:

    stop music fadeout 0.5

    play music normal

    scene bg train carriage

    "lorem"

    show peten hat normal at leftPeten
    with easeinleft

    p "Вы создали новую игру Ren'Py."

    show hitler normal at rightHitler
    with easeinright

    g "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    p hat sad "Вы создали новую игру Ren'Py."

    # Меню выбора ответа:
    menu:
        "text"

        "Убить Хитлера":
            jump kill

        "Пойти в вагон":
            g "text"

            hide peten hat sad with moveoutleft
            hide hitler normal with easeoutleft

            jump trainCarriage

    return

# Попытка убийства:
label kill:

    play music death

    show hitler normal at rightHitler

    g "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return

# Переход в вагон:
label trainCarriage:

    scene bg train carriage is inside
    with fade

    show peten serious at leftPeten
    with dissolve

    p "Вы создали новую игру Ren'Py."

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

# Нахамить Гимлеру:
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