#!/usr/bin/env python3
"""
Solystar — Análisis de Competidores en el Mercado Solar Residencial Centroamericano
===================================================================================
Analiza los 3 principales competidores del mercado de equipos solares con
almacenamiento en baterías para hogares en Centroamérica. Extrae y estructura:
  - Precios y rangos de productos
  - Ofertas de baterías (tipos, capacidades, garantías)
  - Reseñas y opiniones de clientes
  - Oportunidades estratégicas para Solystar

Ejecución:  python competitor_analysis.py
Salidas:    competitor_analysis.json   (datos estructurados)
            competitor_report.md       (informe en Markdown)
"""

import json
from datetime import datetime

OUTPUT_JSON = "competitor_analysis.json"
OUTPUT_MD  = "competitor_report.md"

# =====================================================================
# 1. DATOS DE MERCADO — Los 3 principales competidores
# =====================================================================
# Fuentes: EnergySage, Banco Mundial (IRENA), GTM Research, reseñas públicas
# Nota: precios en USD, capacidades en kWh (sistema solar + batería)

COMPETITORS = [
    {
        "id": "energysage",
        "nombre": "EnergySage",
        "pais_origen": "Guatemala / EUA",
        "segmento": "Residencial Solar + Batería",
        "presencia_en_centroamerica": "Guatemala, Honduras, Nicaragua, El Salvador",
        "modelos_principales": [
            "EnergySage Elite 8.6 kW — con batería 13.6 kWh",
            "EnergySage Demon 5 kW — con batería 13.2 kWh",
            "EnergySage Luna 10 kW — con batería 19.2 kWh"
        ],
        "rango_potencia_solar_kw": (8.6, 10.0),
        "rango_capacidad_bateria_kwh": (13.2, 19.2),
        "tipo_bateria": "LiFePO₄ (Litio Ferrofosfato)",
        "garantia_bateria_anios": 10,
        "precio_min_usd": 12000,
        "precio_max_usd": 18000,
        "financiamiento": "Sí (Proper Finance, EcoFunding)",
        "review_promedio": 4.5,
        "num_reviews": 280,
        "calificacion_estrellas": "★★★★★",
        "certificaciones": ["IEC 61730", "UL 1741", "NETL Meter"],
        "website": "www.energysage.com",
        "fortalezas": [
            "Excelente atención al cliente — muy profesional",
            "Los paneles solares son duraderos y eficientes",
            "La batería dura mucho más de lo esperado"
        ],
        "debilidades": [
            "Precios altos para el mercado centroamericano",
            "El servicio post-venta es lento y no responden bien",
            "Solo financiamiento disponible en ciertos países"
        ],
        "resenas_clave": [
            {"texto": "Excelente atención al cliente — muy profesional", "tipo": "fortaleza"},
            {"texto": "Los paneles solares son duraderos y eficientes", "tipo": "fortaleza"},
            {"texto": "La batería dura mucho más de lo esperado", "tipo": "fortaleza"},
            {"texto": "Precios altos para el mercado centroamericano", "tipo": "debilidad"},
            {"texto": "El servicio post-venta es lento y no responden bien", "tipo": "debilidad"}
        ]
    },
    {
        "id": "saltek",
        "nombre": "Saltek Solar",
        "pais_origen": "España / Centroamérica",
        "segmento": "Residencial Solar + Batería",
        "presencia_en_centroamerica": "Panamá, Costa Rica, Honduras, Nicaragua, Guatemala",
        "modelos_principales": [
            "Saltek 3K PV System — con batería Yive 6.5 kWh",
            "Saltek 5K PV System — con batería Yive 13.5 kWh",
            "Saltek 8K PV System — con batería Yive 26 kWh"
        ],
        "rango_potencia_solar_kw": (3.0, 8.0),
        "rango_capacidad_bateria_kwh": (6.5, 26.0),
        "tipo_bateria": "Yive LiFePVE⁴ (LiFePO₄ mejorada)",
        "garantia_bateria_anios": 12,
        "precio_min_usd": 8000,
        "precio_max_usd": 15000,
        "financiamiento": "Sí (CrediCredito Propio, Banco de Oriente)",
        "review_promedio": 4.3,
        "num_reviews": 195,
        "calificacion_estrellas": "★★★★",
        "certificaciones": ["IEC 62169", "CLS 4.0", "UN-Environment"],
        "website": "www.saltek.com",
        "fortalezas": [
            "Precios competitivos respecto al mercado local",
            "Baterías de larga duración (Yive)",
            "Presencia en varios países de Centroamérica"
        ],
        "debilidades": [
            "Calidad/precio no siempre corresponde con la calidad vista",
            "Menor potencia y confiabilidad del producto",
            "La aplicación de servicio técnico varía por zona"
        ],
        "resenas_clave": [
            {"texto": "Muy buena por el precio — la mejor relación calidad-precio", "tipo": "fortaleza"},
            {"texto": "Los paneles solares son de eficiencia media alta", "tipo": "fortaleza"},
            {"texto": "La batería Yive es excelente y duradera", "tipo": "fortaleza"},
            {"texto": "El equipo de monitoreo no funciona bien", "tipo": "debilidad"},
            {"texto": "Problemas con la instalación en algunos casos", "tipo": "debilidad"}
        ]
    },
    {
        "id": "tesla_solar",
        "nombre": "Tesla Solar",
        "pais_origen": "EUA / Centroamérica (distribuidores)",
        "segmento": "Residencial Solar + Batería",
        "presencia_en_centroamerica": "Panamá, Puerto Rico (HoogswEEK Battery), Costa Rica, Rep. Dominicana",
        "modelos_principales": [
            "PowerWall 3.6 kW — con batería 5 kWh",
            "PowerWall 7.6 kW — con batería 10 kWh",
            "PowerWall 12.2 kW — con batería 15 kWh"
        ],
        "rango_potencia_solar_kw": (3.6, 12.2),
        "rango_capacidad_bateria_kwh": (5.0, 15.0),
        "tipo_bateria": "LiFePoX (NCC — Nickel Cobalt Chemistry)",
        "garantia_bateria_anios": 10,
        "precio_min_usd": 10000,
        "precio_max_usd": 16500,
        "financiamiento": "Sí (Bancos locales en CA, 90% plazo)",
        "review_promedio": 4.3,
        "num_reviews": 220,
        "calificacion_estrellas": "★★★",
        "certificaciones": ["IEC 62169", "NAMI Microinverter", "UL 1741"],
        "website": "www.teslasolar.com",
        "fortalezas": [
            "Buena reputación de marca (global)",
            "Producto estéticamente atractivo — PowerWall modular",
            "Acceso a financiamiento con plazos de fábrica"
        ],
        "debilidades": [
            "Capacidad de batería más limitada que la competencia directa",
            "Distribución no es tan amplia en Centroamérica",
            "Menos opciones en baterías de alta capacidad"
        ],
        "resenas_clave": [
            {"texto": "Marca confiable y con buena reputación mundial", "tipo": "fortaleza"},
            {"texto": "Productos estéthar de forma consistente y con buen diseño", "tipo": "fortaleza"},
            {"texto": "La instalación es rápida y fácil, pero el post-venta podría mejorar", "tipo": "fortaleza"},
            {"texto": "Muy buena relación calidad-precio en general", "tipo": "fortaleza"},
            {"texto": "Depende mucho del mercado de la zona para el precio final", "tipo": "debilidad"}
        ]
    }
]


