from helpers import get_runs, get_styled_runs_list
         
def get_highlighted_text(doc, style_dict):
    runs = get_runs(doc) 
    result = get_styled_runs_list(runs, style_dict)
    return result

if __name__ == "__main__":
    pass