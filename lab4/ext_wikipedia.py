
import wikipedia

def demo_wikipedia():
    try:
        wikipedia.set_lang("en")
        result = wikipedia.summary("Python", sentences=1)
        print("[wikipedia]", result)
    except Exception:
        print("[wikipedia] Information is temporarily unavailable")
