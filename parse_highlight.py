import docx

def parse_highlight(doc):
    parsed = []
    print(doc.paragraphs[0].runs[0].text)
    runs_list = [para.runs for para in doc.paragraphs]
    ignore_chars = {',', '', ':', ';', '.'}
    for para_runs in runs_list:
        res = []
        for run in para_runs:
            if run.text.strip() in ignore_chars:
                continue
            if run.font.highlight_color == 3:
                res.append([run.text])
            elif run.font.highlight_color is not None:
                res.append(run.text)
        if res:
            parsed.append(res)
    return parsed

if __name__ == "__main__":
    pass