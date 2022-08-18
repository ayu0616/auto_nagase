from PIL.JpegImagePlugin import JpegImageFile
import sys
import pyocr
import pyocr.builders
import pdf2image
import re


def get_sum_score(scores: list[str]):
    "'得点/満点'の形式のリストから、合計点を抽出する"
    split_scores = [*map(lambda x: x.split("/"), scores)]
    sum_score = 0
    max_score_max = 0  # 満点の最大値
    for split_score in split_scores:
        if int(split_score[1]) > max_score_max:
            sum_score = int(split_score[0])
            max_score_max = int(split_score[1])
    return sum_score


def get_score(pdf_path: str):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    # The tools are returned in the recommended order of usage
    tool = tools[0]
    # print("Will use tool '%s'" % (tool.get_name()))
    # Ex: Will use tool 'libtesseract'

    # pdfから画像オブジェクトに
    images: list[JpegImageFile] = pdf2image.convert_from_path(pdf_path, dpi=200, fmt="jpg")
    lang = "eng"
    # lang = 'jpn'
    # 画像オブジェクトからテキストに
    image = images[-1]
    txt = tool.image_to_string(image, lang=lang, builder=pyocr.builders.TextBuilder())
    scores: list[str] = re.findall(r"[0-9]+/[0-9]+", txt)  # "得点/満点"の形式のものを抽出（途中の記述問題のものも残っているから排除せねば）
    return get_sum_score(scores)


if __name__ == "__main__":
    print(get_score("./test.pdf"))