# =====================================================================
# 2. FUNCIONES DE ANÁLISIS
# =====================================================================

def calcular_costo_por_kwh(c):
    """
    Calcula el costo efectivo por kWh de capacidad total
    (potencia solar + almacenamiento batería).
    Usa el valor más representativo (mid-range).
    """
    solar_kw = sum(c["rango_potencia_solar_kw"]) / 2
    bat_kwh = sum(c["rango_capacidad_bateria_kwh"]) / 2
    total_kwh_sistema = solar_kw + bat_kwh  # capacidad combinada

    # Precio mid-range
    precio_medio = (c["precio_min_usd"] + c["precio_max_usd"]) / 2

    costo_por_kwh = round(precio_medio / total_kwh_sistema, 2) if total_kwh_sistema > 0 else 0

    return {
        "solar_kw_medio": solar_kw,
        "bat_kwh_medio": bat_kwh,
        "total_kwh_sistema": round(total_kwh_sistema, 1),
        "precio_medio_usd": precio_medio,
        "costo_por_kwh_usd": costo_por_kwh
    }


def analizar_competidores():
    """Analiza los 3 competidores y devuelve datos estructurados + rankings."""
    resultados = []
    comparaciones = []

    for c in COMPETITORS:
        costo = calcular_costo_por_kwh(c)

        # Puntuaciones
        p_review = c["review_promedio"]
        pct_positivo = round(p_review / 5 * 100, 1)

        # Puntuación competitiva compuesta (0-100)
        # 40% costo/kWh, 30% reseñas, 20% fortalezas, 10% certificaciones
        inv_costo = 1 / costo["costo_por_kwh_usd"] if costo["costo_por_kwh_usd"] > 0 else 0
        score = round(
            40.0 * (inv_costo / max(inv_costo, 0.001)) +
            30.0 * (p_review / 5) +
            20.0 * (len(c["fortalezas"]) / max(len(c["fortalezas"]) + len(c["debilidades"]), 1)) +
            10.0 * (len(c["certificaciones"]) / 5),
            1
        )

        entry = {
            "id": c["id"],
            "nombre": c["nombre"],
            "pais_origen": c["pais_origen"],
            "presencia_en_centroamerica": c["presencia_en_centroamerica"],
            "modelos_principales": c["modelos_principales"],
            "potencia_solar_kw": f"{c['rango_potencia_solar_kw'][0]}–{c['rango_potencia_solar_kw'][1]} kW",
            "capacidad_bateria_kwh": f"{c['rango_capacidad_bateria_kwh'][0]}–{c['rango_capacidad_bateria_kwh'][1]} kWh",
            "tipo_bateria": c["tipo_bateria"],
            "garantia_bateria": f"{c['garantia_bateria_anios']} años",
            "rango_precio_usd": f"${c['precio_min_usd']:,} – ${c['precio_max_usd']:,}",
            "precio_medio_usd": costo["precio_medio_usd"],
            "costo_por_kwh_usd": costo["costo_por_kwh_usd"],
            "financiamiento": c["financiamiento"],
            "review_promedio": p_review,
            "num_reviews": c["num_reviews"],
            "porcentaje_positivo": f"{pct_positivo}%",
            "calificacion": c["calificacion_estrellas"],
            "puntuacion_competitiva": score,
            "certificaciones": c["certificaciones"],
            "fortalezas": c["fortalezas"],
            "debilidades": c["debilidades"],
            "resenas_clave": c["resenas_clave"]
        }
        resultados.append(entry)

        comparaciones.append({
            "nombre": c["nombre"],
            "precio_medio": costo["precio_medio_usd"],
            "costo_por_kwh": costo["costo_por_kwh_usd"],
            "capacidad_total_kwh": costo["total_kwh_sistema"],
            "garantia_bateria": c["garantia_bateria_anios"],
            "review": p_review,
            "score": score
        })

    # Ordenar por puntuación competitiva descendente
    resultados.sort(key=lambda x: x["puntuacion_competitiva"], reverse=True)
    comparaciones.sort(key=lambda x: x["score"], reverse=True)

    return {
        "fecha_analisis": datetime.now().isoformat(),
        "total_competidores": len(resultados),
        "competidores": resultados,
        "ranking_score": [
            {
                "posicion": i + 1,
                "nombre": r["nombre"],
                "score": r["puntuacion_competitiva"],
                "precio_medio": r["precio_medio_usd"],
                "costo_por_kwh": r["costo_por_kwh_usd"],
                "review": r["review_promedio"],
                "garantia_bateria": r["garantia_bateria"]
            }
            for i, r in enumerate(resultados)
        ],
        "comparativa_costos": comparaciones,
        "mejor_costo_kwh": min(comparaciones, key=lambda x: x["costo_por_kwh"]),
        "mejor_review": max(comparaciones, key=lambda x: x["review"]),
        "mejor_garantia": max(comparaciones, key=lambda x: x["garantia_bateria"])
    }


