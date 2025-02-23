import requests
from bs4 import BeautifulSoup

# 1. 헤더에 User-Agent 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 2. 웹 페이지 가져오기
url = "https://ncode.syosetu.com/n8920ex/113"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # 3. HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 4. 특정 내용 추출 (div 태그와 클래스명으로 추출)
    novel_content = soup.find("div", class_="js-novel-text p-novel__text")
    
# 후리가나 포함한 텍스트 변환 함수
    def extract_ruby_text(tag):
        text_parts = []
        for element in tag.contents:
            if element.name == "ruby":  # 한자 + 후리가나 처리
                kanji = "".join(element.find_all(string=True, recursive=False))
                furigana = element.rt.get_text() if element.rt else ""
                text_parts.append(f"{kanji}({furigana})" if furigana else kanji)
            elif element.name == "br":  # <br/> 태그 처리 (줄바꿈 추가)
                text_parts.append("\n")
            else:  # 일반 텍스트
                text_parts.append(str(element))
        return "".join(text_parts)

# 줄 바뀜 유지하면서 후리가나 포함한 텍스트 추출
    if novel_content:
        text_content = "\n".join(extract_ruby_text(p) for p in novel_content.find_all(["p", "div"]))
            # 5. 저장할 파일의 절대 경로
        output_path = "C:/Users/MG/Projects/text/novel_output_with_furigana.txt"

            # 6. 텍스트를 파일에 저장
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text_content)

        print(f"저장 완료! 파일 경로: {output_path}")
    else:
        print("후리가나 변환된 내용이 없습니다. 후리가나가 포함된 <ruby> 태그가 없을 수 있습니다.")
else:
    print(f"웹 페이지를 가져오지 못했습니다. 상태 코드: {response.status_code}")
