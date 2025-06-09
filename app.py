# app.py (versão final com controle de taxa de chamadas)

import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import webbrowser
import json
from datetime import datetime, timedelta
import time # NOVO: Importa a biblioteca para fazer pausas

# 1. Configuração da API (sem alterações)
try:
    genai.configure(api_key='AIzaSyDeEd2XQ0Pr4ZQ4PMSmgMOld7WvR-EaQOU') # Sua chave aqui
    generation_config = {"response_mime_type": "application/json"}
    model = genai.GenerativeModel('gemini-1.5-flash', generation_config=generation_config)
    print("✅ Modelo Gemini conectado.")
except Exception as e:
    print(f"❌ Falha na configuração do Gemini: {str(e)}")
    model = None

# --- Funções dos Agentes (sem alterações) ---
def call_gemini(prompt):
    if not model: raise Exception("Modelo de IA não inicializado.")
    response = None
    try:
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        print(f"Erro na comunicação com a IA ou no processamento da resposta: {e}")
        error_text = "Nenhuma resposta recebida da IA."
        if response and hasattr(response, 'text'): error_text = response.text
        print(f"Resposta bruta da IA (se houver): {error_text}")
        raise Exception(f"Falha na comunicação com a IA. Detalhe: {e}")

def agent_architect(goals, level, time_available, end_date_str=None):
    duration_constraint = f"O plano DEVE ser concluído até {end_date_str}." if end_date_str else "Nenhuma data final específica."
    prompt = f"""Você é um Arquiteto de Conhecimento. Baseado no objetivo '{goals}', nível '{level}', {time_available} horas/semana e a restrição '{duration_constraint}', crie uma lista de módulos de estudo. Retorne APENAS um JSON com a chave "modules", contendo uma lista de objetos com a chave "focus"."""
    return call_gemini(prompt)

# Em app.py, substitua APENAS a função agent_curator por esta versão:

# Em app.py, substitua APENAS a função agent_curator por esta versão final:

def agent_curator(focus, week_number, start_date):
    """
    AGENTE 2 (v3.0 - Mentor Sênior com Tópicos Explícitos): Detalha a semana de forma ultra-rica.
    """
    end_date = start_date + timedelta(days=6)
    prompt = f"""
    Você é um Mentor Educacional Sênior e especialista em design instrucional.
    Sua missão é criar um plano de estudos semanal EXCEPCIONALMENTE DETALHADO, PRÁTICO e RICO para um estudante.

    O tema principal desta semana ({week_number}) é: "{focus}".

    Crie um plano que seja verdadeiramente útil. Em vez de listas genéricas, forneça recursos específicos e nomeados.
    Estruture sua resposta APENAS como um objeto JSON, seguindo rigorosamente o formato abaixo.

    INSTRUÇÕES PARA OS CAMPOS:
    - Para 'study_topics': Crie uma lista com 5 a 7 TÓPICOS TÉCNICOS e específicos. Seja direto. Ex: 'Sintaxe do CREATE TABLE', 'Tipos de Dados SQL', 'Cláusula WHERE'.
    - Para 'resources': Forneça o TÍTULO do recurso e a FONTE (Site, Canal no YouTube, Autor do Livro, etc).

    Formato JSON esperado:
    {{
      "week_number": {week_number},
      "weekly_theme": "{focus}",
      "start_date": "{start_date.strftime('%d/%m/%Y')}",
      "end_date": "{end_date.strftime('%d/%m/%Y')}",
      "learning_objectives": [
        "Um objetivo de aprendizado claro e mensurável.",
        "Outro objetivo específico para a semana.",
        "Um terceiro objetivo prático."
      ],
      "study_topics": [
        "Conceito técnico específico 1",
        "Ferramenta ou comando 2",
        "Sintaxe ou função 3",
        "Teoria importante 4",
        "Conceito relacionado 5"
      ],
      "daily_plan": [
        {{ "days": "1-2 (Foco em Teoria)", "activity": "Descrição da atividade teórica, como ler capítulos ou assistir vídeos sobre os tópicos centrais." }},
        {{ "days": "3-4 (Prática Dirigida)", "activity": "Descrição de exercícios para praticar os tópicos listados." }},
        {{ "days": "5 (Projeto da Semana)", "activity": "Descrição do mini-projeto semanal para consolidar o conhecimento." }}
      ],
      "resources": {{
        "articles_blogs": ["Artigo 1: Título e Fonte"],
        "videos_tutorials": ["Vídeo 1: Título e Canal"],
        "books_chapters": ["Livro 1: Título, Autor e Capítulo"]
      }},
      "weekly_project": "Descrição detalhada de um mini-projeto prático para ser desenvolvido ao final da semana.",
      "tools_and_tips": [
        "Uma dica prática sobre ferramentas.",
        "Uma dica de metodologia de estudo."
      ]
    }}
    """
    return call_gemini(prompt)

def agent_tutor(topic, level, help_type, context=""):
    context_prompt = f"Leve em conta o seguinte contexto adicional: '{context}'" if context else ""
    action_map = {'challenge': "Crie um mini-desafio prático e conciso.", 'tip': f"Forneça uma dica técnica ou ferramenta PRÁTICA sobre o tema para alguém de nível '{level}'. EVITE conselhos genéricos. {context_prompt}"}
    output_map = {'challenge': 'Retorne APENAS um JSON com "challenge" e "solution".', 'tip': 'Retorne APENAS um JSON com "title" e "description".'}
    action = action_map.get(help_type, "Dê uma mensagem de encorajamento.")
    output_format = output_map.get(help_type, 'Retorne APENAS um JSON com uma chave "text".')
    prompt = f"Você é um Tutor de IA especialista. O usuário pediu uma ajuda do tipo '{help_type}' sobre o tópico '{topic}'. Tarefa: {action}. {output_format}"
    return call_gemini(prompt)

# --- Aplicação Flask ---
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    try:
        data = request.form
        architecture = agent_architect(data['goals'], data['level'], data['time'], data.get('end_date'))
        
        weekly_schedule = []
        start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
        
        # O loop que causa o problema
        for i, module in enumerate(architecture['modules']):
            print(f"Gerando detalhes para a Semana {i+1}: {module['focus']}...")
            week_plan = agent_curator(module['focus'], i + 1, start_date)
            weekly_schedule.append(week_plan)
            start_date += timedelta(weeks=1)
            
            # NOVO: A pausa de 1.1 segundos para respeitar o limite da API
            time.sleep(1.1) 
            
        recommendation = {"overview": f"Plano de estudos para: {data['goals']}.", "weekly_schedule": weekly_schedule}
        return jsonify({"success": True, "recommendation": recommendation})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Rotas de /generate_challenge e /generate_tip (sem alterações)
@app.route('/generate_challenge', methods=['POST'])
def generate_challenge():
    try:
        data = request.json
        challenge_data = agent_tutor(data['topic'], data['level'], 'challenge', data.get('context'))
        return jsonify({"success": True, "data": challenge_data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/generate_tip', methods=['POST'])
def generate_tip():
    try:
        data = request.json
        tip_data = agent_tutor(data['topic'], data['level'], 'tip', data.get('context'))
        return jsonify({"success": True, "data": tip_data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run(port=5000, debug=False)