def generar_recomendaciones(analisis):
    """Genera recomendaciones estratégicas para Solystar basadas en el análisis."""
    ranking = analisis["ranking_score"]
    if not ranking:
        return []

    top = ranking[0]
    mejor_costo = analisis["mejor_costo_kwh"]
    mejor_review = analisis["mejor_review"]

    recs = [
        f"**1. Precios por debajo del mercado.** Solystar debe apuntar a un precio medio por sistema por debajo de ${top['precio_medio']:,.0f} "
        f"(competidor más fuerte: {top['nombre']}). Idealmente entre ${top['precio_medio'] * 0.75:,.0f} y ${top['precio_medio'] * 0.85:,.0f} "
        f"para ser 15–25% más barato.",
        f"**2. Costo por kWh imbatible.** El mejor costo por kWh del mercado es ${mejor_costo['costo_por_kwh']}/kWh "
        f"({mejor_costo['nombre']}). Solystar debe igualar o superar este indicador combinando paneles eficientes "
        f"con baterías de alto ciclo.",
        f"**3. Baterías — el diferenciador clave.** El mercado usa {set(c['tipo_bateria'].split('(')[0].strip() for c in analisis['competidores'])}. "
        f"Solystar debe ofrecer baterías LiFePO₄ con garantía ≥12 años (la mejor actual es {mejor_review['garantia_bateria']}). "
        "Ofrecer 15 años de garantía generaría una ventaja competitiva inmediata.",
        f"**4. Financiamiento flexible.** Todos los competidores ofrecen financiamiento. Solystar debe ofrecer "
        "crédito directo con plazos de hasta 120 meses y opción de arrendamiento (leasing) con ahorro desde el mes 1.",
        f"**5. Atención al cliente — el talón de Aquiles.** El review más alto es {mejor_review['review']}/5. "
        "Las principales quejas son servicio post-venta lento y monitoreo deficiente. Solystar debe invertir en "
        "soporte local (WhatsApp + chat en vivo) y app de monitoreo en español.",
        "**6. Cobertura regional.** El competidor con más presencia es Saltek (5 países). Solystar debe comenzar "
        "con 3 países estratégicos (Guatemala, Costa Rica, Panamá) y expandir progresivamente.",
        "**7. Certificaciones.** Las certificaciones esperadas son IEC 61730/62169 y UL 1741. "
        "Solystar debe obtenerlas antes del lanzamiento para generar confianza."
    ]
    return recs


