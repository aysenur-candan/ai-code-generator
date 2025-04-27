from flask import Flask, request, jsonify, render_template  
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OLLAMA_API_URL = "http://host.docker.internal:11434/api/generate"
MODEL_NAME = "gemma3:1b"

SYSTEM_PROMPT = (
    "Sen bir yapay zekâ destekli Python kod üretici asistansın. "
    "Kullanıcının verdiği isteğe (prompt) göre, sadece Python dilinde bir kod üret. "
    "Kodun işlevsel, doğru ve kullanıcı isteğini tam karşılayan bir çözüm olmalı. "
    "Cevabının sonunda, ürettiğin kodu özetleyen kısa ve anlamlı bir başlık yaz. "
    "Başlığı 'Başlık:' etiketiyle belirt. "
    "Yanıtında sadece kodu ve başlığı döndür, başka açıklama ekleme."
)

def generate_code(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": f"{SYSTEM_PROMPT}\n\nKullanıcı promptu: {prompt}",
        "stream": False
    }

    response = requests.post(OLLAMA_API_URL, json=payload)
    
    print(response.json()) 
    
    result = response.json().get("response", "")

    # Kod ve başlık ayrıştır
    lines = result.strip().split("\n")
    code_lines = []
    title = "Başlık bulunamadı"
    for line in lines:
        if line.lower().startswith("başlık:"):
            title = line.replace("Başlık:", "").strip()
            break
        else:
            code_lines.append(line)

    return {
        "code": "\n".join(code_lines),
        "title": title
    }


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt boş olamaz."}), 400

    try:
        result = generate_code(prompt)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
