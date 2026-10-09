import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add trialStarted and isPro to initial state
js = js.replace('lastHeartRegen: parseInt(localStorage.getItem(\'wunder_last_regen\') || Date.now()),', 'lastHeartRegen: parseInt(localStorage.getItem(\'wunder_last_regen\') || Date.now()),\n    trialStarted: null,\n    isPro: false,')

# Add trial check logic to TMA init
trial_logic = '''
                    if ((cloudState.xp || 0) >= (appState.xp || 0)) {
                        Object.assign(appState, cloudState);
                    }
                } catch(e){}
            }
            
            // 3-Day Trial Logic
            if (!appState.trialStarted) {
                appState.trialStarted = Date.now();
                // Save immediately
                tg.CloudStorage.setItem('wunder_state', JSON.stringify(appState));
            }
            
            const THREE_DAYS_MS = 3 * 24 * 60 * 60 * 1000;
            const elapsed = Date.now() - appState.trialStarted;
            const isTrialActive = elapsed < THREE_DAYS_MS;
            
            if (isTrialActive && !appState.isPro) {
                appState.isAdmin = true; // Give infinite hearts temporarily
                const daysLeft = Math.ceil((THREE_DAYS_MS - elapsed) / (24 * 60 * 60 * 1000));
                
                // Try to find the upgrade button in settings
                setTimeout(() => {
                    const upgradeCard = document.querySelector('.card[onclick="openPremiumModal()"]');
                    if (upgradeCard) {
                        upgradeCard.innerHTML = `<div style="font-weight:800; font-size:16px; display:flex; justify-content:center; align-items:center; gap:8px;">
                            <i data-lucide="zap" style="width:20px; fill: white;"></i> ⚡ ${daysLeft} kun sinov
                        </div>`;
                    }
                }, 500);
            } else if (!appState.isPro) {
                appState.isAdmin = false;
                appState.lives = Math.min(appState.lives, 5); // Cap hearts at 5
                
                setTimeout(() => {
                    const upgradeCard = document.querySelector('.card[onclick="openPremiumModal()"]');
                    if (upgradeCard) {
                        upgradeCard.innerHTML = `<div style="font-weight:800; font-size:16px; display:flex; justify-content:center; align-items:center; gap:8px;">
                            <i data-lucide="zap" style="width:20px; fill: white;"></i> ⚡ PRO olish
                        </div>`;
                    }
                }, 500);
            }
            
            isCloudSynced = true;
'''

js = re.sub(r'if \(\(cloudState\.xp \|\| 0\) >= \(appState\.xp \|\| 0\)\) \{\n\s*Object\.assign\(appState, cloudState\);\n\s*\}\n\s*\} catch\(e\)\{\}\n\s*\}\n\s*isCloudSynced = true;', trial_logic.strip(), js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Added trial logic to TMA init")