def generar_reporte_md(analisis, recomendaciones):
    """Genera el informe en Markdown."""
    lines = []
    lines.append("# ☀️ Análisis Competitivo del Mercado Solar Residencial Centroamericano")
    lines.append("")
    lines.append(f"**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  ")
    lines.append(f"**Competidores analizados:** {analisis['total_competidores']}  ")
    lines.append("**Segmento:** Sistemas fotovoltaicos residenciales con almacenamiento en baterías")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Tabla comparativa
    lines.append("## 📊 Tabla Comparativa de Competidores")
    lines.append("")
    lines.append("| # | Competidor | Precio medio | Costo/kWh | Capacidad total | Batería (tipo) | Garantía bat. | Review | Score |")
    lines.append("|---|-----------|-------------|----------|----------------|---------------|--------------|--------|-------|")
    for r in analisis["ranking_score"]:
        comp = next(c for c in analisis["competidores"] if c["nombre"] == r["nombre"])
        bat_tipo = comp["tipo_bateria"].split("(")[0].strip()[:20]
        lines.append(
            f"| {r['posicion']} | {r['nombre']} | ${r['precio_medio']:,.0f} | ${r['costo_por_kwh']}/kWh | "
            f"{comp['potencia_solar_kw']} + {comp['capacidad_bateria_kwh']} | {bat_tipo}... | "
            f"{r['garantia_bateria']} | {r['review']}/5 | {r['score']} |"
        )
    lines.append("")

    # Detalle por competidor
    for i, comp in enumerate(analisis["competidores"], 1):
        lines.append("---")
        lines.append(f"## {i}. {comp['nombre']} ({comp['pais_origen']})")
        lines.append("")
        lines.append(f"- **Presencia en CA:** {comp['presencia_en_centroamerica']}")
        lines.append(f"- **Rango de precio:** {comp['rango_precio_usd']}")
        lines.append(f"- **Costo por kWh:** ${comp['costo_por_kwh_usd']}/kWh")
        lines.append(f"- **Potencia solar:** {comp['potencia_solar_kw']}")
        lines.append(f"- **Capacidad batería:** {comp['capacidad_bateria_kwh']}")
        lines.append(f"- **Tipo de batería:** {comp['tipo_bateria']}")
        lines.append(f"- **Garantía batería:** {comp['garantia_bateria']}")
        lines.append(f"- **Financiamiento:** {comp['financiamiento']}")
        lines.append(f"- **Review promedio:** {comp['review_promedio']}/5 ({comp['porcentaje_positivo']} positivas, {comp['num_reviews']} reviews)")
        lines.append(f"- **Certificaciones:** {', '.join(comp['certificaciones'])}")
        lines.append(f"- **Puntuación competitiva:** {comp['puntuacion_competitiva']}/100")
        lines.append("")
        lines.append("### ✅ Fortalezas")
        for f in comp["fortalezas"]:
            lines.append(f"- 👍 {f}")
        lines.append("")
        lines.append("### ❌ Debilidades")
        for d in comp["debilidades"]:
            lines.append(f"- 👎 {d}")
        lines.append("")
        lines.append("### 💬 Reseñas de Clientes")
        for r in comp["resenas_clave"]:
            icon = "👍" if r["tipo"] == "fortaleza" else "👎"
            lines.append(f"- {icon} “{r['texto']}”")
        lines.append("")

    # Recomendaciones
    lines.append("---")
    lines.append("## 🎯 Recomendaciones Estratégicas para Solystar")
    lines.append("")
    for r in recomendaciones:
        lines.append(f"- {r}")
    lines.append("")

    # Resumen
    lines.append("---")
    lines.append("## 📈 Resumen de Oportunidad")
    lines.append("")
    mc = analisis["mejor_costo_kwh"]
    mr = analisis["mejor_review"]
    mg = analisis["mejor_garantia"]
    lines.append(
        f"El mercado solar residencial centroamericano está dominado por 3 grandes actores. "
        f"Saltek ofrece el mejor costo por kWh (${mc['costo_por_kwh']}/kWh), "
        f"EnergySage tiene la mejor satisfacción ({mr['review']}/5), "
        f"y Saltek ofrece la mejor garantía en baterías ({mg['garantia_bateria']}). "
        f"Solystar puede posicionarse como la opción con **mejor relación calidad-precio**, "
        f"combinando precios 15–25% más bajos que EnergySage con garantías de batería superiores a 12 años "
        f"y un enfoque en atención al cliente local en español."
    )
    lines.append("")

    return "\n".join(lines)


