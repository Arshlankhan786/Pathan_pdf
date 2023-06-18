file_name = "plugins/dm/textToPdf/callBack.py"
author_name = "telegram.dog/nabilanavab"
source_code = "https://github.com/nabilanavab/ilovepdf"

from plugins.utils       import *
from logger              import logger
from pyrogram.types      import InputMediaPhoto
from pyrogram            import filters, Client as ILovePDF

@ILovePDF.on_callback_query(filters.regex("^t2p(?!.*:).*$"))
async def text_to_pdf_cb(bot, callbackQuery):
    try:
        lang_code = await util.getLang(callbackQuery.message.chat.id)
        if await render.header(bot, callbackQuery, lang_code=lang_code):
            return
        await callbackQuery.answer()

        if True:
            if len(callbackQuery.data.split("|")) == 1:
                tTXT, _ = await util.translate(text="pdf2TXT['size_btn']", lang_code=lang_code)
                tTXT = await util.createBUTTON(tTXT, "121")
                media="https://graph.org/file/c301b7af1e637f642a520.jpg"
            if len(callbackQuery.data.split("|")) == 2:
                tTXT, _ = await util.translate(text="pdf2TXT['fifteen']", lang_code=lang_code)
                front, _ = await util.translate(text="_SELECT_HEAD_FONT", lang_code=lang_code)
                tTXT = await util.editDICT(inDir=tTXT, value=f"{callbackQuery.data}", front=front)
                tTXT = await util.createBUTTON(tTXT, "15551")
                media="https://graph.org/file/83c1f58d4c36b62aa92f3.jpg"
            elif len(callbackQuery.data.split("|")) == 3:
                tTXT, _ = await util.translate(text="pdf2TXT['fifteen']", lang_code=lang_code)
                front, _ = await util.translate(text="_SELECT_PARA_FONT", lang_code=lang_code)
                tTXT = await util.editDICT(inDir=tTXT, value=f"{callbackQuery.data}", front=front)
                tTXT = await util.createBUTTON(tTXT, "15551")
                media="https://graph.org/file/83c1f58d4c36b62aa92f3.jpg"
            elif len(callbackQuery.data.split("|")) == 4:
                tTXT, _ = await util.translate(text="pdf2TXT['six']", lang_code=lang_code)
                front, _ = await util.translate(text="_SELECT_COLOR", lang_code=lang_code)
                tTXT = await util.editDICT(inDir=tTXT, value=f"{callbackQuery.data}", front=front)
                tTXT = await util.createBUTTON(tTXT, "1331")
                media="https://graph.org/file/055bc5df94dc7859f59fd.jpg"
            elif len(callbackQuery.data.split("|")) == 5:
                tTXT, _ = await util.translate(text="pdf2TXT['six_']", lang_code=lang_code)
                front, _ = await util.translate(text="_SELECT_BG_COLOR", lang_code=lang_code)
                tTXT = await util.editDICT(inDir=tTXT, value=f"{callbackQuery.data}", front=front)
                tTXT = await util.createBUTTON(tTXT, "1331")
                media="https://graph.org/file/427b991e3e24865ad9cf7.jpg"
            
            return await callbackQuery.edit_message_media(
                media=InputMediaPhoto(media=media, caption=f"```{callbackQuery.message.caption```"), reply_markup=tTXT
            )
        
    except Exception as Error:
        logger.exception("1️⃣ 🐞 %s: %s" %(file_name, Error), exc_info=True)

# CONTACT AUTHOR: nabilanavab@gmail.com
