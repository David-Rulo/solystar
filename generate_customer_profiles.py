#!/usr/bin/env python3
"""
Solystar — Customer Profile Generator for Seed Data
====================================================
Generates 25 realistic residential customer profiles for Central America,
covering Guatemala, Costa Rica, Panama, Honduras, and El Salvador.

Output: customer_profiles.json
"""

import json
import random
import hashlib
from datetime import datetime, timedelta

random.seed(42)

# ── Countries & cities ────────────────────────────────────────────────
LOCATIONS = [
    # Guatemala
    {"pais": "Guatemala", "ciudad": "Ciudad de Guatemala", "moneda": "GTQ", "tipo_cambio": 7.75},
    {"pais": "Guatemala", "ciudad": "Antigua Guatemala", "moneda": "GTQ", "tipo_cambio": 7.75},
    {"pais": "Guatemala", "ciudad": "Quetzaltenango", "moneda": "GTQ", "tipo_cambio": 7.75},
    # Costa Rica
    {"pais": "Costa Rica", "ciudad": "San José", "moneda": "CRC", "tipo_cambio": 530.0},
    {"pais": "Costa Rica", "ciudad": "Heredia", "moneda": "CRC", "tipo_cambio": 530.0},
    {"pais": "Costa Rica", "ciudad": "Alajuela", "moneda": "CRC", "tipo_cambio": 530.0},
    # Panama
    {"pais": "Panamá", "ciudad": "Ciudad de Panamá", "moneda": "USD", "tipo_cambio": 1.0},
    {"pais": "Panamá", "ciudad": "David", "moneda": "USD", "tipo_cambio": 1.0},
    {"pais": "Panamá", "ciudad": "Santiago de Veraguas", "moneda": "USD", "tipo_cambio": 1.0},
    # Honduras
    {"pais": "Honduras", "ciudad": "Tegucigalpa", "moneda": "HNL", "tipo_cambio": 24.7},
    {"pais": "Honduras", "ciudad": "San Pedro Sula", "moneda": "HNL", "tipo_cambio": 24.7},
    # El Salvador
    {"pais": "El Salvador", "ciudad": "San Salvador", "moneda": "USD", "tipo_cambio": 1.0},
    {"pais": "El Salvador", "ciudad": "Santa Ana", "moneda": "USD", "tipo_cambio": 1.0},
    {"pais": "El Salvador", "ciudad": "San Miguel", "moneda": "USD", "tipo_cambio": 1.0},
]

# ── Spanish full names ─────────────────────────────────────────────────
FIRST_NAMES = [
    "Carlos", "María", "José", "Ana", "Luis", "Carmen", "Miguel", "Rosa",
    "Jorge", "Elena", "Fernando", "Laura", "Andrés", "Patricia", "Santiago",
    "Diana", "Roberto", "Mónica", "Felipe", "Adriana", "Diego", "Sara",
    "Gabriel", "Claudia", "Ricardo", "Verónica", "Pablo", "Marcela",
    "Héctor", "Silvia", "Juan", "Karla", "Manuel", "Iveth", "Ronaldo",
    "Bianka", "Esteban", "Alejandra", "Oscar", "Yesenia"
]

LAST_NAMES = [
    "Ramírez", "García", "Rodríguez", "Martínez", "López", "Hernández",
    "González", "Pérez", "Cruz", "Morales", "Montecinos", "Sandoval",
    "Castillo", "Reyes", "Orellana", "Ponce", "Escobar", "Villalobos",
    "Acosta", "Campos", "Méndez", "Rivas", "Aguilar", "Chacón", "Navarro",
    "Solís", "Figueroa", "Cordero", "Vargas", "Brenes", "Quesada", "Pizarro",
    "Marín", "Zúñiga", "Calderón", "Bonilla", "Carvajal", "Cascante", "Quirós",
    "Alvarado"
]

# ── Monthly kWh ranges by house size ───────────────────────────────────
# Typical residential consumption in Central America
HOUSE_TYPES = [
    {"tipo": "Pequeña", "habitaciones": 2, "kwh_mensual_min": 180, "kwh_mensual_max": 350, "precio_sistema_min": 7500, "precio_sistema_max": 11000},
    {"tipo": "Mediana", "habitaciones": 3, "kwh_mensual_min": 350, "kwh_mensual_max": 600, "precio_sistema_min": 10500, "precio_sistema_max": 15000},
    {"tipo": "Grande", "habitaciones": 4, "kwh_mensual_min": 600, "kwh_mensual_max": 950, "precio_sistema_min": 14500, "precio_sistema_max": 20000},
    {"tipo": "Premium", "habitaciones": 5, "kwh_mensual_min": 950, "kwh_mensual_max": 1500, "precio_sistema_min": 19500, "precio_sistema_max": 28000},
]

# ── Monthly electricity bill in USD (estimated from kWh) ───────────────
# Average rate ~$0.18/kWh in Central America for residential
KWH_PRICE_USD = 0.18

# ── Budget score ranges (1-5, how well they can pay) ───────────────────
# mapped from house type
BUDGET_MAP = {"Pequeña": (1, 3), "Mediana": (2, 4), "Grande": (3, 5), "Premium": (4, 5)}

