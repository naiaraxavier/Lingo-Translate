from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()
    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
    else:
        text_to_translate = "O que deseja traduzir?"
        translate_from = "pt"
        translate_to = "en"

    translated = translated_text(
        text_to_translate, translate_from, translate_to
    )
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@translate_controller.route("/reverse", methods=["POST"])
def index_reverse():
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    translated = translated_text(
        text_to_translate, translate_from, translate_to
    )
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )


def translated_text(text_to_translate, translate_from, translate_to):
    return GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)
