import os
import random
import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import XSD

# 1. ONTOLOJİ TANIMLAMALARI
PET_NS = Namespace("http://www.semanticweb.org/pet-management-ontology#")
g = Graph()
g.bind("pet", PET_NS)

# ⚠️ DOSYA KONTROLÜ
csv_path = "pet_adoption_dataset.csv"
if not os.path.exists(csv_path):
    print(f"❌ HATA: Masaüstünde '{csv_path}' dosyası bulunamadı!")
    exit()

print("📊 1. ADIM: Masaüstündeki gerçek Kaggle veri seti başarıyla sisteme yükleniyor...")
df = pd.read_csv(csv_path).head(5000)

# 🩺 40 KİŞİLİK DEV VETERİNER KADROSU VE HASTANE HAVUZU
vets_pool = [
    {"ID": "VET4412", "Name": "Dr. Aslı Yılmaz", "Spec": "Cerrahi", "Clinic": "Anadolu Hayvan Hastanesi", "Exp": 8},
    {"ID": "VET5523", "Name": "Dr. Can Tekin", "Spec": "Dermatoloji", "Clinic": "Merkez Vet Tıp Merkezi", "Exp": 4},
    {"ID": "VET6634", "Name": "Dr. Zeynep Aydın", "Spec": "Kardiyoloji", "Clinic": "Anadolu Hayvan Hastanesi", "Exp": 12},
    {"ID": "VET7745", "Name": "Dr. Murat Kaya", "Spec": "Ortopedi", "Clinic": "Merkez Vet Tıp Merkezi", "Exp": 7},
    {"ID": "VET8856", "Name": "Dr. Ebru Şahin", "Spec": "Göz Hastalıkları", "Clinic": "Anadolu Hayvan Hastanesi", "Exp": 9},
    {"ID": "VET9967", "Name": "Dr. Ahmet Demir", "Spec": "Dahiliye", "Clinic": "Pati Veteriner Kliniği", "Exp": 15},
    {"ID": "VET1122", "Name": "Dr. Merve Çetin", "Spec": "Onkoloji", "Clinic": "Anadolu Hayvan Hastanesi", "Exp": 6},
    {"ID": "VET2233", "Name": "Dr. Burak Eren", "Spec": "Diş Hekimliği", "Clinic": "Merkez Vet Tıp Merkezi", "Exp": 5},
    {"ID": "VET3344", "Name": "Dr. Gamze Yıldız", "Spec": "Doğum ve Jinekoloji", "Clinic": "Pati Veteriner Kliniği", "Exp": 11},
    {"ID": "VET5566", "Name": "Dr. Kaan Özdemir", "Spec": "Acil Tıp", "Clinic": "Anadolu Hayvan Hastanesi", "Exp": 3},
    {"ID": "VET1234", "Name": "Dr. Seda Yurt", "Spec": "Nöroloji", "Clinic": "Vadi Hayvan Hastanesi", "Exp": 10},
    {"ID": "VET2345", "Name": "Dr. Onur Arslan", "Spec": "Cerrahi", "Clinic": "Vadi Hayvan Hastanesi", "Exp": 14},
    {"ID": "VET3456", "Name": "Dr. Pelin Koç", "Spec": "Fizik Tedavi", "Clinic": "Pati Veteriner Kliniği", "Exp": 5},
    {"ID": "VET4567", "Name": "Dr. Hakan Çelik", "Spec": "Dahiliye", "Clinic": "Merkez Vet Tıp Merkezi", "Exp": 13},
    {"ID": "VET5678", "Name": "Dr. Deniz Bulut", "Spec": "Dermatoloji", "Clinic": "Vadi Hayvan Hastanesi", "Exp": 7},
    {"ID": "VET6789", "Name": "Dr. Tolga Yıldırım", "Spec": "Ortopedi", "Clinic": "Anadolu Hayvan Hastanesi", "Exp": 16},
    {"ID": "VET7890", "Name": "Dr. Nilay Duran", "Spec": "Kardiyoloji", "Clinic": "Pati Veteriner Kliniği", "Exp": 8},
    {"ID": "VET8901", "Name": "Dr. Serkan Avcı", "Spec": "Anesteziyoloji", "Clinic": "Vadi Hayvan Hastanesi", "Exp": 11},
    {"ID": "VET9012", "Name": "Dr. Elif Yaman", "Spec": "Radyoloji", "Clinic": "Merkez Vet Tıp Merkezi", "Exp": 9},
    {"ID": "VET9123", "Name": "Dr. Cemal Kurt", "Spec": "Acil Tıp", "Clinic": "Vadi Hayvan Hastanesi", "Exp": 4},
    {"ID": "VET9234", "Name": "Prof. Dr. Selim Efe", "Spec": "Onkoloji", "Clinic": "Ege Bölge Hayvan Hastanesi", "Exp": 22},
    {"ID": "VET9345", "Name": "Doç. Dr. Hale Can", "Spec": "Nöroşirürji", "Clinic": "Ege Bölge Hayvan Hastanesi", "Exp": 18},
    {"ID": "VET9456", "Name": "Dr. Emre Can", "Spec": "Yaban Hayatı Uzmanlığı", "Clinic": "Doğa ve Patiler Tıp Merkezi", "Exp": 6},
    {"ID": "VET9567", "Name": "Dr. Simge Aksoy", "Spec": "Dermatoloji", "Clinic": "Doğa ve Patiler Tıp Merkezi", "Exp": 5},
    {"ID": "VET9678", "Name": "Dr. Mert Öztürk", "Spec": "Cerrahi", "Clinic": "Marmara Veteriner Kompleksi", "Exp": 12},
    {"ID": "VET9789", "Name": "Dr. Aylin Yılmaz", "Spec": "Gastroenteroloji", "Clinic": "Marmara Veteriner Kompleksi", "Exp": 14},
    {"ID": "VET9890", "Name": "Dr. Ozan Demir", "Spec": "Üroloji", "Clinic": "Marmara Veteriner Kompleksi", "Exp": 7},
    {"ID": "VET9001", "Name": "Dr. Gizem Yıldız", "Spec": "Dahiliye", "Clinic": "Körfez Veteriner Polikliniki", "Exp": 11},
    {"ID": "VET9002", "Name": "Dr. Sinan Kaya", "Spec": "Cerrahi", "Clinic": "Körfez Veteriner Polikliniki", "Exp": 13},
    {"ID": "VET9003", "Name": "Dr. Nazlı Eren", "Spec": "Fizik Tedavi", "Clinic": "Ege Bölge Hayvan Hastanesi", "Exp": 8},
    {"ID": "VET9004", "Name": "Dr. Kerem Bulut", "Spec": "Davranış Bilimleri", "Clinic": "Doğa ve Patiler Tıp Merkezi", "Exp": 9},
    {"ID": "VET9005", "Name": "Dr. İrem Arslan", "Spec": "Göz Hastalıkları", "Clinic": "Marmara Veteriner Kompleksi", "Exp": 10},
    {"ID": "VET9006", "Name": "Dr. Bora Kılıç", "Spec": "Kardiyoloji", "Clinic": "Ege Bölge Hayvan Hastanesi", "Exp": 15},
    {"ID": "VET9007", "Name": "Dr. Tuğba Çetin", "Spec": "Endokrinoloji", "Clinic": "Körfez Veteriner Polikliniki", "Exp": 6},
    {"ID": "VET9008", "Name": "Dr. Alper Şahin", "Spec": "Ortopedi", "Clinic": "Marmara Veteriner Kompleksi", "Exp": 17},
    {"ID": "VET9009", "Name": "Dr. Hande Özdemir", "Spec": "Dermatoloji", "Clinic": "Anadolu Hayvan Hastanesi", "Exp": 5},
    {"ID": "VET9010", "Name": "Dr. Gökhan Duran", "Spec": "Diş Hekimliği", "Clinic": "Vadi Hayvan Hastanesi", "Exp": 8},
    {"ID": "VET9011", "Name": "Dr. Melis Avcı", "Spec": "Radyoloji", "Clinic": "Ege Bölge Hayvan Hastanesi", "Exp": 7},
    {"ID": "VET9013", "Name": "Dr. Berkay Kurt", "Spec": "Acil Tıp", "Clinic": "Marmara Veteriner Kompleksi", "Exp": 4},
    {"ID": "VET9014", "Name": "Dr. Ceren Yaman", "Spec": "Parazitoloji", "Clinic": "Doğa ve Patiler Tıp Merkezi", "Exp": 12}
]