# ── Lead status options ────────────────────────────────────────────────
STATUS_WEIGHTS = {
    "lead_nuevo": 0.24,
    "cotizacion_enviada": 0.28,
    "negociacion": 0.20,
    "cerrado_ganado": 0.16,
    "cerrado_perdido": 0.12,
}

# ── Contact preferences ────────────────────────────────────────────────
CONTACT_PREFS = ["WhatsApp", "Teléfono", "Email", "Chat Web"]

# ── Motivations ────────────────────────────────────────────────────────
MOTIVATIONS = [
    "Ahorro en factura eléctrica",
    "Protección contra apagones",
    "Independencia energética",
    "Cuidado del medio ambiente",
    "Aumento del valor de la propiedad",
    "Energía limpia para la familia",
]

# ── Referral sources ───────────────────────────────────────────────────
REFERRAL_SOURCES = [
    ("Recomendación de amigo/familiar", 0.35),
    ("Redes sociales (Facebook/Instagram)", 0.20),
    ("Google / búsqueda en línea", 0.18),
    ("Ferias de construcción / eventos", 0.10),
    ("Anuncio en radio/TV", 0.08),
    ("Visita de vendedor puerta a puerta", 0.05),
    ("Partner (constructora / eléctrico)", 0.04),
]

# ── Annual income ranges in USD ────────────────────────────────────────
INCOME_RANGES = [
    (20000, 35000),   # Small home
    (35000, 60000),   # Medium home
    (55000, 90000),   # Large home
    (85000, 150000),  # Premium home
]


def generate_email(first, last):
    """Generate a plausible email address."""
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    # Remove accents for email
    first_clean = first.lower().replace("í", "i").replace("é", "e").replace("ó", "o").replace("á", "a").replace("ú", "u")
    last_clean = last.lower().replace("í", "i").replace("é", "e").replace("ó", "o").replace("á", "a").replace("ú", "u")
    domain = random.choice(domains)
    patterns = [
        f"{first_clean}.{last_clean}@{domain}",
        f"{first_clean}{last_clean}@{domain}",
        f"{first_clean[0]}{last_clean}@{domain}",
        f"{first_clean}{last_clean[0]}@{domain}",
    ]
    return random.choice(patterns)


def generate_phone(pais):
    """Generate phone number by country."""
    codes = {
        "Guatemala": "+502",
        "Costa Rica": "+506",
        "Panamá": "+507",
        "Honduras": "+504",
        "El Salvador": "+503",
    }
    code = codes[pais]
    digits = "".join([str(random.randint(0, 9)) for _ in range(8)])
    return f"{code} {digits[:4]}-{digits[4:]}"


def generate_nit(pais):
    """Generate a fake tax ID (NIT) format per country."""
    if pais == "Guatemala":
        return f"{random.randint(1000000, 9999999)}-{random.randint(0, 9)}"
    elif pais == "Costa Rica":
        return f"{random.randint(1, 9)}-{random.randint(100, 999)}-{random.randint(100000, 999999)}"
    elif pais in ("Panamá", "El Salvador"):
        return f"{random.randint(100, 999)}-{random.randint(100000, 999999)}-{random.randint(100, 999)}"
    elif pais == "Honduras":
        return f"{random.randint(100, 999)}-{random.randint(10000000, 99999999)}-{random.randint(0, 9)}"
    return str(random.randint(1000000, 99999999))


def generate_mac_address():
    """Return a randomized fake MAC address for a solar inverter."""
    import string
    hex_chars = string.hexdigits.upper()[:16]
    mac = ":".join("".join(random.choices(hex_chars, k=2)) for _ in range(6))
    return mac


def pick_status():
    """Pick a lead status respecting weights."""
    statuses, weights = zip(*STATUS_WEIGHTS.items())
    return random.choices(statuses, weights=weights, k=1)[0]


def pick_referral():
    """Pick a referral source."""
    sources, weights = zip(*REFERRAL_SOURCES)
    return random.choices(sources, weights=weights, k=1)[0]


