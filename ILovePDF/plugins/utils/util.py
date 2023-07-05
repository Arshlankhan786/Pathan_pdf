# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = os.path.abspath(__file__)

from configs.db import myID
from itertools import islice
from configs.db import dataBASE
from configs.config import settings
from lang import __users__, langList
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# loading languages
try:
    if settings.MULTI_LANG_SUP:
        langs = os.listdir(f"./lang")
        for lang in langs:
            if lang.endswith(".py") and lang not in [
                "__init__.py",
                "__users__.py",
                "__demo__.py",
            ]:
                exec(f"from lang import {lang[:-3]}")
                logger.debug(f"adding {lang[:-3]}")
    else:
        exec(f"from lang import {settings.DEFAULT_LANG}")
        exec(f"from lang import eng")
except Exception as Error:
    logger.debug(f"lang: %s" % (Error), exc_info=True)
    logger.debug(f"ERROR IN DEFAULT LANG: {Error}")


#  BUTTON CREATOR 
deBUTTON_SPLIT = 2
async def createBUTTON(btn, order=deBUTTON_SPLIT):
    try:
        # https://favtutor.com/blogs/string-to-dict-python
        # btn =  ast.literal_eval(btn)   # convert str to dict
        button = []
        for key, value in btn.items():
            if value.startswith(tuple(["https://", "http://"])):
                temp = InlineKeyboardButton(
                    key, url=value.format(myID[0].username)
                )  # add bot_username for creating add grup link else pass
            else:
                temp = InlineKeyboardButton(key, callback_data=value)
            button.append(temp)
        if order == deBUTTON_SPLIT:
            keyboard = [
                button[i : i + deBUTTON_SPLIT]
                for i in range(0, len(button), deBUTTON_SPLIT)
            ]
        else:
            new_order = [int(x) for x in str(order)]
            button = iter(button)
            keyboard = [list(islice(button, elem)) for elem in new_order]

        return InlineKeyboardMarkup(keyboard)
    except Exception as Error:
        logger.exception("🐞 %s : %s" % (file_name, Error))


#  TEXT, BUTTON TRANSLATOR 
async def translate(
    text :str = None,
    button :dict = None,
    asString :bool = False,
    order :int = deBUTTON_SPLIT,
    lang_code :str = settings.DEFAULT_LANG,
):
    rtn_text = text
    rtn_button = button
    try:
        if text is not None:
            rtn_text = eval(f"{lang_code}.{text}")
        if button is not None:
            rtn_button = eval(f"{lang_code}.{button}")
    except Exception as Error:
        logger.debug(f"❌❌ can't find {text} : %s" % (Error))
        if text is not None:
            rtn_text = eval(f"eng.{text}")
        if button is not None:
            rtn_button = eval(f"eng.{button}")
    finally:
        if asString:
            return rtn_text, rtn_button  # return button as String
    try:
        if button is not None:
            rtn_button = await createBUTTON(btn=rtn_button, order=order)
    except Exception as Error:
        logger.debug("🚫 %s: %s" % (file_name, Error))
    finally:
        return (
            rtn_text,
            rtn_button,
        )  # return desired text, button (one text+button at once)


#  GET USER LANG CODE 
async def getLang(chatID :int) -> str:
    if not settings.MULTI_LANG_SUP:  # if multiple lang not supported
        return str(settings.DEFAULT_LANG)  # return default lang
    lang = __users__.userLang.get(
        int(chatID), str(settings.DEFAULT_LANG)
    )  # else return corresponding lang code
    return (
        lang if lang in langList else settings.DEFAULT_LANG
    )  # return lang code if in langList(
    # this way you can simply remove lang by removing lang from list)


#  ADD VALUES TO CB DICT 
async def editDICT(
    inDir: dict, value :bool = False, front=False
) -> dict:
    outDir = {}

    if front:  # changes cb in UI
        for i, j in inDir.items():
            outDir[i.format(front)] = j
        inDir = outDir
    if value and type(value) != list:  # changes cb.data
        for i, j in inDir.items():
            outDir[i] = j.format(value)
    elif value and type(value) == list:
        if len(value) == 2:
            for i, j in inDir.items():
                outDir[i] = j.format(value[0], value[1])
        if len(value) == 3:
            for i, j in inDir.items():
                outDir[i] = j.format(value[0], value[1], value[2])
    return outDir

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