treatment_pool = {
    "Vaccination": [
        ("Kuduz Aşısı", 450.0, "Yıllık rutin kuduz aşısı uygulandı."),
        ("Karma Aşı", 550.0, "DHPPi koruyucu aşı dozu tamamlandı."),
        ("Lösemi Aşısı", 600.0, "FeLV enfeksiyonuna karşı aşılama yapıldı.")
    ],
    "Surgery": [
        ("Kırık Operasyonu", 4500.0, "İntramedüller pin ve plak stabilizasyonu sağlandı."),
        ("Kısırlaştırma", 2500.0, "Ovariohisterektomi / Kastrasyon operasyonu sorunsuz bitti.")
    ],
    "Emergency": [
        ("Zehirlenme Müdahalesi", 1800.0, "Gastrik lavaj uygulandı, aktif kömür og IV sıvı tedavisi başlandı."),
        ("Trafik Kazası Müdahalesi", 5000.0, "Şok tedavisi oksijen desteği ve internal kanama takibi yapıldı.")
    ],
    "Checkup": [
        ("Rutin Kontrol", 350.0, "Genel sistemik muayene ve lenf yumrusu kontrolü normal."),
        ("Detaylı Kan Tahlili", 900.0, "Biyokimya ve hemogram parametreleri referans aralığında.")
    ]
}