def generate_profiles(count=25):
    """Generate `count` customer profiles."""
    profiles = []

    for i in range(1, count + 1):
        loc = random.choice(LOCATIONS)
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        house_type = random.choice(HOUSE_TYPES)

        kwh = random.randint(house_type["kwh_mensual_min"], house_type["kwh_mensual_max"])
        bill_usd = round(kwh * KWH_PRICE_USD, 2)

        system_price_min = house_type["precio_sistema_min"]
        system_price_max = house_type["precio_sistema_max"]
        budget_score = random.randint(*BUDGET_MAP[house_type["tipo"]])

        # Income in USD (annual)
        income_idx = HOUSE_TYPES.index(house_type)
        inc_min, inc_max = INCOME_RANGES[income_idx]
        annual_income = random.randint(inc_min, inc_max)

        # Financing viability
        # down payment: 15-30% of system price
        system_price = random.randint(system_price_min, system_price_max)
        down_payment_pct = round(random.uniform(0.15, 0.30), 2)
        down_payment_amount = round(system_price * down_payment_pct, 2)

        # Months of financing (12-84)
        months = random.choice([12, 24, 36, 48, 60, 72, 84])
        monthly_payment = round((system_price - down_payment_amount) / months, 2)

        # Savings estimate
        savings_monthly_usd = round(bill_usd * random.uniform(0.60, 0.90), 2)

        # Leverage hash for stable IDs
        raw_seed = f"{first}{last}{i}"
        customer_id = "CUST-" + hashlib.md5(raw_seed.encode()).hexdigest()[:8].upper()

        # Date created (within last 6 months)
        days_ago = random.randint(0, 180)
        created_date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")

        profile = {
            "id": customer_id,
            "nombre": f"{first} {last}",
            "primer_nombre": first,
            "apellido": last,
            "email": generate_email(first, last),
            "telefono": generate_phone(loc["pais"]),
            "pais": loc["pais"],
            "ciudad": loc["ciudad"],
            "direccion_resumen": f"Colonia {random.choice(['Las Flores', 'San Antonio', 'Los Olivos', 'El Carmen', 'Santa Eduviges', 'Villa Nueva', 'Escazú', 'Curridabat', 'Betania'])}",
            "nit": generate_nit(loc["pais"]),
            "tipo_vivienda": house_type["tipo"],
            "habitaciones": house_type["habitaciones"],
            "consumo_kwh_mensual": kwh,
            "factura_mensual_usd": bill_usd,
            "ingreso_anual_usd": annual_income,
            "puntaje_presupuesto": budget_score,
            "moneda_local": loc["moneda"],
            "tipo_cambio_local": loc["tipo_cambio"],
            "estado_lead": pick_status(),
            "fecha_registro": created_date,
            "motivacion_principal": random.choice(MOTIVATIONS),
            "fuente_referencia": pick_referral(),
            "preferencia_contacto": random.choice(CONTACT_PREFS),
            "tiene_aire_acondicionado": random.choice([True, False]),
            "tiene_bomba_agua": random.choice([True, False]),
            "sistema_estimado": {
                "precio_usd": system_price,
                "paneles_estimados": max(6, round(kwh / 40)),
                "capacidad_kwp": round(kwh / 150, 1),
                "bateria_kwh": random.choice([5.0, 7.5, 10.0, 13.2, 15.0, 19.2]),
                "ahorro_mensual_usd": savings_monthly_usd,
                "porcentaje_ahorro": round(savings_monthly_usd / bill_usd * 100, 1),
                "inversion_total": system_price,
                "enganche_usd": down_payment_amount,
                "enganche_porcentaje": down_payment_pct,
                "plazo_meses": months,
                "cuota_mensual_usd": monthly_payment,
                "tiempo_recuperacion_meses": round(system_price / (savings_monthly_usd * 0.85), 1),
            },
            "notas_comerciales": "",
            "tags": [],
        }

        # Tags based on profile
        tags = []
        if budget_score >= 4:
            tags.append("alto_presupuesto")
        elif budget_score <= 2:
            tags.append("sensible_al_precio")
        if profile["motivacion_principal"] == "Protección contra apagones":
            tags.append("zona_apagones")
        if house_type["tipo"] in ("Grande", "Premium"):
            tags.append("alto_consumo")
        if profile["fuente_referencia"].startswith("Recomendación"):
            tags.append("referido")
        if profile["tiene_aire_acondicionado"]:
            tags.append("clima_caluroso")
        profile["tags"] = tags

        profiles.append(profile)

    return profiles


def main():
    profiles = generate_profiles(25)
    output = {
        "meta": {
            "generado": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "generado_por": "Solystar Customer Profile Generator",
            "total_perfiles": len(profiles),
            "segmento": "Residencial Centroamérica",
            "version_esquema": "1.0",
        },
        "perfiles": profiles,
    }

    with open("customer_profiles.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Generados {len(profiles)} perfiles de clientes → customer_profiles.json")
    print()

    # ── Summary stats ──────────────────────────────────────────────────
    paises = {}
    for p in profiles:
        pais = p["pais"]
        paises[pais] = paises.get(pais, 0) + 1

    print("📊 Distribución por país:")
    for pais, count in sorted(paises.items(), key=lambda x: -x[1]):
        print(f"   {pais}: {count} clientes")

    print()
    print(f"💰 Precios de sistema: ${min(p['sistema_estimado']['precio_usd'] for p in profiles):,.0f} – ${max(p['sistema_estimado']['precio_usd'] for p in profiles):,.0f} USD")
    print(f"⚡ Consumo kWh: {min(p['consumo_kwh_mensual'] for p in profiles)} – {max(p['consumo_kwh_mensual'] for p in profiles)} kWh/mes")
    print(f"📋 Lead estados: {len(set(p['estado_lead'] for p in profiles))} estados únicos")

    by_status = {}
    for p in profiles:
        s = p["estado_lead"]
        by_status[s] = by_status.get(s, 0) + 1
    print("   Detalle:")
    for status, count in sorted(by_status.items(), key=lambda x: -x[1]):
        print(f"      {status}: {count}")


if __name__ == "__main__":
    main()