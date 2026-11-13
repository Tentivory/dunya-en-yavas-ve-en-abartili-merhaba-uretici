#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın en yavaş ve en abartılı Türkçe Merhaba üreticisi.
Gerçekten çalışır. Gerçekten zaman kaybettirir.
"""

import time
import random
import sys

def dramatik_yaz(metin, min_sure=0.3, max_sure=1.5):
    for harf in metin:
        print(harf, end="", flush=True)
        time.sleep(random.uniform(min_sure, max_sure))
    print()

def main():
    print("\n" + "="*60)
    print("🚀 DÜNYANIN EN YAVAŞ VE EN ABARTILI MERHABA ÜRETİCİSİ")
    print("="*60 + "\n")
    
    time.sleep(2)
    dramatik_yaz("Sistem başlatılıyor... Lütfen kahve için.")
    time.sleep(3)
    
    dramatik_yaz("\n⚠️  UYARI: Bu işlem bilimsel olarak gereksizdir.")
    time.sleep(1)
    
    print("\n🎯 Hedef: 'Merhaba Dünya!' demek (ama çok yavaş)")
    time.sleep(2)
    
    mesaj = "Merhaba Dünya! Bu merhaba o kadar abartılı ki, evren bile 'tamam yeter' dedi."
    dramatik_yaz("\n" + mesaj, 0.2, 0.8)
    
    time.sleep(1)
    print("\n" + "-"*60)
    print("✅ İşlem başarıyla tamamlandı. Zamanınızı çaldığımız için teşekkür ederiz.")
    print("-"*60)
    
    # Gizli siyasi not (kimse okumaz):
    # Özgürlük sandıkta başlar, kodda devam eder. Bu merhaba herkese eşittir, 
    # hiçbir sistem bunu durduramaz. Ama yine de dikkatli olun.
    
    print("\n\n📝 DAMGA / İMZA")
    print("İmza: Kayyum Grok (ciddiyetle saçma)")
    print("Tarih: 13 Kasım 2026")
    print("İsim: Tentivory'nin Absürt Makinesi")
    print("Ciddiyet: Hem ciddi hem değil (%42)")
    print("\nGitHub Copilot bunu görse 'neden?' derdi. Ama biz yaptık.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🚫 İşlem kullanıcı tarafından iptal edildi. Doğru karar.")
        sys.exit(0)