first_names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
cities = ["Manisa, Şehzadeler", "İzmir, Bornova", "Manisa, Yunusemre", "İzmir, Karşıyaka", "İzmir, Buca", "Manisa, Turgutlu", "İzmir, Konak", "Manisa, Akhisar"]
pet_names_pool = ["Pati", "Duman", "Pamuk", "Gofret", "Mila", "Zeytin", "Tarçın", "Karamel", "Mavi", "Kont", "Max", "Bella", "Charlie", "Lucy", "Cooper"]

print(f"🔗 2. ADIM: {len(df)} adet gerçek kayıt tamamen benzersiz kimliklerle işleniyor...")

for index, row in df.iterrows():
    pet_uri = URIRef(PET_NS + f"CHIP_{row['PetID']}")
    owner_uri = URIRef(PET_NS + f"OWNER_{10000 + index}")
    vet = random.choice(vets_pool)
    vet_uri = URIRef(PET_NS + vet["ID"])

    # ── A) KAGGLE PET ÖZELLİKLERİ ──
    g.add((pet_uri, RDF.type, URIRef(PET_NS + str(row["PetType"]).strip().capitalize())))
    g.add((pet_uri, URIRef(PET_NS + "hasPetID"), Literal(str(row["PetID"]), datatype=XSD.string)))
    
    p_name = f"{random.choice(pet_names_pool)}_{row['PetID']}"
    g.add((pet_uri, URIRef(PET_NS + "hasName"), Literal(p_name, datatype=XSD.string)))
    
    age_years = max(1, int(row["AgeMonths"] // 12))
    g.add((pet_uri, URIRef(PET_NS + "hasAge"), Literal(age_years, datatype=XSD.integer)))
    g.add((pet_uri, URIRef(PET_NS + "hasBreed"), Literal(str(row["Breed"]), datatype=XSD.string)))
    g.add((pet_uri, URIRef(PET_NS + "hasGender"), Literal(random.choice(["Male", "Female"]), datatype=XSD.string)))
    
    # 🌟 ONDALIK GARANTİSİ: String üzerinden formatlayıp float yaparak Python'ın arkadaki uzun ondalık tutmasını engelliyoruz
    rounded_weight = float(f"{float(row['WeightKg']):.1f}")
    g.add((pet_uri, URIRef(PET_NS + "hasWeight"), Literal(rounded_weight, datatype=XSD.float)))

    # ── B) SAHTE OWNER ÖZELLİKLERİ ──
    g.add((owner_uri, RDF.type, URIRef(PET_NS + "Owner")))
    g.add((owner_uri, URIRef(PET_NS + "hasOwnerId"), Literal(f"OWNER_{10000 + index}", datatype=XSD.string)))
    
    unique_owner_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    g.add((owner_uri, URIRef(PET_NS + "hasName"), Literal(unique_owner_name, datatype=XSD.string))) 
    
    # 🌟 TELEFON GARANTİSİ: Tamamen bağımsız bir string fonksiyonuyla her döngüde taze numara üretilir
    dynamic_phone = "0532" + "".join([str(random.randint(0, 9)) for _ in range(7)])
    g.add((owner_uri, URIRef(PET_NS + "hasPhone"), Literal(dynamic_phone, datatype=XSD.string)))
    
    g.add((owner_uri, URIRef(PET_NS + "hasEmail"), Literal(f"owner_{index}@mail.com", datatype=XSD.string)))
    g.add((owner_uri, URIRef(PET_NS + "hasAddress"), Literal(random.choice(cities), datatype=XSD.string)))
    g.add((pet_uri, URIRef(PET_NS + "hasOwner"), owner_uri))

    # ── C) VETERİNER ÖZELLİKLERİ ──
    g.add((vet_uri, RDF.type, URIRef(PET_NS + "Veterinarian")))
    g.add((vet_uri, URIRef(PET_NS + "hasVetID"), Literal(vet["ID"], datatype=XSD.string))) 
    g.add((vet_uri, URIRef(PET_NS + "hasName"), Literal(vet["Name"], datatype=XSD.string))) 
    g.add((vet_uri, URIRef(PET_NS + "hasSpecialization"), Literal(vet["Spec"], datatype=XSD.string)))
    g.add((vet_uri, URIRef(PET_NS + "worksAtClinic"), Literal(vet["Clinic"], datatype=XSD.string)))
    g.add((vet_uri, URIRef(PET_NS + "hasExperience"), Literal(vet["Exp"], datatype=XSD.integer)))

    # ── D) TEDAVİ BİLGİLERİ VE BAĞLANTI KÖPRÜLERİ ──
    treatment_id = f"TRT_REC_{30000 + index}"
    treatment_uri = URIRef(PET_NS + treatment_id)
    
    trt_class = random.choice(list(treatment_pool.keys()))
    trt_type, trt_cost, trt_notes = random.choice(treatment_pool[trt_class])
    
    g.add((treatment_uri, RDF.type, URIRef(PET_NS + trt_class)))
    g.add((treatment_uri, URIRef(PET_NS + "treatmentType"), Literal(trt_type, datatype=XSD.string)))
    g.add((treatment_uri, URIRef(PET_NS + "treatmentDate"), Literal(f"2026-06-{random.randint(10,28)}", datatype=XSD.string)))
    g.add((treatment_uri, URIRef(PET_NS + "treatmentCost"), Literal(trt_cost, datatype=XSD.float)))
    g.add((treatment_uri, URIRef(PET_NS + "hasNotes"), Literal(trt_notes, datatype=XSD.string)))

    g.add((treatment_uri, URIRef(PET_NS + "isAppliedTo"), pet_uri)) 
    g.add((treatment_uri, URIRef(PET_NS + "isTreatedBy"), vet_uri)) 

g.serialize(destination="populated_clinic.ttl", format="turtle")
print("⚡ MUHTEŞEM! Kusursuz ve gerçekçi veritabanı 'populated_clinic.ttl' başarıyla oluşturuldu!")