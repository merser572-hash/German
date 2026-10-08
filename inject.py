import json
import re

with open('extracted_grammar.json', 'r', encoding='utf-8') as f:
    grammar_data = f.read()

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Remove old A1_GRAMMAR and renderGrammar
app_js = re.sub(r'const A1_GRAMMAR = \{.*?\n\}\;\n*function renderGrammar\(\) \{.*?\n\}\n', '', app_js, flags=re.DOTALL)

# Let's append the new data and functions
new_code = f'''
const GRAMMAR_DATA = {grammar_data};

function renderGrammar() {{
    const container = document.getElementById('grammar-cards-container');
    if (!container) return;
    container.innerHTML = '';

    GRAMMAR_DATA.forEach((chap, idx) => {{
        const card = document.createElement('div');
        card.className = 'grammar-item';
        card.style.marginBottom = '12px';
        card.style.cursor = 'pointer';
        
        card.innerHTML = `
            <div class="grammar-header" style="background: #fff;">
                <span style="font-size: 16px; font-weight: 800; color: #2D3436;">${{chap.title}}</span>
                <span style="font-size: 11px; font-weight: 800; padding: 2px 8px; border-radius: 12px; background: #E8F8F5; color: #16A085; border: 1px solid #16A085;">${{chap.tag}}</span>
            </div>
            <div class="grammar-body" style="display: block; max-height: none; padding: 0 20px 15px 20px; background: #fff; border-bottom: 2px solid transparent;">
                <p style="font-size:13px; color:var(--text-muted); line-height:1.4;">${{chap.summary}}</p>
            </div>
        `;
        
        card.onclick = () => openGrammarChapter(idx);
        container.appendChild(card);
    }});
}}

let activeGrammarChap = null;

function openGrammarChapter(idx) {{
    playSound('tap');
    activeGrammarChap = GRAMMAR_DATA[idx];
    document.getElementById('gm-title').innerText = activeGrammarChap.title;
    document.getElementById('gm-summary').innerText = activeGrammarChap.summary;
    document.getElementById('gm-fritz-tip').innerText = activeGrammarChap.fritz_tip;

    const rulesBox = document.getElementById('gm-rules-list');
    rulesBox.innerHTML = '';
    activeGrammarChap.rules.forEach(r => {{
        const div = document.createElement('div');
        div.style.marginBottom = '8px';
        div.innerHTML = `<span style="font-weight:800; font-size:13px; color:#0984E3;">• ${{r.label}}:</span> <span style="font-size:13px; color:#2D3436;">${{r.tip}}</span>`;
        rulesBox.appendChild(div);
    }});

    const tableBox = document.getElementById('gm-table-container');
    tableBox.innerHTML = '';
    if (activeGrammarChap.table) {{
        let ths = activeGrammarChap.table.headers.map(h => `<th>${{h}}</th>`).join('');
        let trs = activeGrammarChap.table.rows.map(row => `<tr>${{row.map(c => `<td>${{c}}</td>`).join('')}}</tr>`).join('');
        tableBox.innerHTML = `<table class="rule-table"><thead><tr>${{ths}}</tr></thead><tbody>${{trs}}</tbody></table>`;
    }}

    const quizBox = document.getElementById('gm-quiz-container');
    quizBox.innerHTML = '';
    activeGrammarChap.quiz.forEach((qObj, qIdx) => {{
        const qDiv = document.createElement('div');
        qDiv.style.margin = '10px 0';
        qDiv.style.background = '#F8F9FA';
        qDiv.style.border = '2px solid var(--border-color)';
        qDiv.style.borderRadius = '14px';
        qDiv.style.padding = '10px 12px';
        
        let opts = qObj.options.map((opt, oIdx) => `
            <button class="action-btn" style="margin-top:6px; font-size:13px; padding:6px 10px; width: 100%;" onclick="answerGrammarQuiz(${{qIdx}}, ${{oIdx}}, this)">
                ${{opt}}
            </button>
        `).join('');

        qDiv.innerHTML = `
            <div style="font-weight:700; font-size:13px; margin-bottom:4px;">Frage ${{qIdx + 1}}: ${{qObj.q}}</div>
            <div class="opts-group" id="quiz-opts-${{qIdx}}">${{opts}}</div>
            <div id="quiz-feedback-${{qIdx}}" style="font-size:12px; font-weight:700; margin-top:6px; display:none;"></div>
        `;
        quizBox.appendChild(qDiv);
    }});

    const modal = document.getElementById('modal-grammar-detail');
    modal.style.display = 'flex';
}}

function answerGrammarQuiz(qIdx, oIdx, btn) {{
    if (!activeGrammarChap) return;
    const qObj = activeGrammarChap.quiz[qIdx];
    const feed = document.getElementById(`quiz-feedback-${{qIdx}}`);
    const parent = document.getElementById(`quiz-opts-${{qIdx}}`);
    
    parent.querySelectorAll('button').forEach(b => b.disabled = true);
    
    feed.style.display = 'block';
    if (oIdx === qObj.answer) {{
        playSound('success');
        btn.style.background = '#55EFC4';
        feed.style.color = '#00B894';
        feed.innerText = '✅ Richtig! ' + qObj.hint;
        appState.xp += 10;
        updateStats();
    }} else {{
        playSound('error');
        btn.style.background = '#FF7675';
        feed.style.color = '#D63031';
        feed.innerText = '❌ Nicht ganz: ' + qObj.hint;
    }}
}}

function closeGrammarModal() {{
    playSound('tap');
    document.getElementById('modal-grammar-detail').style.display = 'none';
}}
'''

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js + new_code)
print('Injected successfully!')