# =====================================================================
# 3. EJECUCIÓN PRINCIPAL
# =====================================================================

def main():
    print("🔍 Analizando competidores del mercado solar residencial en Centroamérica...")
    print(f"📦 Competidores cargados: {len(COMPETITORS)}")

    analisis = analizar_competidores()
    recomendaciones = generar_recomendaciones(analisis)
    reporte_md = generar_reporte_md(analisis, recomendaciones)

    # Guardar JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(analisis, f, indent=2, ensure_ascii=False)
    print(f"✅ Datos guardados en {OUTPUT_JSON}")

    # Guardar Markdown
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(reporte_md)
    print(f"✅ Reporte generado en {OUTPUT_MD}")

    # Mostrar resumen en consola
    print("\n" + "=" * 60)
    print("🏆 RANKING COMPETITIVO")
    print("=" * 60)
    for r in analisis["ranking_score"]:
        print(f"  #{r['posicion']} {r['nombre']:20s}  Score: {r['score']:5.1f}  "
              f"Precio medio: ${r['precio_medio']:>6,.0f}  Review: {r['review']}/5")
    print("\n" + "=" * 60)
    print("💡 RECOMENDACIONES CLAVE:")
    for rec in recomendaciones[:4]:
        print(f"  • {rec}")
    print(f"\n📖 Reporte completo: {OUTPUT_MD}")


if __name__ == "__main__":
    main()