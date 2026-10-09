import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

buy_pro_logic = '''
function buyPro(plan_type) {
    playSound('tap');
    if (!isTMA) {
        showToast("Faqat Telegram bot orqali ishlaydi!");
        return;
    }
    
    let amount = 0;
    if (plan_type === 'click_1mo') amount = 15000;
    if (plan_type === 'click_3mo') amount = 50000;
    if (plan_type === 'click_lifetime') amount = 200000;
    
    if (plan_type.startsWith('click')) {
        tg.sendData(JSON.stringify({
            action: "BUY_PRO_CLICK",
            plan: plan_type,
            amount_uzs: amount,
            userId: currentUser.uid,
            timestamp: Date.now()
        }));
    } else if (plan_type === 'stars') {
        tg.sendData(JSON.stringify({
            action: "BUY_PRO_STARS",
            userId: currentUser.uid
        }));
    }
    
    closePremiumModal();
    showToast("To'lov oynasi ochilmoqda...");
}
'''
js = re.sub(r'function buyPro\(provider\) \{.*?showToast\("To\'lov oynasi ochilmoqda\.\.\."\);\n\}', buy_pro_logic.strip(), js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated buyPro")
