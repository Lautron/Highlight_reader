def get_formatted_run(run, style_dict):
    highlight_id = run.font.highlight_color 
    if highlight_id in style_dict.keys():
        return {style_dict[highlight_id]: run.text}
    else:
        return {style_dict['normal']: run.text}
     
def format_run(run, style_dict):
    ignore_chars = {',', '', ':', ';', '.'}
    if run.text.strip() in ignore_chars: 
        return
    return get_formatted_run(run, style_dict) 
        
def get_styled_runs_list(runs, style_dict):
    result = []
    for paragraph in runs:
        para_list = []
        for run in paragraph:
            styled_run = format_run(run, style_dict)
            para_list.append(styled_run)
        if res:
            parsed.append(para_list)
    return res

def get_runs(doc):
    return [para.runs for para in doc.paragraphs]